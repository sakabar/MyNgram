#coding:utf-8
import sys
import math

def main():
    vocab_num = 2565424 #FIXME Google N-gram ベタ打ち
    input_fourgram_dic = {}

    #後々使うことになる4-gramをキャッシュする目的
    cache='fourgram_keys.txt'
    with open(cache, 'r') as input_ngram:
        for line in input_ngram:
            line = line.rstrip()
            input_fourgram_dic[line] = 1
        
    trigram_key = () #今見ている4gramの、先頭3gram
    cnt_dic = [] #今見ている4garmをkeyとして、回数を返す
    sum_cnt = 0 #今見ている4gram群の回数の和
    for line in sys.stdin:
        line = line.rstrip()
        lst = line.split('\t')
        key = lst[0]
        cnt = int(lst[1])
        tri = tuple(key.split(' ')[0:3])

        #もし前の3語が異なるngramになったら、前までのぶんを計算して出力する
        if trigram_key != tri:
            if trigram_key != ():
                for k in cnt_dic:
                    v = cnt_dic[k]
                    log_p = math.log10(v + 1.0) - math.log10(sum_cnt +  vocab_num)
                    output_str = "%s\t%f" % (k, log_p)
                    print output_str
                    # sys.stdout.write(output_str)

                    #後で使うngramは出力しておく
                    if k in input_fourgram_dic:
                        # with open('fourgram_log_p.txt', 'a') as f:
                        sys.stderr.write(output_str + '\n')

                # sys.stdout.flush()


            sum_cnt = 0
            cnt_dic = {}
            trigram_key = tuple(key.split(' ')[0:3])

        cnt_dic[key] = cnt
        sum_cnt += cnt

if __name__ == '__main__':
    main()
