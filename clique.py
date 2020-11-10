from itertools import combinations
import graph

# Searches for all cliques inside of the graph.
#
# Uses a naive approach doing all combinations of vertexes and checking if each group has connections to each others.
def findCliquesNaive(g):
	# List of cliques found in the graph
	cliques = []

	size = 2

	while True:
		if size > len(g.vertices):
			break

		cliqueFound = False

		# All possible combinations of vertices
		combs = list(combinations(g.vertices, size))

		# Iterate all combinations
		for c in combs:
			isClique = True

			# Check if the vertices are all connected
			for i in range(0, len(c) - 1):
				for j in range(i + 1, len(c)):
					if not g.edgeExists(c[i], c[j]):
						isClique = False

			if isClique:
				cliqueFound = True

				# Create the subgraph and store
				cq = graph.Graph()
				cq.vertices = c
				for i in range(0, len(c) - 1):
					for j in range(i + 1, len(c)):
						cq.addEdge(graph.Edge(c[i], c[j]))
				cliques.append(cq)

		# Increase size
		size += 1

		if not cliqueFound:
			break

	return cliques

