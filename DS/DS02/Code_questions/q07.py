# Question 7:
def get_five_more_close(hub):
    d=0
    five_more_close=[]
    while len(five_more_close)<5:
        d+=0.0001
        for compteur in compteurs:
            if distance(compteur[2],hub[2])<d and compteur not in five_more_close and compteur!=hub:
                five_more_close.append(compteur)
    return five_more_close

print(get_five_more_close(dorian))
    
