#nlp03
#円周率

str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

#まずはsplit()を使ってスペースで分けてみる
splited = str.split()
#print (splited)
#['Now', 'I', 'need', 'a', 'drink,', 'alcoholic', 'of', 'course,', 'after', 'the', 'heavy', 'lectures', 'involving', 'quantum', 'mechanics.']
#しっかり分けることができてる

#print(len(splited[0]))
#これで文字数をカウントできた

"""
result = []
count = 0
for word in splited:
    #print(len(splited[count]))
    result.append(len(splited[count]))
    count += 1
print (result)

[3, 1, 4, 1, 6, 9, 2, 7, 5, 3, 5, 8, 9, 7, 10]
これで一応文字のすべてのカウントはできたのだけれども
最後のピリオドもカウントされてしまっている
のでなおす
"""

result = []
for word in splited:
    count = 0
    for char in word:
        if char.isalpha():
            count += 1
    result.append(count)
print (result)