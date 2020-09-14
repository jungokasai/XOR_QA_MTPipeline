import sys
with open(sys.argv[1]) as fin:
    with open('bpecodes', 'wt') as fout:
        fout.write('#version: 0.2\n')
        for line in fin:
            line = line.split()
            line = line[:-1]
            line = ' '.join(line)
            fout.write(line)
            fout.write('\n')
