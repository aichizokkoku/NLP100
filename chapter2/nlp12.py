#nlp12
#1列目をcol.txtに、2列目をcol2.txtに保存

file = "/home/ec2-user/environment/nlp100/chapter2/hightemp.txt"
colpath1 = "/home/ec2-user/environment/nlp100/chapter2/col.txt"
colpath2 = "/home/ec2-user/environment/nlp100/chapter2/col2.txt"

"""
with open(file) as data:
    for line in data:
        splited = line.split()
        with open (colpath1, mode = "w") as col1:
            col1.write(splited[0])
        with open (colpath2, mode = "w") as col2:
            col2.write(splited[1])
これでできなかった、なぜなのかはわからない
追記：パスが間違っていたことがわかりました
"""

with open(file) as data, open(colpath1, mode='w') as col, open(colpath2, mode='w') as col2:
    for line in data.readlines():
        splited = line.split()
        col.write(splited[0])
        col2.write(splited[1])

"""
UNIX command
$ cut --field=1 hightemp.txt > col.txt
高知県
埼玉県
岐阜県
山形県
山梨県
和歌山県
静岡県
山梨県
埼玉県
群馬県
群馬県
愛知県
千葉県
静岡県
愛媛県
山形県
岐阜県
群馬県
千葉県
埼玉県
大阪府
山梨県
山形県
愛知県

$ cut --field=2 hightemp.txt > col2.txt
江川崎
熊谷
多治見
山形
甲府
かつらぎ
天竜
勝沼
越谷
館林
上里見
愛西
牛久
佐久間
宇和島
酒田
美濃
前橋
茂原
鳩山
豊中
大月
鶴岡
名古屋
"""