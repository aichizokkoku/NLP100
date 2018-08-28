#nlp20
#行数のカウント

file = "hightemp.txt"

with open(file) as text:
    for line in text.readlines():
        print(line)
        