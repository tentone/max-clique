from itertools import combinations

# Searches for all cliques inside of the graph.
#
# Uses a naive approach doing all combinations of vertexes and checking if each group has connections to each others.
def findCliques(graph):
	combs = combinations(graph.vertices, 3)
	combs = list(combs)

	cliques = []

	for c in combs:
		print(c[0])
		print(c)

	return cliques

# Get the biggest (or one of the biggest) cliques in the graph
#
# Using a naive approach, starting for the biggest ammount of
def getBiggestClique():
    pass
