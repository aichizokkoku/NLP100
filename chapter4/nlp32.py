#nlp32
#動詞の原形

from nlp31a import neco_lines
import MeCab

fname = "/home/ec2-user/environment/nlp100/chapter4/neko.txt"
fname_parsed = "/home/ec2-user/environment/nlp100/chapter4/neko.txt.mecab"

verbs = set()
verbs_test = []     # 確認用の出現順リスト
lines = neco_lines()
for line in lines:
    for morpheme in line:
        if morpheme['pos'] == '動詞':
            verbs.add(morpheme['base'])
            verbs_test.append(morpheme['base'])      # 確認用の出現順リストにも追加

# 確認しやすいようverbs_testを使って出現順にソートして表示
print(sorted(verbs, key=verbs_test.index))