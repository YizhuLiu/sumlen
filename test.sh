#gold length
TEXT=data/cnndm41.tokenized.en-de
cp $TEXT/*.len* data-bin/cnndm41.tokenized.en-de

#python generate.py data-bin/cnndm41.tokenized.en-de \
# --save-path 4120lenParam --path checkpoints/fconv_cnndm41/checkpoint_best.pt \
#    --batch-size 128 --beam 5 --max-source-positions 500 \
#	--max-target-positions 200 --max-len-b 100


#arbitrary length
#python fortest.py 10 #10 is the desired length.

#python generate.py data-bin/cnndm41.tokenized.en-de \
# --save-path 4120lenParam --path checkpoints/fconv_cnndm41/checkpoint_best.pt \
#    --batch-size 128 --beam 5 --max-source-positions 500 \
#	--max-target-positions 200 --max-len-b 100
