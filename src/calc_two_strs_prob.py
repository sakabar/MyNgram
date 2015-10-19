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
        lst = line.split('\t')
        orig_str = lst[0]
        changed_str = lst[1]

        orig_str_bigram = my_ngram.get_ngram(orig_str.split(' '), 2)
        changed_str_bigram = my_ngram.get_ngram(changed_str.split(' '), 2)
        orig_log_prob = my_ngram.calc_sentence_log_probability(orig_str_bigram, bigram_dict, unigram_dict, vocab_num)
        changed_log_prob = my_ngram.calc_sentence_log_probability(changed_str_bigram, bigram_dict, unigram_dict, vocab_num)
        print "%s\t%f\t%s\t%f" % (orig_str, orig_log_prob, changed_str, changed_log_prob)

if __name__ == '__main__':
    main()


