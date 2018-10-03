#nlp31
#動詞

#from main import neko_lines
import MeCab

file = "/home/ec2-user/environment/nlp100/chapter4/neko_test.txt"
AnedFile = "/home/ec2-user/environment/nlp100/chapter4/neko_test.txt.mecab"

"""
def neko_verb():
    with open(AnedFile) as datafile:
        morphemes = []
        for line in datafile:
            col = line.split("\t")
            col_comp = col[1].split(",")

            morpheme = {
                "surface" : col[0],
                "base" : col_comp[6],
                "pos" : col_comp[0],
                "pos1" : col_comp[1]
            }
            
            if morpheme["pos"] == "動詞":
                morphemes.append(morpheme["surface"])
        print(set(morphemes))
        return morphemes


if __name__ == "__main__":
    #sentence = neko_verb()
    #print(sentence)
    neko_verb()
"""

with open(AnedFile) as datafile:
    morphemes = []
    for line in datafile:
        col = line.split("\t")
        if(len(col) < 2):
            raise StopIteration
        col_comp = col[1].split(",")
        #print(col)
        #print(col_comp)

        morpheme = {
            "surface" : col[0],
            "base" : col_comp[6],
            "pos" : col_comp[0],
            "pos1" : col_comp[1]
        }
        pos = morpheme["surface"]
            
        if morpheme["pos"] == "動詞":
            morphemes.append(pos)
print(morphemes)
print(set(morphemes))