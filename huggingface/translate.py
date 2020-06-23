import transformers
import sys

def translate(in_file, lang='ja-en', out_file='tgt.txt'):
    tokenizer = transformers.AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-{}".format(lang))
    model = transformers.AutoModelWithLMHead.from_pretrained("Helsinki-NLP/opus-mt-{}".format(lang))
    src_text = get_src_text(in_file)
    #translated = []
    #for sent in src_text:
    #    #print(sent)
    #    out = model.generate(**tokenizer.prepare_translation_batch([sent]))
    #    translated.append(out)
    #    print(tokenizer.decode(out, skip_special_tokens=True))
    import IPython as ipy
    ipy.embed()
    translated = model.generate(**tokenizer.prepare_translation_batch(src_text))
    tgt_text = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]
    out_src_text(tgt_text, out_file)


def get_src_text(in_file):
    src_text = []
    with open(in_file) as fin:
        for line in fin:
            src_text.append(line.strip())
    return src_text

def out_src_text(src_text, out_file):
    with open(out_file, 'wt') as fout:
        for line in src_text:
            fout.write(line.strip())
            fout.write('\n')
    return src_text

if __name__ == '__main__':
    in_file = sys.argv[1]
    lang = sys.argv[2]
    out_file = sys.argv[3]
    translate(in_file, lang, out_file)
