#mecabのテスト


import MeCab

m = MeCab.Tagger ("-Ochasen")
print (m.parse ("おはようございます"))


