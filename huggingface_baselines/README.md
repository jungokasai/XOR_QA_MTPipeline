# Hugging Face MT Models for XOR-TyDi

### Requirements and Installation

* [PyTorch](http://pytorch.org/) version >= 1.4.0
* [transformers](https://github.com/huggingface/transformers) version = 2.9.1 
* Python version >= 3.6

### Example Commands

```bash
python translate.py --in-file <input_file> \
--out-file  <ouput_file> --src-lang <source language [en,ja,ko,...]> --tgt-lang <target language [en, ja, ko,...]>
```
For example, run the following:
```bash
python translate.py --src-lang ja --tgt-lang en --in-file examples/example_ja.txt --out-file examples/example_ja-en.en.txt
```

### Reference
These [Hugging Face MT models](https://huggingface.co/Helsinki-NLP) were taken from [Helsinki NLP](https://github.com/Helsinki-NLP/OPUS-MT-train). Please cite accordingly.
