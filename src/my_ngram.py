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
    # return (ans_dict, 1)
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

    for i in xrange(0,8+1): #ここ、マジックナンバー FIXME
        file_name = '/raid_back/lrscp/data/ngram/original/vol1/data/2gms/2gm-000%d.gz' % i
        sys.stderr.write("Loading #%02d\n" % i)

        for line in gzip.open(file_name, 'r'):
            line = line.rstrip()
            lst = line.split('\t')
            ngram = lst[0]
            cnt = int(lst[1])
            ans_dict[ngram]=cnt

    return (ans_dict, 2)

#FIXME
#ディレクトリはベタ打ち。
#trigramの情報を特定のファイルから読み込んで、その結果を辞書にして返す
#読み込むファイル群は固定なので、デリミタなどは指定できない。(ここでは、Google N-gramに準拠)
#辞書のキーはtrigram (単語同士の区切り文字はスペース)
#辞書の値はtrigramの出現回数
def get_trigram_dict():
    # ans_dict = defaultdict(lambda: 0) #存在しないキーにアクセスした場合は0を返すようにする ← これだと、だんだんキーの数が変わるので、語彙の数がおかしくなる
    ans_dict = {}

    for i in xrange(0,39+1): #ここ、マジックナンバー FIXME
        file_name = '/raid_back/lrscp/data/ngram/original/vol1/data/3gms/3gm-00%02d.gz' % i
        sys.stderr.write("Loading #%02d\n" % i)
        for line in gzip.open(file_name, 'r'):
            line = line.rstrip()
            lst = line.split('\t')
            ngram = lst[0]
            cnt = int(lst[1])
            ans_dict[ngram]=cnt

    return (ans_dict, 3)

#FIXME
#ディレクトリはベタ打ち。
#fourgramの情報を特定のファイルから読み込んで、その結果を辞書にして返す
#読み込むファイル群は固定なので、デリミタなどは指定できない。(ここでは、Google N-gramに準拠)
#辞書のキーはfourgram (単語同士の区切り文字はスペース)
#辞書の値はfourgramの出現回数
def get_fourgram_dict():
    ans_dict = {}

    for i in xrange(0,70+1): #ここ、マジックナンバー FIXME
        file_name = '/raid_back/lrscp/data/ngram/original/vol1/data/4gms/4gm-00%02d.gz' % i if i <= 24  else '/raid_back/lrscp/data/ngram/original/vol2/data/4gms/4gm-00%02d.gz' % i
        sys.stderr.write("Loading #%02d\n" % i)
        for line in gzip.open(file_name, 'r'):
            line = line.rstrip()
            lst = line.split('\t')
            ngram = lst[0]
            cnt = int(lst[1])
            ans_dict[ngram]=cnt

    return (ans_dict, 4)


#文字列のリストを受けとり、ngramにしたリストとnの値のタプルを返す
#words: 文字列のリスト
#start: 文頭を表す特殊な文字列
#end: 文末を表す特殊な文字列
#delim: ngramにする際に単語同士を結合するための記号
def get_ngram(words, n, start="<S>", end="</S>", delim=' '):
    lst = [start]
    lst.extend(words)
    lst.append(end)

    return ([delim.join(lst[i:i+n]) for i in xrange(0, len(lst) + 1 - n)], n)

def load_ngram_dicts(n):
    sys.stderr.write("Loading unigram...")
    sys.stderr.flush()
    unigram_dict = get_unigram_dict()
    sys.stderr.write("done.\n")
    sys.stderr.flush()

    if n == 2:
        sys.stderr.write("Loading bigram...")
        sys.stderr.flush()
        ngram_dict = get_bigram_dict()
        sys.stderr.write("done.\n")
        sys.stderr.flush()
        return (unigram_dict, unigram_dict, ngram_dict)

    elif n == 3:
        sys.stderr.write("Loading bigram...")
        sys.stderr.flush()
        n_1_gram_dict = get_bigram_dict()
        sys.stderr.write("done.\n")
        sys.stderr.flush()

        sys.stderr.write("Loading trigram...")
        sys.stderr.flush()
        ngram_dict = get_trigram_dict()
        sys.stderr.write("done.\n")
        sys.stderr.flush()
        return (unigram_dict, n_1_gram_dict, ngram_dict)

    elif n == 4:
        sys.stderr.write("Loading trigram...")
        sys.stderr.flush()
        n_1_gram_dict = get_trigram_dict()
        sys.stderr.write("done.\n")
        sys.stderr.flush()

        sys.stderr.write("Loading fourgram...")
        sys.stderr.flush()
        ngram_dict = get_fourgram_dict()
        sys.stderr.write("done.\n")
        sys.stderr.flush()
        return (unigram_dict, n_1_gram_dict, ngram_dict)

class NgramManager:
    def __init__(self, n):
        self.n = n
        sys.stderr.write("Loading unigram...")
        sys.stderr.flush()
        self.unigram_dict = get_unigram_dict()
        self.vocab_num = 2565424 #FIXME Google N-gram ベタ打ち
        sys.stderr.write("done.\n")
        sys.stderr.flush()

        self.ngram_dict = {}
        self.ngram_loaded_flags = {}
        if n == 2:
            self.n_1_gram_dict = self.unigram_dict
            self.n_1_gram_loaded_flags = {}
            self.n_1_gram_loaded_flags[0] = 1
        else:
            self.n_1_gram_dict = {}
            self.n_1_gram_loaded_flags = {}

    def search_ngram_ind(self, key, ind_lst):
        #ind_lst[0] <= key < ind_lst[1] → ans_ind = 0
        for i in xrange(0, len(ind_lst)-1):
            if key < ind_lst[i+1]:
                return i

        return len(ind_lst)-1

    #ngram_dictとn_1_gram_dictを利用して対数確率を計算
    def calc_sentence_log_probability(self, sentence_ngram, delim=' '):
        ans = 0.0
        for ngram in sentence_ngram[0]:
            ans += self.calc_ngram_log_probability(ngram, delim)

        return ans


    #返す値は対数確率
    def calc_ngram_log_probability(self, ngram, delim=' '):
        n_1_gram_key = delim.join(ngram.split(delim)[0:-1])

        ngram_ind = -1
        if self.n == 2:
            ind_lst = ["! </S>", "☆ 青のり", "たくさん 臨時", "も 追い返せ", "デバイス CD", "伯 朗", "引き続き 指摘", "発 叩き込も", "高かろ ー"]
            ngram_ind = self.search_ngram_ind(ngram, ind_lst)
        
        elif self.n == 3:
            ind_lst = ["!! ありがとう ござい", "2 ) はっぴ", "<S> そのまま 轢か", "<S> 日本 赤ちゃん", "TOP | 気", "、 そんな 憂鬱", "「 アール・デコ 様式", "いっ た 戦績", "が おこがましい です", "さ れ 歩道橋", "それなり に 着込ん", "つか 、 劇", "と かなり 早め", "ながら クリア で", "による 歌 .", "の 違法 整備", "ぴこぞう コーナー >", "もしかして 「 私", "を 教える 係り", "キチ の 誕生", "ストレート 用 コーム", "ハービス ENT で", "マジ あり ませ", "・ ・ 定峰", "交わる べき なり", "個別 的 です", "割合 ( 好み", "呼びかけ て 頂く", "天皇 が 参列", "左腕 が 復活", "情報 ( 料金", "新潟 の フィッシング", "村 に 生きる", "法 ; 港", "生前 に 読ん", "程 良く 煮え", "脇 元 嘉", "設け たり と", "過程 で 社内", "頸城 郡 松代"]
            ngram_ind = self.search_ngram_ind(ngram, ind_lst)
        elif self.n == 4:
            ind_lst = ["!! こちら は この", "- とにかく 綺麗 です", "4 形式 の 圧縮", "<S> ■ 注目 システム", "<S> ちょっと 天 板", "<S> ナポリ 経由 で", "<S> 問題 教師 は", "<S> 理系 大学生 学園", "CD じゃ ない じゃん", "↓ 以下 、 コメントレス", "、 なんとなく 何 回", "、 又は あ つて", "、 肝 は 「", "」 し て ←", "あん たら 何 しとる", "おおむね 同じ 期間 で", "が 20 年 先", "が 萱野 稔 人", "この 馬 が 勝っ", "し 以下 の 事", "その 味 は 多く", "た 猫 長靴 を", "ちょうど 良い 焼き 具合", "て 吸っ て 下さい", "で 嬉しい な (*^^*)", "と ヒャクニチソウ の 花", "どうこう 口出し する こと", "なく て 「 エイ", "に は 離れ ませ", "におい 、 廃 熱", "の オキニイリ は 、", "の 名前 や レース", "の 申請 日 と", "は 1 歩 譲る", "は 塩素 で バツ", "へ 本気 で 行き", "も あまり 考え すぎ", "や 砂 と の", "を おこす と 言う", "ん だ 大丈夫 じゃ", "ガム を 減らし て", "シーズン / お ぎやはぎ", "データベース が あり 、", "フランス と の 類似", "モットー に がんばっ ちゃ", "・ 三河 産地 フォーラム", "世界 で 23 億", "人間らしい 猫 です 。", "何となく 理解 出来 まし", "全国 各地 で 急増", "剣道 時代 5 月", "只 、 人 の", "国民 を 応援 する", "大臣 が 「 農業", "寝泊まり し た 時", "幼稚園 の お子さん だ", "性 ・ ソフト タイプ", "授業 で 会っ て", "日 ギフト で も", "月 ~ 金 ):", "様 な 演技 に", "活動 し て られ", "狩り は 嫌い な", "皆 に 無視 さ", "積み木 を 利用 し", "編成 の 極めて 珍しい", "英 史 、 寿司", "計画 図 Iga を", "身近 に 大阪 を", "酢 砂糖 ゴマ油 </S>", "音 を 放つ 事"]
            ngram_ind = self.search_ngram_ind(ngram, ind_lst)
        else:
            raise Exception('No implimentation')

        #既に読み込んだngramか?
        if ngram_ind in self.ngram_loaded_flags:
            pass
        else:
            if self.n == 2:
                self.ngram_dict = self.load_ngram_lazily(self.ngram_dict, ngram_ind, self.n)
                self.ngram_loaded_flags[ngram_ind] = 1
            elif self.n == 3:
                self.ngram_dict = self.load_ngram_lazily(self.ngram_dict, ngram_ind, self.n)
                self.ngram_loaded_flags[ngram_ind] = 1
            elif self.n == 4:
                self.ngram_dict = self.load_ngram_lazily(self.ngram_dict, ngram_ind, self.n)
                self.ngram_loaded_flags[ngram_ind] = 1
            else:
                raise Exception('No implimentation')

        n_1_gram_ind = -1
        if self.n == 2:
            pass

        elif self.n == 3:
            ind_lst = ["! </S>", "☆ 青のり", "たくさん 臨時", "も 追い返せ", "デバイス CD", "伯 朗", "引き続き 指摘", "発 叩き込も", "高かろ ー"]
            n_1_gram_ind = self.search_ngram_ind(n_1_gram_key, ind_lst)
        elif self.n == 4:
            ind_lst = ["!! ありがとう ござい", "2 ) はっぴ", "<S> そのまま 轢か", "<S> 日本 赤ちゃん", "TOP | 気", "、 そんな 憂鬱", "「 アール・デコ 様式", "いっ た 戦績", "が おこがましい です", "さ れ 歩道橋", "それなり に 着込ん", "つか 、 劇", "と かなり 早め", "ながら クリア で", "による 歌 .", "の 違法 整備", "ぴこぞう コーナー >", "もしかして 「 私", "を 教える 係り", "キチ の 誕生", "ストレート 用 コーム", "ハービス ENT で", "マジ あり ませ", "・ ・ 定峰", "交わる べき なり", "個別 的 です", "割合 ( 好み", "呼びかけ て 頂く", "天皇 が 参列", "左腕 が 復活", "情報 ( 料金", "新潟 の フィッシング", "村 に 生きる", "法 ; 港", "生前 に 読ん", "程 良く 煮え", "脇 元 嘉", "設け たり と", "過程 で 社内", "頸城 郡 松代"]
            n_1_gram_ind = self.search_ngram_ind(n_1_gram_key, ind_lst)
        else:
            raise Exception('No implimentation')

        #既に読み込んだ(n-1)gramか?
        if n_1_gram_ind in self.n_1_gram_loaded_flags:
            pass
        else:
            if self.n == 2:
                pass #unigramは読み込み済み
            elif self.n == 3:
                self.n_1_gram_dict = self.load_ngram_lazily(self.n_1_gram_dict, n_1_gram_ind, self.n-1)
                self.n_1_gram_loaded_flags[n_1_gram_ind] = 1
            elif self.n == 4:
                self.n_1_gram_dict = self.load_ngram_lazily(self.n_1_gram_dict, n_1_gram_ind, self.n-1)
                self.n_1_gram_loaded_flags[n_1_gram_ind] = 1
            else:
                raise Exception('No implimentation')

        log_nume = math.log10(self.ngram_dict.get(ngram, 0) + 1.0)
        log_demo = math.log10(self.n_1_gram_dict.get(n_1_gram_key, 0) + self.vocab_num)
        return log_nume - log_demo

    def load_ngram_lazily(self, dic, ind, n):
        file_name = ''

        if n == 2:
            file_name = '/raid_back/lrscp/data/ngram/original/vol1/data/2gms/2gm-000%d.gz' % ind
            sys.stderr.write("**Loading 2gram #%02d..." % ind)
            sys.stderr.flush()
        elif n == 3:
            file_name = '/raid_back/lrscp/data/ngram/original/vol1/data/3gms/3gm-00%02d.gz' % ind
            sys.stderr.write("***Loading 3gram #%02d..." % ind)
            sys.stderr.flush()
        elif n == 4:
            file_name = '/raid_back/lrscp/data/ngram/original/vol1/data/4gms/4gm-00%02d.gz' % ind if ind <= 24  else '/raid_back/lrscp/data/ngram/original/vol2/data/4gms/4gm-00%02d.gz' % ind
            sys.stderr.write("****Loading 4gram #%02d..." % ind)
            sys.stderr.flush()
        else:
            Exception('Not implimented')

        for line in gzip.open(file_name, 'r'):
            line = line.rstrip()
            lst = line.split('\t')
            ngram = lst[0]
            cnt = int(lst[1])
            dic[ngram]=cnt

        sys.stderr.write("done\n")
        sys.stderr.flush()

        return dic
