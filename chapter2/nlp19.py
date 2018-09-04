#nlp19
#各行の1コラム目の文字列の出現頻度を求め、出現頻度の高い順に並べる

from collections import Counter

file = "/home/ec2-user/environment/nlp100/chapter2/hightemp.txt"
result =[]

with open(file) as data:
    for line in data:
        result.append(line[0:3])

newList = Counter(result)
#print(newList)

for count in newList.most_common():
    print(count[0], count[1])

#すべて自分の力でかけた！やった

"""
UNIX command
$ cut --fields=1 hightemp.txt | sort| uniq --count | sort -r
      3 群馬県
      3 山梨県
      3 山形県
      3 埼玉県
      2 静岡県
      2 愛知県
      2 岐阜県
      2 千葉県
      1 高知県
      1 愛媛県
      1 大阪府
      1 和歌山県
"""