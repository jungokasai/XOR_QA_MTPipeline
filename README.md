# XORQA Machine Translation Baselines
This repository contains baseline code for Machine Translation in the XORQA task.

## How to setup
0. install python packages
```
pip -r install requirements.txt
```
1. Download data
```
bash download.sh
```

2. Preprocess data

* Tokenize with [Stanford NLP](https://stanfordnlp.github.io/stanfordnlp/)
* Run BPE
* Index and binarize data

Will update with a one-line command. For now all separate sub-directories.

```
python preprocess_mt_data.py --dest-dir <destination-dir> \
--lang [en,ja,...] --outfile <output-file-name> \
--joined-dictionary \
```

3. Train a model with fairseq

4. Generate text
```
python preprocess_mt_data.py --dest-dir <destination-dir> \
--lang [en,ja,...] --outfile <output-file-name> \
--joined-dictionary \
```
