#nlp05
#n-gram

str = "I am an NLPer"

#関数作れって言われてるからdefenissionで
def n_gram(sentence, number):
    result = []
    
    #文字列の長さ分ループさせるけどここでちょっと頭をひねった
    for i in range(len(sentence)-number+1):
        result.append(sentence[i:i+number])
        
    return result


if __name__ == "__main__":
    
    result = n_gram(str, 2)
    print(result)

    splited = str.split()
    result2 = n_gram(splited, 2)
    print(result2)