#!/bin/zsh

#一例。長さで割って対数確率を比較し、より高くなった文のみ出力
lv output_calc_with_trigram.txt | awk -F'\t' -f shell/normalize.awk | awk -F'\t' '$4 > $2 {print $0}'
