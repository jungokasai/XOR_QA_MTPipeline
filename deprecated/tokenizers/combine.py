import stanfordnlp, sys, argparse

def combine():
    with open('all.ar-en.ar', 'wt') as fout:
        for i in range(200):
            with open('train_{}.ar-en.ar'.format(i)) as fin:
                print('train_{}.ar-en.ar'.format(i))
                for line in fin:
                    fout.write(line)
                 


if __name__ == '__main__':
    combine()
