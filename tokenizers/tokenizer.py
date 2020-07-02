import stanfordnlp, sys, argparse
parser = argparse.ArgumentParser(allow_abbrev=False)
# fmt: off

parser.add_argument('--num-shards', default=1, type=int, metavar='N',
                    help='number of shards')
parser.add_argument('--shard-id', default=0, type=int, metavar='N',
                    help='shard id')
parser.add_argument('--in-file', type=str, metavar='N', help='input file name')
parser.add_argument('--out-file', type=str, metavar='N', help='output file name')
parser.add_argument('--lang', default='en', type=str, metavar='N', help='target language')

args = parser.parse_args()

def tokenize(in_file, lang, out_file, num_shards, shard_id):
    start_id, end_id = get_line_ids(in_file, num_shards, shard_id)
    print(start_id, end_id)
    nlp = stanfordnlp.Pipeline(processors='tokenize', lang=lang)
    with open(in_file) as fin:
        with open(out_file, 'wt') as fout:
            for i, line in enumerate(fin):
                if start_id <= i < end_id:
                    line = line.strip()
                    if line == '':
                        fout.write('\n')
                        continue
                    doc = nlp(line)
                    sent = []
                    for i, sentence in enumerate(doc.sentences):
                        for token in sentence.tokens:
                            sent.append(token.text)
                    fout.write(' '.join(sent))
                    fout.write('\n')

def get_line_ids(in_file, num_shards, shard_id):
    nb_lines = sum(1 for i in open(in_file, 'rb'))
    shard_size = nb_lines//num_shards
    remainder = nb_lines - shard_size*num_shards
    start_id = shard_size*shard_id + min([shard_id, remainder])
    end_id = shard_size*(shard_id+1) + min([shard_id+1, remainder])
    return start_id, end_id


if __name__ == '__main__':
    in_file = args.in_file
    lang = args.lang
    out_file = args.out_file
    num_shards = args.num_shards
    shard_id = args.shard_id
    assert shard_id < num_shards
    tokenize(in_file, lang, out_file, num_shards, shard_id)
