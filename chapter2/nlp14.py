#nlp14
#先頭からN行を出力

file = "/home/ec2-user/environment/nlp100/chapter2/hightemp.txt"

number = input("先頭の何行を取り出しますか: ")
count = 1

with open(file) as data:
    for line in data.readlines():
        if count <= int(number):
            print(line.rstrip())
            count += 1
        else:
            break

"""
UNIX command
$ head --line="数字" hightemp.txt
"""