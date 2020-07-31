TEXT=data/cnndm41.tokenized.en-de

python -u preprocess.py --source-lang en --target-lang de --trainpref $TEXT/train --validpref $TEXT/valid --testpref $TEXT/test --destdir data-bin/cnndm41.tokenized.en-de --thresholdtgt 20 --thresholdsrc 20

python length.py

cp $TEXT/*.len* data-bin/cnndm41.tokenized.en-de

mkdir -p checkpoints/fconv_cnndm41

CUDA_VISIBLE_DEVICES=0 python -u train.py data-bin/cnndm41.tokenized.en-de --lr 0.2 --clip-norm 0.1 --dropout 0.2 --max-tokens 4000 --label-smoothing 0.1 --force-anneal 200 --save-dir checkpoints/fconv_cnndm41 --arch fconv_cnndm_en_de --skip-invalid-size-inputs-valid-test --sample-without-replacement 3850 --max-source-positions 500 --max-target-positions 200
