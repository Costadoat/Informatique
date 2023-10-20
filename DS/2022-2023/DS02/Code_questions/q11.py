# Question 11:
def get_five_more_close_v2(hub,exclude):
    d=0
    five_more_close=[]
    while len(five_more_close)<5:
        d+=0.0001
        for compteur in compteurs:
            if distance(compteur[2],hub[2])<d and compteur not in five_more_close and compteur not in exclude:
                five_more_close.append(compteur)
    return five_more_close

parcours=[dorian]
for i in range(10):
    parcours.append(get_max(get_five_more_close_v2(parcours[i],parcours)))
print(parcours)

