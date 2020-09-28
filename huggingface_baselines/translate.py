import transformers
import argparse
parser = argparse.ArgumentParser(allow_abbrev=False)

parser.add_argument('--batch-size', default=20, type=int, metavar='N',
                    help='batch size')
parser.add_argument('--src-lang', type=str, metavar='N', 
                    help='source language id')
parser.add_argument('--tgt-lang', type=str, metavar='N', 
                    help='target language id')
parser.add_argument('--in-file', type=str, metavar='N',
                    help='source file')
parser.add_argument('--out-file', type=str, metavar='N',
                    help='target file')
parser.add_argument('--num-shards', default=1, type=int, metavar='N',
                    help='number of shards')
parser.add_argument('--shard-id', default=0, type=int, metavar='N',
                    help='shard id')

args = parser.parse_args()

def translate(src_lang,
              tgt_lang,
              in_file,
              out_file,
              batch_size,
              num_shards,
              shard_id,
              ):

    model_name = 'Helsinki-NLP/opus-mt-{}-{}'.format(src_lang, tgt_lang)
    try:
        tokenizer = transformers.AutoTokenizer.from_pretrained(model_name)
    except:
        raise RuntimeError(
            "language direction {}-{} is not supported by Hugging Face".format(src_lang, tgt_lang))
    model = transformers.AutoModelWithLMHead.from_pretrained(model_name)

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
        text = src_sents[i*batch_size:(i+1)*batch_size]
        data = tokenizer.prepare_translation_batch(text)
        data.to('cuda')
        output = model.generate(**data)
        output = [tokenizer.decode(t, skip_special_tokens=True) for t in output]
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
    translate(args.src_lang,
              args.tgt_lang,
              args.in_file,
              args.out_file,
              args.batch_size,
              args.num_shards,
              args.shard_id,
              )
