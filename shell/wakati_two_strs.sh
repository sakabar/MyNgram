#!/bin/zsh

set -eu

if [ $# -ne 1 ]; then
  echo "Argument Error" >&2
  exit 1
fi

# file_name=~/work/replace_with_antonym/output.txt
file_name=$1
paste -d '\t' <(lv $file_name | awk '{print $1}' | mecab -O wakati ) \
              <(lv $file_name | awk '{print $2}' | mecab -O wakati) 
