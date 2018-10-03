#nlp36
#単語の出現頻度

from nlp31a import neco_lines
import MeCab
from collections import Counter

fname = "/home/ec2-user/environment/nlp100/chapter4/neko.txt"
fname_parsed = "/home/ec2-user/environment/nlp100/chapter4/neko.txt.mecab"

lines = neco_lines()

#collections.Counterオブジェクトを用いればリスト内の個数をカウントして辞書型にしてくれる
word_counter = Counter()
for line in lines:
    word_counter.update([mophera['surface'] for mophera in line])

list_word = word_counter.most_common()
print(list_word)