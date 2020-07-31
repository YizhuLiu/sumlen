# sumlen
This code is for EMNLP 2018 paper: [![Controlling Length in Abstractive Summarization Using a Convolutional Neural Network]](https://www.aclweb.org/anthology/D18-1444/)

In this paper, we propose an approach to constrain the summary length by extending a convolutional sequence to sequence model ([Paper]:https://arxiv.org/abs/1705.03122 , [Code(fairseq-py)]: https://github.com/pytorch/fairseq).

citation:
@inproceedings{DBLP:conf/emnlp/LiuLZ18,
  author    = {Yizhu Liu and
               Zhiyi Luo and
               Kenny Q. Zhu},
  title     = {Controlling Length in Abstractive Summarization Using a Convolutional
               Neural Network},
  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural
               Language Processing, Brussels, Belgium, October 31 - November 4, 2018},
  pages     = {4110--4119},
  year      = {2018}
}

# Requirements
PyTorch version >= 0.4.0
Python version >= 3.6

pip install -r requirments

# Data Preprocessing
1. We use CNN/Daily Mail as dataset and get train/valid/test sets according to [See et al. 2017]:https://github.com/abisee/cnn-dailymail. 
   The preprocessed data can be downloaded from [here]:https://drive.google.com/file/d/1KjzKYhpsIwBKiNZx5x-NiYQabumY3qkY/view?usp=sharing .
2. python -u preprocess.py --source-lang en --target-lang de --trainpref $TEXT/train --validpref $TEXT/valid --testpref $TEXT/test --destdir data-bin/cnndm41.tokenized.en-de --thresholdtgt 20 --thresholdsrc 20

# Training
TEXT=data/cnndm41.tokenized.en-de

python length.py
cp $TEXT/*.len* data-bin/cnndm41.tokenized.en-de

mkdir -p checkpoints/fconv_cnndm41

CUDA_VISIBLE_DEVICES=0 python -u train.py data-bin/cnndm41.tokenized.en-de --lr 0.2 --clip-norm 0.1 --dropout 0.2 --max-tokens 4000 --label-smoothing 0.1 --force-anneal 200 --save-dir checkpoints/fconv_cnndm41 --arch fconv_cnndm_en_de --skip-invalid-size-inputs-valid-test --sample-without-replacement 3850 --max-source-positions 500 --max-target-positions 200

The pretrained model can be downloaded from 

# Testing
TEXT=data/cnndm41.tokenized.en-de

1. Gold Length
cp $TEXT/*.len* data-bin/cnndm41.tokenized.en-de

python generate.py data-bin/cnndm41.tokenized.en-de \
 --save-path 4120lenParam --path checkpoints/fconv_cnndm41/checkpoint_best.pt \
 --batch-size 128 --beam 5 --max-source-positions 500 \
 --max-target-positions 200 --max-len-b 100


2. Arbitrary Length
python fortest.py 10 #10 is the desired length.
python generate.py data-bin/cnndm41.tokenized.en-de \
 --save-path 4120lenParam --path checkpoints/fconv_cnndm41/checkpoint_best.pt \
 --batch-size 128 --beam 5 --max-source-positions 500 \
 --max-target-positions 200 --max-len-b 100

