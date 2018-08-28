#nlp09
#Typoglycemia

import random

def Typoglycemia(sentence):
    splited = sentence.split()
    result = []
    
    for word in splited:
        if len(word) <= 4:
            result.append(word)
        else:
            characterList = list(word[1:-1])
            #random.suffle()を使うとリストの中身などをランダムにシャッフルしてくれる
            random.shuffle(characterList)
            result.append(word[0] + "".join(characterList) + word[-1])
                    
    return result

sentence = input("文を入力してください: ")
result = Typoglycemia(sentence)

print(" ".join(result))
