#!/bin/zsh
echo "歩いて帰ろう。" | mecab -O wakati | python -m cProfile -s time src/main.py

#| tee profile.txt
