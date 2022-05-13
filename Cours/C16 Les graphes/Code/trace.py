import imageio
import matplotlib.pyplot as plt
import networkx as nx
import os


data={'A':{0:'B',1:'D'},'B':{0:'A',1:'C'},'C':{0:'B',1:'D'},'D':{0:'A',1:'C',2:'G'},'E':{0:'I',1:'H'},'G':{0:'D',1:'H',2:'I'},'H':{0:'G',1:'E'},'I':{0:'G',1:'E'}}


def PL(gr,s):
    i=0
    j=0
    global filenames
    files=[s]
    noeuds_decouverts=[s]
    nodePos={}
    while len(files)!=0:
#    while len(noeuds_decouverts)<20:
        noeud_courant=files[0]
        files=files[1:]
        for voisin in gr[noeud_courant].values():
            nx.add_path(G, [noeud_courant, voisin])
            if voisin not in noeuds_decouverts:
                noeuds_decouverts.append(voisin)
                files.append(voisin)
    pos=nx.spring_layout(G)
    for i in range(len(noeuds_decouverts)):
        out=noeuds_decouverts[i:]
        H = nx.restricted_view(G, out, [])
        nx.draw_networkx(H,pos=pos)
        filename = f'{i}.png'
        i+=1
        filenames.append(filename)
        plt.savefig(filename)
        plt.close()
    nx.draw_networkx(G,pos=pos)
    filename = f'{i}.png'
    filenames.append(filename)
    plt.savefig(filename)
    plt.savefig('largeur.png')
    plt.close()
    return(noeuds_decouverts)


def PP(gr,s):
    i=0
    global filenames
    piles=[s]
    noeuds_decouverts=[]
    nodePos={}
    while len(piles)!=0:
#   while len(noeuds_decouverts)<20:
        noeud_courant=piles[-1]
        piles=piles[:-1]
        for voisin in gr[str(noeud_courant)].values():
            nx.add_path(G, [noeud_courant, voisin])
            if (voisin not in noeuds_decouverts) and (voisin not in piles):
                piles.append(voisin)
        noeuds_decouverts.append(noeud_courant)

    pos=nx.spring_layout(G)
    for i in range(len(noeuds_decouverts)):
        out=noeuds_decouverts[i:]
        H = nx.restricted_view(G, out, [])
        nx.draw_networkx(H,pos=pos)
        filename = f'{i}.png'
        i+=1
        filenames.append(filename)
        plt.savefig(filename)
        plt.close()
    nx.draw_networkx(G,pos=pos)
    filename = f'{i}.png'
    filenames.append(filename)
    plt.savefig(filename)
    plt.savefig('profondeur.png')
    plt.close()
    return(noeuds_decouverts)



G = nx.DiGraph()
filenames = []
result=PL(data,'A')

with imageio.get_writer('mygif_largeur.gif', mode='I') as writer:
    for filename in filenames:
        for i in range(10):
            image = imageio.imread(filename)
            writer.append_data(image)

# Remove files
for filename in set(filenames):
    os.remove(filename)

G = nx.DiGraph()
filenames = []
result=PP(data,'A')

with imageio.get_writer('mygif_profondeur.gif', mode='I') as writer:
    for filename in filenames:
        for i in range(10):
            image = imageio.imread(filename)
            writer.append_data(image)

        
# Remove files
for filename in set(filenames):
    os.remove(filename)
    
