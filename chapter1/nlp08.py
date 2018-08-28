#nlp08
#暗号文

def cipher(sentence):
    result = ""
    
    for char in sentence:
        if char.islower():
            #文字コードはord()で求めることができる
            result += chr(219 - ord(char))
        else:
            result += char
            
    return result
           
            
sentence = input("文を入力してください: ")

result = cipher(sentence)
result2 = cipher(result)

print ("暗号化されました: {}".format(result))
print ("復元化しました: {}".format(result2))

#本当にしっかり暗号化して復元化できているかチェックするよ
if sentence == result2:
    print("成功しています")
else:
    print("失敗しています")