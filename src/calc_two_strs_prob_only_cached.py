#coding:utf-8

#coding:utf-8
import sys
import my_ngram

def main():
    n = 4
    argvs = sys.argv #argvs[0]は実行しているプログラムの名前
    argc = len(argvs)

    cached_prob_dic = {}
    if argc == 2:
        cached_file_name = argvs[1]
        with open(cached_file_name, 'r') as ngram_cache:
            for line in ngram_cache:
                line = line.rstrip()
                lst = line.split('\t')
                cached_prob_dic[lst[0]] = float(lst[1])

        if len(cached_prob_dic.keys()[0].split(' ')) != n:
            raise Exception('')


    ngram_manager = my_ngram.NgramManager(n, cached_prob_dic)

    for line in sys.stdin:
        line = line.rstrip()
        lst = line.split('\t')
        orig_str = lst[0]
        changed_str = lst[1]

        orig_str_ngram = my_ngram.get_ngram(orig_str.split(' '), n)
        changed_str_ngram = my_ngram.get_ngram(changed_str.split(' '), n)
        orig_log_prob = ngram_manager.calc_sentence_log_probability_only_cache(cached_prob_dic, orig_str_ngram)
        changed_log_prob = ngram_manager.calc_sentence_log_probability_only_cache(cached_prob_dic, changed_str_ngram)

        print "%s\t%f\t%s\t%f" % (orig_str, orig_log_prob, changed_str, changed_log_prob)



if __name__ == '__main__':
    main()
