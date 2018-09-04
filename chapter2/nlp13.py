#nlp13
#col.txtとcol2.txtをマージ

colpath1 = "/home/ec2-user/environment/nlp100/chapter2/col.txt"
colpath2 = "/home/ec2-user/environment/nlp100/chapter2/col2.txt"
margepath = "/home/ec2-user/environment/nlp100/chapter2/marge.txt"

with open(colpath1) as col1, open(colpath2) as col2, open(margepath, mode="w") as marge:
    for col1data, col2data in zip(col1,col2):
        #print(col1data + col2data, end = "")
        #print("\t", end = "")
        #print(col2data, end = "")
        #marge.write("{}\t{}".format(col1data, col2data))
        #どうしてもプリントする際に改行されてしまう
        #なのでrstrip()をつかって空白を消してしまおうと考える
        print("{}\t{}".format(col1data.rstrip(), col2data.rstrip()))
        #なんかファイルに書き込むときは最後に改行が必要みたい・・・
        marge.write("{}\t{}\n".format(col1data.rstrip(), col2data.rstrip()))
        
        
        
"""        
UNIX command
$ paste col.txt col2.txt > marge.txt
"""