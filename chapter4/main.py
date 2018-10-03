#nlp30
#形態素解析結果の読み込み

import MeCab
file = "/home/ec2-user/environment/nlp100/chapter4/neko.txt"
AnedFile = "/home/ec2-user/environment/nlp100/chapter4/neko.txt.mecab"


def neko_ana():
    with open(file) as data, open(AnedFile, mode="w") as outfile:
        mecab = MeCab.Tagger()
        outfile.write(mecab.parse(data.read()))
        
def neko_lines():
    with open(AnedFile) as datafile:
        morphemes = []
        for line in datafile:
            col = line.split("\t")
            col_comp = col[1].split(",")
            #print ("{}{}".format(col, col_comp))
            
            morpheme = {
                "surface" : col[0],
                "base" : col_comp[6],
                "pos" : col_comp[0],
                "pos1" : col_comp[1]
            }
            
            morphemes.append(morpheme)
            
            if col_comp[1] == "句点":
                yield morphemes
                morphemes = []
        
if __name__ == "__main__":
    #neko_ana()
    sentence = neko_lines()
    for line in sentence:
        print (line)
    