#!/bin/zsh

set -eu

if [ $# -ne 2 ]; then
  echo "Argument Error" >&2
  exit 1
fi

# n=4
n=$2 #ngarmのnを第2引数で指定する

cache_name=cache/$n'-gram_prob.cache.old'
if [ -e $cache_name ]; then
  shell/wakati_two_strs.sh $1 | python src/calc_two_strs_prob.py $cache_name 

  #もし元のキャッシュと新しいキャッシュが同一ではなかったらメッセージを表示
  if [ `diff $cache_name $cache_name:r".new" | wc -l` -ne 0 ]; then
    echo "Argument Error" >&2
  else
    mv $cache_name:r".new" $cache_name
  fi

else
  shell/wakati_two_strs.sh $1 | python src/calc_two_strs_prob.py
  mv $cache_name:r".new" $cache_name
fi



