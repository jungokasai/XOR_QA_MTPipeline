# Download
wget -c https://object.pouta.csc.fi/OPUS-MultiUN/v1/moses/en-ru.txt.zip
# Tokenize
cd ~/projects/XORQA/XOR_data/XLM/
cat data/en-ru/MultiUN.en-ru.en | tools/tokenize.sh en > MultiUN.en-ru.moses.en
cat data/en-ru/MultiUN.en-ru.ru | tools/tokenize.sh ru > MultiUN.en-ru.moses.ru
# Split
cd ~/projects/XORQA/XOR_data/XLM/data/en-ru
bash ~/projects/XORQA/XOR_QA_MTPipeline/tokenizers/get-train.sh en-ru
# BPE
~/projects/fastBPE/fast learnbpe 32000 train.en-ru.en train.en-ru.ru > codes
~/projects/fastBPE/fast  applybpe train.bpe.en-ru.en  train.en-ru.en codes
~/projects/fastBPE/fast  applybpe train.bpe.en-ru.ru  train.en-ru.ru codes
~/projects/fastBPE/fast  applybpe valid.bpe.en-ru.en  valid.en-ru.en codes
~/projects/fastBPE/fast  applybpe valid.bpe.en-ru.ru  valid.en-ru.ru codes
~/projects/fastBPE/fast  applybpe test.bpe.en-ru.en  test.en-ru.en codes
~/projects/fastBPE/fast  applybpe test.bpe.en-ru.ru  test.en-ru.ru codes
# Binarize
python preprocess.py --destdir ~/projects/XORQA/XOR_data/XLM/data/en-ru/ --source-lang en --target-lang ru --testpref ~/projects/XORQA/XOR_data/XLM/data/en-ru/test.bpe.en-ru --trainpref ~/projects/XORQA/XOR_data/XLM/data/en-ru/train.bpe.en-ru --validpref ~/projects/XORQA/XOR_data/XLM/data/en-ru/valid.bpe.en-ru --workers 60 --joined-dictionary > ~/projects/XORQA/XOR_data/XLM/data/en-ru/preprocess.log
python preprocess.py --destdir ~/projects/XORQA/XOR_data/XLM/data/ru-en/ --source-lang ru --target-lang en --testpref ~/projects/XORQA/XOR_data/XLM/data/en-ru/test.bpe.en-ru --trainpref ~/projects/XORQA/XOR_data/XLM/data/en-ru/train.bpe.en-ru --validpref ~/projects/XORQA/XOR_data/XLM/data/en-ru/valid.bpe.en-ru --workers 60 --joined-dictionary > ~/projects/XORQA/XOR_data/XLM/data/ru-en/preprocess.log

# Spiece
 ./spm_train --input=$HOME//projects/XORQA/XOR_data/XLM/data/en-ja/opus.en-ja.en-ja --model_prefix=spiece.en-ja --vocab_size=32000 --character_coverage=1.0 --model_type=unigram
./spm_encode --model=spiece.en-ja.model --output_format=piece < ~/projects/XORQA/XOR_data/XLM/data/en-ja/opus.en-ja.ja > opus.spm.en-ja.ja
./spm_encode --model=spiece.en-ja.model --output_format=piece < ~/projects/XORQA/XOR_data/XLM/data/en-ja/opus.en-ja.en > opus.spm.en-ja.en

# Test
./spm_encode --model=spiece.en-ja.model --output_format=piece < ~/projects/XORQA/XOR_data/XLM/data/en-ja/xor/ja_en_dev_input.txt > ~/projects/XORQA/XOR_data/XLM/data/en-ja/xor/xor.spm.en-ja.ja
./spm_encode --model=spiece.en-ja.model --output_format=piece < ~/projects/XORQA/XOR_data/XLM/data/en-ja/xor/ja_en_dev_reference.txt > ~/projects/XORQA/XOR_data/XLM/data/en-ja/xor/xor.spm.en-ja.en
python preprocess.py --destdir ~/projects/XORQA/XOR_data/XLM/data/en-ja/xor/ --source-lang en --target-lang ja --trainpref ~/projects/XORQA/XOR_data/XLM/data/en-ja/xor/xor.spm.train.en-ja --validpref ~/projects/XORQA/XOR_data/XLM/data/en-ja/xor/xor.spm.dev.en-ja --workers 10 --srcdict ~/projects/XORQA/XOR_data/XLM/data/en-ja/dict.en.txt --tgtdict ~/projects/XORQA/XOR_data/XLM/data/en-ja/dict.ja.txt > ~/projects/XORQA/XOR_data/XLM/data/en-ja/xor/preprocess.log
python preprocess.py --destdir ~/projects/XORQA/XOR_data/XLM/data/ja-en/xor/ --source-lang ja --target-lang en --trainpref ~/projects/XORQA/XOR_data/XLM/data/en-ja/xor/xor.spm.train.en-ja --validpref ~/projects/XORQA/XOR_data/XLM/data/en-ja/xor/xor.spm.dev.en-ja --workers 10 --srcdict ~/projects/XORQA/XOR_data/XLM/data/en-ja/dict.ja.txt --tgtdict ~/projects/XORQA/XOR_data/XLM/data/en-ja/dict.en.txt > ~/projects/XORQA/XOR_data/XLM/data/ja-en/xor/preprocess.log
python generate.py ~/projects/XORQA/XOR_data/XLM/data/en-ja/xor/ --path /checkpoint/jkasai/trans_enja_6-6_mp/checkpoint_best.pt --lenpen 1.0 --beam 5 --max-sentences 100 --gen-subset train --remove-bpe sentencepiece > ~/projects/XORQA/XOR_data/XLM/data/en-ja/xor/xor.train.en-ja.out
python generate.py ~/projects/XORQA/XOR_data/XLM/data/en-ja/xor/ --path /checkpoint/jkasai/trans_enja_6-6_mp/checkpoint_best.pt --lenpen 1.0 --beam 5 --max-sentences 100 --gen-subset valid --remove-bpe sentencepiece > ~/projects/XORQA/XOR_data/XLM/data/en-ja/xor/xor.valid.en-ja.out
python generate.py ~/projects/XORQA/XOR_data/XLM/data/ja-en/xor/ --path /checkpoint/jkasai/trans_jaen_6-6_mp/checkpoint_best.pt --lenpen 1.0 --beam 5 --max-sentences 100 --gen-subset train --remove-bpe sentencepiece > ~/projects/XORQA/XOR_data/XLM/data/ja-en/xor/xor.train.ja-en.out
python generate.py ~/projects/XORQA/XOR_data/XLM/data/ja-en/xor/ --path /checkpoint/jkasai/trans_jaen_6-6_mp/checkpoint_best.pt --lenpen 1.0 --beam 5 --max-sentences 100 --gen-subset valid --remove-bpe sentencepiece > ~/projects/XORQA/XOR_data/XLM/data/ja-en/xor/xor.valid.ja-en.out
10 --gen-subset valid --remove-bpe sentencepiece >  ~/projects/XORQA/XOR_data/XLM/data/en-ja/xor/en-ja.ja.out
cat ~/projects/XORQA/XOR_data/XLM/data/en-ja/xor/xor.train.en-ja.out | grep -P '^H-' | cut -c3- | sort -n -k 1 |uniq | cut -f 3 > ~/projects/XORQA/XOR_data/XLM/data/en-ja/xor/xor.train.en-ja.ja.pred
cat ~/projects/XORQA/XOR_data/XLM/data/en-ja/xor/xor.valid.en-ja.out | grep -P '^H-' | cut -c3- | sort -n -k 1 |uniq | cut -f 3 > ~/projects/XORQA/XOR_data/XLM/data/en-ja/xor/xor.valid.en-ja.ja.pred
cat ~/projects/XORQA/XOR_data/XLM/data/ja-en/xor/xor.train.ja-en.out | grep -P '^H-' | cut -c3- | sort -n -k 1 |uniq | cut -f 3 > ~/projects/XORQA/XOR_data/XLM/data/ja-en/xor/xor.train.ja-en.en.pred
cat ~/projects/XORQA/XOR_data/XLM/data/ja-en/xor/xor.valid.ja-en.out | grep -P '^H-' | cut -c3- | sort -n -k 1 |uniq | cut -f 3 > ~/projects/XORQA/XOR_data/XLM/data/ja-en/xor/xor.valid.ja-en.en.pred
