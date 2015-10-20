#coding:utf-8
import sys
import my_ngram

def main():
    n = 2
    unigram_dict, n_1_gram_dict, ngram_dict = my_ngram.load_ngram_dicts(n)

    sys.stderr.write("Calculating vocab num...")
    sys.stderr.flush()
    # vocab_num = len(unigram_dict[0].keys())
    vocab_num = 2565424 #FIXME Google N-gram ベタ打ち
    sys.stderr.write("done.\n")
    sys.stderr.flush()

    # unigram_dict = my_ngram.get_stub_unigram_dict()
    # bigram_dict = my_ngram.get_stub_bigram_dict()
    # trigram_dict = my_ngram.get_stub_trigram_dict()

    for line in sys.stdin:
        line = line.rstrip()
        lst = line.split('\t')
        orig_str = lst[0]
        changed_str = lst[1]

        orig_str_ngram = my_ngram.get_ngram(orig_str.split(' '), n)
        changed_str_ngram = my_ngram.get_ngram(changed_str.split(' '), n)
        orig_log_prob = my_ngram.calc_sentence_log_probability(orig_str_ngram, ngram_dict, n_1_gram_dict, vocab_num)
        changed_log_prob = my_ngram.calc_sentence_log_probability(changed_str_ngram, ngram_dict, n_1_gram_dict, vocab_num)
        print "%s\t%f\t%s\t%f" % (orig_str, orig_log_prob, changed_str, changed_log_prob)

    sys.stderr.write("Done. Releasing Memory...\n")
    sys.stderr.flush()


if __name__ == '__main__':
    main()


