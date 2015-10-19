#coding:utf-8
import sys
import my_ngram

def main():
    sys.stderr.write("Loading n-gram...")
    sys.stderr.flush()
    unigram_dict = my_ngram.get_unigram_dict()
    bigram_dict = my_ngram.get_bigram_dict()
    # unigram_dict = my_ngram.get_stub_unigram_dict()
    # bigram_dict = my_ngram.get_stub_bigram_dict()
    vocab_num = len(unigram_dict.keys())
    sys.stderr.write("done.\n")
    sys.stderr.flush()

    for line in sys.stdin:
        line = line.rstrip()
        words = line.split(' ')
        sentence_ngram = my_ngram.get_ngram(words, 2)
        log_prob = my_ngram.calc_sentence_log_probability(sentence_ngram, bigram_dict, unigram_dict, vocab_num)
        print "%s\t%f" % (line, log_prob)

if __name__ == '__main__':
    main()

