#coding:utf-8
import sys
import gzip
import math

#FIXME
#ディレクトリはベタ打ち。
#unigramの情報を特定のファイルから読み込んで、その結果を辞書にして返す
#読み込むファイル群は固定なので、デリミタなどは指定できない。(ここでは、Google N-gramに準拠)
#辞書のキーはunigram(つまり、単語)
#辞書の値はunigramの出現回数
def get_unigram_dict():
    # ans_dict = defaultdict(lambda: 0) #存在しないキーにアクセスした場合は0を返すようにする ← これだと、だんだんキーの数が変わるので、語彙の数がおかしくなる
    ans_dict = {}
    file_name = '/raid_back/lrscp/data/ngram/original/vol1/data/1gms/1gm-0000.gz'
    for line in gzip.open(file_name, 'r'):
        line = line.rstrip()
        lst = line.split('\t')
        ans_dict[lst[0]]=int(lst[1])
    return ans_dict

#FIXME
#ディレクトリはベタ打ち。
#bigramの情報を特定のファイルから読み込んで、その結果を辞書にして返す
#読み込むファイル群は固定なので、デリミタなどは指定できない。(ここでは、Google N-gramに準拠)
#辞書のキーはbigram (単語同士の区切り文字はスペース)
#辞書の値はbigramの出現回数
def get_bigram_dict():
    # ans_dict = defaultdict(lambda: 0) #存在しないキーにアクセスした場合は0を返すようにする ← これだと、だんだんキーの数が変わるので、語彙の数がおかしくなる
    ans_dict = {}

    for i in xrange(0,9): #ここ、マジックナンバー FIXME
        file_name = '/raid_back/lrscp/data/ngram/original/vol1/data/2gms/2gm-000%d.gz' % i
        for line in gzip.open(file_name, 'r'):
            line = line.rstrip()
            lst = line.split('\t')
            ngram = lst[0]
            cnt = int(lst[1])
            ans_dict[ngram]=cnt

    return ans_dict


#文字列のリストを受けとり、ngramにしたリストを返す
#words: 文字列のリスト
#start: 文頭を表す特殊な文字列
#end: 文末を表す特殊な文字列
#delim: ngramにする際に単語同士を結合するための記号
def get_ngram(words, n, start="<S>", end="</S>", delim=' '):
    lst = [start]
    lst.extend(words)
    lst.append(end)

    return [delim.join(lst[i:i+n]) for i in xrange(0, len(lst) + 1 - n)]

#返す値は対数確率
def calc_ngram_log_probability(ngram, ngram_dict, n_1_gram_dict, vocab_num, delim=' '):
    # #n-gramの種類(nの値)が異なっていたらエラー
    # if len(ngram.split(delim)) != len(ngram_dict.keys()[0].split(delim)):
    #     raise Exception('Argument Error')

    # #依存型でNgramの型を表したい。無理だけど。
    # if len(ngram_dict.keys()[0].split(delim)) - len(n_1_gram_dict.keys()[0].split(delim)) != 1:
    #     raise Exception('Argument Error')

    n_1_gram = delim.join(ngram.split(delim)[0:-1])
    return math.log10(ngram_dict.get(ngram, 0) + 1.0) - math.log10(n_1_gram_dict.get(n_1_gram, 0) + vocab_num)
     
#返す値は対数確率
def calc_sentence_log_probability(sentence_ngram, ngram_dict, n_1_gram_dict, vocab_num, delim=' '):
    ans = 0.0
    # if len(sentence_ngram[0].split(delim)) != len(ngram_dict.keys()[0].split(delim)):
    #     raise Exception('Argument Error')

    for ngram in sentence_ngram:
        ans += calc_ngram_log_probability(ngram, ngram_dict, n_1_gram_dict, vocab_num, delim)

    return ans

def get_stub_unigram_dict():
    unigram_dict = {}
    unigram_dict["走る"] = 1
    unigram_dict["<S>"] = 1
    unigram_dict["</S>"] = 1

    return unigram_dict

def get_stub_bigram_dict(): 
    bigram_dict = {}
    bigram_dict["<S> 走る"] = 1
    bigram_dict["走る </S>"] = 1

    return bigram_dict

