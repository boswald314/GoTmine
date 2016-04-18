import networkx as nx
import matplotlib.pyplot as plt

DISTANCE = 15

charFile = open("characters.txt",'r')
characters = charFile.read().split('\n')
charFile.close()

book = open("1-AGameofThrones/gameofthrones.txt")
words = book.read().strip().split()
book.close()

G = nx.Graph()
for person in characters:
	G.add_node(person)


for wordnum,word in enumerate(words):
	if word in G.nodes():
		#print words[wordnum:wordnum+DISTANCE]
		for newWord in words[wordnum+1:wordnum+DISTANCE]:
			if newWord in G.nodes():
				#print words[wordnum:wordnum+DISTANCE]
				if (word,newWord) not in G.edges():
					G.add_edge(word,newWord, weight=1)
				else:
					G[word][newWord]['weight'] += 1



outdeg = G.degree(G.nodes())
to_remove = [n for n in outdeg if outdeg[n]==0]

G.remove_nodes_from(to_remove)


nx.draw(G)
nx.draw_networkx_labels(G,pos=nx.spring_layout(G))
plt.show()
