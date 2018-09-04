#nlp16
#ファイルをN分割するNLPer

file = "/home/ec2-user/environment/nlp100/chapter2/hightemp.txt"
direct = "/home/ec2-user/environment/nlp100/chapter2/"

number = int(input("何分割しますか: "))

with open(file) as data:
    lines = data.readlines()

fileCount = int(len(lines) / number)
fileCountAdd = len(lines) % number

#print(len(line), fileCount, fileCountAdd)


"""
for output in range(1, number + 1):
    with open("{}splited{}.txt".format(direct, output), mode="w") as splitedfile:
        if output == number + 1:
            for couunt in range(fileCount + fileCountAdd):
                for lines in line[]:
                    splitedfile.write(lines)
        else:
            for count in range(fileCount):
                splitedfile.write(line)
"""

for direct, file in enumerate (range(0, fileCount, fileCountAdd), 1):
    with open("splited{}.txt".format(direct), mode="w") as splitedfile:
        for line in lines[file:file+fileCountAdd]:
            splitedfile.write(line)
            
            
#UNiXコマンドはよくわからないから省略！てへ