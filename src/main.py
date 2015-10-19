import sys
import my_ngram

def main():
    sys.stderr.write("Loading n-gram...")
    sys.stderr.flush()
    bigram_dict = my_ngram.get_bigram_dict()
    sys.stderr.write("done.\n")
    sys.stderr.flush()

    for line in sys.stdin:
        line = line.rstrip()
        words = line.split(' ')
        ngrams = my_ngram.get_ngram(words, 2)
        for ngram in ngrams:
            print "%s and %d" % (ngram, bigram_dict[ngram])
        print "EOS"


if __name__ == '__main__':
    main()

