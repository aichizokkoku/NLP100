#nlp04
#元素記号

str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
numbers = (1, 5, 6, 7, 8, 9, 15, 16, 19)

#nlp03と同じやり方
splited = str.split()


#文字の抜き出しについて確認
#word = splited[0]
#print (word[0:1])
#H

"""
#emulate()を使うことによって通し番号を振れる
for (i, word) in enumerate(splited, 1):
    if i in numbers:
        print (i, word[0:1])
    else:
        print (i, word[0:2])
        
1 H
2 He
3 Li
4 Be
5 B
6 C
7 N
8 O
9 F
10 Ne
11 Na
12 Mi
13 Al
14 Si
15 P
16 S
17 Cl
18 Ar
19 K

あとはこれを辞書型に直すだけ
"""

data = {}

for (i, word) in enumerate(splited, 1):
    if i in numbers:
        data[word[0:1]] = i
    else:
        data[word[0:2]] = i
        
print (data)