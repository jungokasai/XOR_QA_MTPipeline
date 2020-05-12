import stanfordnlp, sys

def tokenize(in_file, lang, out_file):
    nlp = stanfordnlp.Pipeline(processors='tokenize', lang=lang)
    with open(in_file) as fin:
        with open(out_file, 'wt') as fout:
            for line in fin:
                line = line.strip()
                try:
                    doc = nlp(line)
                except:
                    fout.write('\n')
                    continue
                sent = []
                for i, sentence in enumerate(doc.sentences):
                    for token in sentence.tokens:
                        sent.append(token.text)
                fout.write(' '.join(sent))
                fout.write('\n')

if __name__ == '__main__':
    in_file = sys.argv[1]
    lang = sys.argv[2]
    out_file = sys.argv[3]
    tokenize(in_file, lang, out_file)
