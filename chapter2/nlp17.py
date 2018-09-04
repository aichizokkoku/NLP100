#nlp17
#1列目の文字列の異なり

file = "/home/ec2-user/environment/nlp100/chapter2/hightemp.txt"

with open(file) as data:
    
    #set()は集合用のデータセット。リストの順番がないものと考える
    setWords = set()
    
    for line in data:
        lines = line.split()
        setWords.add(lines[0])
        
for string in setWords:
    print(string)
    
    
"""
UNIX command
$ cut --fields=1 | sort | uniq
千葉県
和歌山県
埼玉県
大阪府
山形県
山梨県
岐阜県
愛媛県
愛知県
群馬県
静岡県
高知県
"""