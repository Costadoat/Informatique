import matplotlib.pyplot as plt

liste1=[0,0,0.1,.4,.5,.7,.8,.5,.5,.4,.5,.2,.3\
        ,0,.1,.1,0,.1,0,0,0,0,0]
liste2=[0,0,3,4,5,7,8,10,10.5,11,11.5,12,13,10\
        ,11,9,8,5,4,3,0,0,0]

plt.plot(liste1,label="Lac d'Ayous")
plt.plot(liste2,label="Pic du Midi d'Ossau")
plt.xticks(range(len(liste1)))
plt.legend()
plt.show()

labels=[i+1 for i in range(len(liste1))]
plt.bar(labels,liste2, label="Ossau")
plt.bar(labels,liste1, label="Lac d'Ayous")

plt.xticks(range(len(liste1)),labels=labels)
plt.legend()
plt.show()
