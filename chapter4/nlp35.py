#nlp35
#名詞の連接

from nlp31a import neco_lines
import MeCab

fname = "/home/ec2-user/environment/nlp100/chapter4/neko.txt"
fname_parsed = "/home/ec2-user/environment/nlp100/chapter4/neko.txt.mecab"

connectnouns = set()
#connectnouns_test = []     # 確認用の出現順リスト
lines = neco_lines()
nouns = []
seriesnouns = []
for line in lines:
    for morpheme in line:
        if morpheme['pos'] == '名詞':
            nouns.append(morpheme['surface'])
        else:
            if len(nouns) > 1:
                seriesnouns.append("".join(nouns))
            nouns = []

print (seriesnouns)