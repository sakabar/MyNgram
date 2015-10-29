#coding:utf-8

import sys
import my_ngram

def main():
    n = 4#FIXME ベタ打ち
    # ngram_manager = my_ngram.NgramManager(n) 

    for line in sys.stdin:
        line = line.rstrip()
        
        ngram_lst , _ = my_ngram.get_ngram(line.split(' '), n)
        for ngram in ngram_lst:
            print ngram

if __name__ == '__main__':
    main()
    
