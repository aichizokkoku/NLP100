#nlp34
#「AのB」

from nlp31a import neco_lines
import MeCab

fname = "/home/ec2-user/environment/nlp100/chapter4/neko.txt"
fname_parsed = "/home/ec2-user/environment/nlp100/chapter4/neko.txt.mecab"

connectnouns = set()
#connectnouns_test = []     # 確認用の出現順リスト
lines = neco_lines()
for line in lines:
    for i in range(1, len(line) - 1):
        if line[i]['surface'] == 'の':
            if line[i - 1]['pos'] == '名詞':
                if line[i + 1]['pos'] == '名詞':
                    phrase = line[i - 1]['surface'] + line[i]['surface'] + line[i + 1]['surface']
                    connectnouns.add(phrase)
                     #connectnouns_test.append(line[i]['surface'])      # 確認用の出現順リストにも追加

print (connectnouns)