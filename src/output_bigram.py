#coding:utf-8
import sys
import my_ngram

#bigramの対数確率を出力する
def main():
    sys.stderr.write("Loading n-gram...")
    sys.stderr.flush()
    unigram_dict = my_ngram.get_unigram_dict()
    bigram_dict = my_ngram.get_bigram_dict()
    vocab_num = len(unigram_dict.keys())
    sys.stderr.write("done.\n")
    sys.stderr.flush()

    for bigram in bigram_dict:
        log_prob = my_ngram.calc_ngram_log_probability(bigram, bigram_dict, unigram_dict, vocab_num)
        print "%s\t%f" % (bigram, log_prob)

if __name__ == '__main__':
    main()

