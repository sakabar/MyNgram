#coding:utf-8
import sys
import my_ngram

def main():
    n = 3
    argvs = sys.argv #argvs[0]は実行しているプログラムの名前
    argc = len(argvs)

    ngram_cache_file_name = str(n) + '-gram_prob.cache'

    cached_prob_dic = {}
    #もしキャッシュファイルを指定していたら、読み込み
    if argc == 2:
        prev_cached_file_name = argvs[1]
        with open(prev_cached_file_name, 'r') as ngram_cache:
            for line in ngram_cache:
                line = line.rstrip()
                lst = line.split('\t')
                cached_prob_dic[lst[0]] = float(lst[1])

        if len(cached_prob_dic.keys()[0].split(' ')) != n:
            raise Exception('')


    ngram_manager = my_ngram.NgramManager(n, cached_prob_dic)

    ngram_keys = set() #入力文中に現れたn-gram(スペースを含む文字列)
    with open(ngram_cache_file_name+".new", 'w') as ngram_cache:
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

            #使ったn-gramを書き出しておく
            ngram_keys = ngram_keys.union(set(orig_str_ngram[0]))
            ngram_keys = ngram_keys.union(set(changed_str_ngram[0]))

        #使ったn-gramをキャッシュとして出力
        for ngram_key in ngram_keys:
            p = ngram_manager.calc_ngram_log_probability(ngram_key)
            out = "%s\t%f\n" % (ngram_key, p)
            ngram_cache.write(out)

    sys.stdout.flush()
    sys.stderr.write("Done. Releasing Memory...\n")
    sys.stderr.flush()

if __name__ == '__main__':
    main()
