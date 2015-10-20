#coding:utf-8
import sys
import my_ngram

def main():
    n = 2
    ngram_manager = my_ngram.NgramManager(2)

    for line in sys.stdin:
        line = line.rstrip()
        lst = line.split('\t')
        orig_str = lst[0]
        changed_str = lst[1]

        orig_str_ngram = my_ngram.get_ngram(orig_str.split(' '), n)
        changed_str_ngram = my_ngram.get_ngram(changed_str.split(' '), n)
        orig_log_prob = ngram_manager.calc_sentence_log_probability(orig_str_ngram)
        changed_log_prob = ngram_manager.calc_sentence_log_probability(changed_str_ngram)
        print "%s\t%f\t%s\t%f" % (orig_str, orig_log_prob, changed_str, changed_log_prob)

    sys.stderr.write("Done. Releasing Memory...\n")
    sys.stderr.flush()



if __name__ == '__main__':
    main()


