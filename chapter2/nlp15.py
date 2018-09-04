#nlp15
#末尾のN行を出力

file = "/home/ec2-user/environment/nlp100/chapter2/hightemp.txt"

number = int(input("末尾の何行をとりだしますか: "))

with open(file) as data:
    line = data.readlines()
    
    for output in line[-number:]:
        print(output.rstrip())
        


"""
UNIC command
$ tail --line="数字" hightemp.txt
"""