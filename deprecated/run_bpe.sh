lang1=$1
lang2=$2
OUTPUT_DIR=${OUTPUT_DIR:-$PWD}
DATA_DIR=${DATA_DIR:-$HOME/data-bin/master/multi-un/}
# Learn Shared BPE
for merge_ops in 32000; do
  echo "Learning BPE with merge_ops=${merge_ops}. This may take a while..."
  cat "${DATA_DIR}/train.${lang1}-${lang2}.${lang1}" "${DATA_DIR}/train.${lang1}-${lang2}.${lang2}" | \
    ${OUTPUT_DIR}/subword-nmt/learn_bpe.py -s $merge_ops > "${DATA_DIR}/bpe.${lang1}-${lang2}.${merge_ops}"

  echo "Apply BPE with merge_ops=${merge_ops} to tokenized files..."
  for lang in $lang1 $lang2; do
    for f in ${DATA_DIR}/*.${lang1}-${lang2}.${lang}; do
      outfile="${f%.*}.bpe.${merge_ops}.${lang}"
      ${OUTPUT_DIR}/subword-nmt/apply_bpe.py -c "${DATA_DIR}/bpe.${lang1}-${lang2}.${merge_ops}" < $f > "${outfile}"
      echo ${outfile}
    done
  done

done

echo "All done."
