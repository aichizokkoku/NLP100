#nlp06
#集合

from nlp05 import n_gram

str1 = "paraparaparadise"
str2 = "paragraph"

setx = set(n_gram(str1, 2))
print("X: {}".format(setx))
sety = set(n_gram(str2, 2))
print("Y: {}".format(sety))

set_union = setx | sety
#or setx.union(sety)
print("和集合は: {}".format(set_union))
set_intersection = setx & sety
#or setx.intersection(sety)
print("積集合は: {}".format(set_intersection))
set_difference = setx - sety
#or setx.difference(sety)
print("差集合は: {}".format(set_difference))

#"se"が入っているかを確認
print("\"se\"が入っているか: {}".format("se" in setx))
print("\"se\"が入っているか: {}".format("se" in sety))