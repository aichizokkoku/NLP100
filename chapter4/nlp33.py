#nlp33
#サ変名詞

from nlp31a import neco_lines
import MeCab

fname = "/home/ec2-user/environment/nlp100/chapter4/neko.txt"
fname_parsed = "/home/ec2-user/environment/nlp100/chapter4/neko.txt.mecab"

nouns = set()
nouns_test = []     # 確認用の出現順リスト
lines = neco_lines()
for line in lines:
    for morpheme in line:
        if morpheme['pos'] == '名詞':
            if morpheme['pos1'] == 'サ変接続':
                nouns.add(morpheme['surface'])
                nouns_test.append(morpheme['surface'])      # 確認用の出現順リストにも追加

# 確認しやすいようverbs_testを使って出現順にソートして表示
print(sorted(nouns, key=nouns_test.index))