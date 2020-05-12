## if one of them is empty, delete that instance
fout_0 = open('kyoto-train.stanford.clean.en', 'wt')
fout_1 = open('kyoto-train.stanford.clean.ja', 'wt')
with open('kyoto-train.stanford.en' 'rt') as fin_0:
    with open('kyoto-train.stanford.ja', 'rt') as fin_1:
        for line_0, line_2 in zip(fin_0, fin_1):
            line_0 = line_0.strip()
            line_1 = line_1.strip()
            if (line_0 == '') or (line_1 == ''):
                continue
            fout_0.write(line_0)
            fout_0.write('\n')
            fout_1.write(line_1)
            fout_1.write('\n')
