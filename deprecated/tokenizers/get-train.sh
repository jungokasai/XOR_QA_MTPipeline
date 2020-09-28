PARA_PATH=$PWD
pair=$1
split_data() {
    get_seeded_random() {
        seed="$1"; openssl enc -aes-256-ctr -pass pass:"$seed" -nosalt </dev/zero 2>/dev/null
    };
    NLINES=`wc -l $1  | awk -F " " '{print $1}'`;
    NTRAIN=$((NLINES - 10000));
    NVAL=$((NTRAIN + 5000));
    shuf --random-source=<(get_seeded_random 42) $1 | head -$NTRAIN             > $2;
    shuf --random-source=<(get_seeded_random 42) $1 | head -$NVAL | tail -5000  > $3;
    shuf --random-source=<(get_seeded_random 42) $1 | tail -5000                > $4;
}
for lg in $(echo $pair | sed -e 's/\-/ /g'); do
  split_data $PARA_PATH/opus.spm.$pair.$lg $PARA_PATH/train.spm.$pair.$lg $PARA_PATH/valid.spm.$pair.$lg $PARA_PATH/test.spm.$pair.$lg
  #split_data $PARA_PATH/opus.$pair.$lg $PARA_PATH/train.$pair.$lg $PARA_PATH/valid.$pair.$lg $PARA_PATH/test.$pair.$lg
  #split_data $PARA_PATH/opus.hf.$pair.$lg $PARA_PATH/train.hf.$pair.$lg $PARA_PATH/valid.hf.$pair.$lg $PARA_PATH/test.hf.$pair.$lg
done
