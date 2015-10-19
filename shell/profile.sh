#!/bin/zsh
cat - | head -n1 | mecab -O wakati | python -m cProfile -s time src/main.py | tee profile.txt 
