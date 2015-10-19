#!/bin/zsh

cat - | mecab -O wakati | python src/output_prob.py
