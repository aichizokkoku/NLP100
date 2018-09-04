#nlp11
#タブをスペースに変換

file = "/home/ec2-user/environment/nlp100/chapter2/hightemp.txt"

#文字列を置換するときにはreplace()を使用するらしい
with open(file) as data:
    for character in data.readlines():
        print (character.replace("\t"," "), end = "")
        
#すべての行を順番に読み込んでそこからタブを空欄に変更する
#タブの表現方法は\t
#printする際に開業してほしくないので最後にend = ""を追加する


"""
UNIX command
$ sed "s/\t/ /g" hightemp.txt
#sedのsコマンドの使い方
sed "s/置換選択/置換するもの/g(すべて適用）"　ファイル名
"""