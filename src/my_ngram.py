#coding:utf-8
import sys
import gzip
from collections import defaultdict

#FIXME
#ディレクトリはベタ打ち。
#unigramの情報を特定のファイルから読み込んで、その結果を辞書にして返す
#読み込むファイル群は固定なので、デリミタなどは指定できない。(ここでは、Google N-gramに準拠)
#辞書のキーはunigram(つまり、単語)
#辞書の値はunigramの出現回数
def get_unigram_dict():
    ans_dict = defaultdict(lambda: 0) #存在しないキーにアクセスした場合は0を返すようにする
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
    ans_dict = defaultdict(lambda: 0) #存在しないキーにアクセスした場合は0を返すようにする

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
