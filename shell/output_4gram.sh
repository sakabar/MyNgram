#!/bin/zsh

 zcat /raid_back/lrscp/data/ngram/original/vol1/data/4gms/*.gz /raid_back/lrscp/data/ngram/original/vol2/data/4gms/*.gz <(echo "DAMMY DAMMY DAMMY DAMY\t1" | gzip -c) | python src/output_4gram.py

# echo "<S> ＞ ＞ ＞\t1""\n""DAMMY DAMMY DAMMY DAMY\t1" | python src/output_4gram.py
