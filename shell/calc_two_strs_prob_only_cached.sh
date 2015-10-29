#!/bin/zsh

set -eu

if [ $# -ne 2 ]; then
  echo "Argument Error" >&2
  exit 1
fi

two_colmn_file=$1
cached_ngram_prob=$2

shell/wakati_two_strs.sh $two_colmn_file | python src/calc_two_strs_prob_only_cached.py $cached_ngram_prob
  # mv $cache_name:r".new" $cache_name



