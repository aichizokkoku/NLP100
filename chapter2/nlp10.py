#nlp10
#行数のカウント

file = "/home/ec2-user/environment/nlp100/chapter2/hightemp.txt"
count = 0

with open(file) as text:
    for line in text.readlines():
        count += 1
        
print (count)



"""
UNIX command
$ wc --line hightemp.txt
24
"""