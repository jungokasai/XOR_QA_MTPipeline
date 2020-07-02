import transformers
import sys

lang = sys.argv[1]
in_file = sys.argv[2]
out_file = 'out.txt'

pair = 'ja-en'
tokenizer = transformers.AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-{}".format(pair))

langs = pair.split('-')
if lang == langs[0]:
    tokenizer.current_spm = tokenizer.spm_source
elif lang == langs[1]:
    tokenizer.current_spm = tokenizer.spm_target
else:
    raise

with open(in_file) as fin:
    with open(out_file, 'wt') as fout:
        for line in fin:
            data = line.strip()
            data = tokenizer._tokenize(data)
            fout.write(' '.join(data))
            fout.write('\n')
