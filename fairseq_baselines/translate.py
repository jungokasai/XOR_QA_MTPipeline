import argparse, os
from fairseq.models.transformer import TransformerModel
parser = argparse.ArgumentParser(allow_abbrev=False)
# fmt: off

parser.add_argument('--batch-size', default=20, type=int, metavar='N',
                    help='batch size')
parser.add_argument('--model-dir', type=str, metavar='N', 
                    help='model directory')
parser.add_argument('--model-name', type=str, metavar='N', 
                    default='checkpoint_best_average.pt', help='model name')
parser.add_argument('--in-file', type=str, metavar='N',
                    help='source file')
parser.add_argument('--out-file', type=str, metavar='N',
                    help='target file')
parser.add_argument('--num-shards', default=1, type=int, metavar='N',
                    help='number of shards')
parser.add_argument('--shard-id', default=0, type=int, metavar='N',
                    help='shard id')
parser.add_argument('--spiece', default=False, action='store_true',
                    help='Sentence Piece')
parser.add_argument('--moses', default=False, action='store_true',
                    help='Moses tokenize/detokenize')
parser.add_argument('--lenpen', default=1.0, type=float, metavar='N',
                    help='length penalty')
parser.add_argument('--beam', default=5, type=int, metavar='N',
                    help='beam size')
args = parser.parse_args()

def translate(model_dir,
              in_file,
              out_file,
              batch_size,
              model_name,
              num_shards,
              shard_id,
              moses,
              spiece,
              lenpen,
              beam,
              ):
    if moses:
        tokenizer = 'moses'
    else:
        tokenizer = None
    if spiece:
        model = TransformerModel.from_pretrained(model_dir,
                                                 checkpoint_file=model_name,
                                                 data_name_or_path=model_dir,
                                                 bpe='sentencepiece',
                                                 sentencepiece_model=os.path.join(model_dir, 'spiece.model'),
                                                 tokenizer=tokenizer,
                                                 )
    else:
        model = TransformerModel.from_pretrained(model_dir,
                                                 checkpoint_file=model_name,
                                                 data_name_or_path=model_dir,
                                                 bpe='subword_nmt',
                                                 bpe_codes=os.path.join(model_dir, 'bpecodes'),
                                                 tokenizer=tokenizer,
                                                 )
                                                    

    start_id, end_id = get_line_ids(in_file, num_shards, shard_id)
    print(start_id, end_id)
    src_sents = []
    model.cuda()
    with open(in_file) as fin:
        for i, line in enumerate(fin):
            if start_id <= i < end_id:
                line = line.strip()
                src_sents.append(line)
    nb_sents = len(src_sents)
    nb_batches = (nb_sents+batch_size-1)//batch_size
    outputs = []
    for i in range(nb_batches):
        print('Batch ID: {}/{}'.format(i, nb_batches))
        output = model.translate(src_sents[i*batch_size:(i+1)*batch_size], lenpen=lenpen, beam=beam)
        outputs.extend(output)
    with open(out_file, 'wt') as fout:
        for output in outputs:
            fout.write(output)
            fout.write('\n')


def get_line_ids(in_file, num_shards, shard_id):
    nb_lines = sum(1 for i in open(in_file, 'rb'))
    shard_size = nb_lines//num_shards
    remainder = nb_lines - shard_size*num_shards
    start_id = shard_size*shard_id + min([shard_id, remainder])
    end_id = shard_size*(shard_id+1) + min([shard_id+1, remainder])
    return start_id, end_id


if __name__ == '__main__':
    translate(args.model_dir,
              args.in_file,
              args.out_file,
              args.batch_size,
              args.model_name,
              args.num_shards,
              args.shard_id,
              args.moses,
              args.spiece,
              args.lenpen,
              args.beam,
              )
