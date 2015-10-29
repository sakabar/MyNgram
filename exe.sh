#!/bin/zsh

set -ue

inputdir=input151026_2300
replaceddir=~/work/replace_with_antonym/output151026_2214 #反義語を置き換えたファイルの元の場所
output_ngram_file=fourgram_keys.txt
outputdir=output151026_2300_fourgram
outputfile=fourgram_log_p.txt

cp $replaceddir/*.txt $inputdir/
cat $inputdir/orig.txt $inputdir/changed.txt | mecab -O wakati | python src/get_ngram.py | sort | uniq > $output_ngram_file

time (./shell/output_4gram.sh 2>$outputdir/$outputfile > /local/tsakaki/$outputfile )

