#!/bin/zsh

cat - | mecab -O wakati | python src/main.py
