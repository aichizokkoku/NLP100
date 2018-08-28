#nlp07
#テンプレートによる文生成

#今回は全く難しくなかった、おどろき
def sentence(x, y, z):
    mean = ("{}時の{}は{}".format(x, y, z))
    return mean
    
x = 12
y = "気温"
z = 22.4

answer = sentence(x, y, z)
print (answer)