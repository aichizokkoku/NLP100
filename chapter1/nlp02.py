#nlp02
#「パトカー」＋「タクシー」＝「パタトクカシーー」

str1 = "パトカー"
str2 = "タクシー"

#zip関数の使い方の確認
#print (list(zip(str1, str2)))
#[('パ', 'タ'), ('ト', 'ク'), ('カ', 'シ'), ('ー', 'ー')]
#あれ、できちゃった。
#タプル型を文字列に変換させて終了

#result = list(zip(str1, str2))
#map_list = map(str, result)
#string = "".join(str(x) for x in map_list)
#print (string)
#('パ', 'タ')('ト', 'ク')('カ', 'シ')('ー', 'ー')
#なぜか知らないけど、タプルを文字列に直せないので...

result = ""
for (a, b) in (zip(str1, str2)):
    result += a + b
print (result)

#reduce()とlambdaをもちいてforを使わずにできる方法もあるらしい