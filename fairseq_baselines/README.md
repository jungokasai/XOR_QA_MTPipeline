# OPUS MT Transformer Base Models for XOR-TyDi

### Download Trained Transformer Base Models

Language |→ English |English →  | Bitext | # Sents | Preprocess | 
---|---|---|---|---|---|
Arabic | [model](https://drive.google.com/uc?id=1gaMwPd6aXr1qGBAQWK_P05lL2eK9uKVI)|  [model](https://drive.google.com/uc?id=1gR78oAPtWlvesMD9oLEGJKnf0lUU6PS6)  | [multi_un](https://drive.google.com/uc?id=1wJOEYNT8szepLEKb8tQsnD36A7DIiXcj) | 9.76M | [moses](https://github.com/moses-smt/mosesdecoder/tree/master/scripts/tokenizer)+[BPE](https://github.com/glample/fastBPE) 
Bengali | [model](https://drive.google.com/uc?id=1DFN4Uo6QQXk4MckWp-Ebc9uRv9tXC_qv)| [model](https://drive.google.com/uc?id=1yGv4gXg1H8x7lgM6F6d16FkhLBLuUrws)  | [opus](https://drive.google.com/uc?id=1d2z3SKv9OyYWwsxTJfknpgt1r1UT3jvx) | 920K | [sentencepiece](https://github.com/google/sentencepiece) 
Finnish| [model](https://drive.google.com/uc?id=19gaMSTGUPbeErGaWnsduBrel_eGpPx7J) | [model](https://drive.google.com/uc?id=1l4rUzYPUNiO9sYcjoCaBK_b7XKJwYVFu)  | [opus](https://drive.google.com/uc?id=1wk7U--iUsHJ0auaR26arRG6ckm0mVMWi) | 44.4M |[moses](https://github.com/moses-smt/mosesdecoder/tree/master/scripts/tokenizer)+[BPE](https://github.com/glample/fastBPE) 
Indonesian | [model](https://drive.google.com/uc?id=1CJCa-CuYZwwGkXbURBIGZfeQmW_1E9I5) | [model](https://drive.google.com/uc?id=1xwOjzz9WCoMQ29eC1CrLC_l_Ql8d6c-H)  | [opus](https://drive.google.com/uc?id=1jxRxUL0vpuPDD0IbzIUAfiBetV0wa6bf) | 10.2M | [sentencepiece](https://github.com/google/sentencepiece) 
Japanese | [model](https://drive.google.com/uc?id=1M8zKXtcrzMWNIytFREgd6l9lSOfgmMbQ) | [model](https://drive.google.com/uc?id=1SJwVsbGdLWYYJPbIsvTLPcG9e0-VnnSp) | [opus](https://drive.google.com/uc?id=14mq-MRVUqErP3bblg7B4oeKLsBvBx8Q_) | 3.03M | [sentencepiece](https://github.com/google/sentencepiece) 
Kiswahili | [model](https://drive.google.com/uc?id=1ZUmXGVIw1MwlwGkqc6D3qI5133aG1cg4) | [model](https://drive.google.com/uc?id=1gz9bZ_WELnJEDonIfrhc_LhyOr5JP3Qk)  | [opus](https://drive.google.com/uc?id=1vGu36fMQ6lsQdrDAvcmBAx7CYjanQvUt) | 170K | [sentencepiece](https://github.com/google/sentencepiece)
Korean | [model](https://drive.google.com/uc?id=1IqXuhXqMtaXa1SNI9Ku4DNR4aXlpiJqj) | [model](https://drive.google.com/uc?id=178l--ieKjgFQLGzNBwozD3MsfrOCwFNC)  | [opus](https://drive.google.com/uc?id=1uXCxiRsHERsqL8O8UDLWLNeJxmreqjpB) | 2.16M | [sentencepiece](https://github.com/google/sentencepiece) 
Russian | [model](https://drive.google.com/uc?id=1z2RYTBpkVMxgLogFl8EplSEmigRiHvrZ) | [model](https://drive.google.com/uc?id=1t5Xeb-nw-Lf2sUGpB8UubCibchs3Y51E)  | [WMT19](http://www.statmt.org/wmt19/) | 43.6M | [moses](https://github.com/moses-smt/mosesdecoder/tree/master/scripts/tokenizer)+[BPE](https://github.com/glample/fastBPE) 
Telegu | [model](https://drive.google.com/uc?id=1iLGSX-5LgY2v8mIAxZHDGxMCUmwmbbER) | [model](https://drive.google.com/uc?id=1siz00Sek5qwIiG7CGEqwvvhiOc9Zlqxm) | [opus](https://drive.google.com/uc?id=1cJRcBZoPkUM8vovLuLf8vDFL674M5y72) | 116K   | [sentencepiece](https://github.com/google/sentencepiece) 
Thai | [model](https://drive.google.com/uc?id=1rTLBabW7PQNBP6XcDvhZ6T1B4ba5R7A7) | [model](https://drive.google.com/uc?id=1XCfNVbjJfm-eL_IgWTlSnQSAPWsvTC63)  | [opus](https://drive.google.com/uc?id=1bBxT4M-ZZrU17-c2kFdVuObSby4WwH91) | 3.84M | [sentencepiece](https://github.com/google/sentencepiece) 

### Requirements and Installation

* [PyTorch](http://pytorch.org/) version >= 1.4.0
* [fairseq](https://github.com/pytorch/fairseq) version = 0.9.0
* Python version >= 3.6

### Example Commands

#### moses+BPE (ar, fi, and ru)
```bash
python translate.py --in-file <input_file> \
--out-file  <ouput_file> --model-dir <path_to_model_dir> --moses
```
#### sentencepiece (all other languages)
```bash
python translate.py --in-file <input_file> \
--out-file  <ouput_file> --model-dir <path_to_model_dir> --spiece
```

### Complete Script to Download and Run ja→en
```bash
python scripts/download_run_ja-en.py
```
