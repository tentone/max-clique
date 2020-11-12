from itertools import combinations
import graph

# Searches for all cliques inside of the graph.
#
# Uses a naive approach doing all combinations of vertexes and checking if each group has connections to each others.
def findAllCliques(g):
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

# Find the maximum clique using a naive approach.
#
# Starts by testing the higher possible, size of the clique
def findMaximumCliqueNaive(g):
	size = len(g.vertices)
	comparisons = 0

	while size > 1:
		# All possible combinations of vertices
		combs = list(combinations(g.vertices, size))

		# Iterate all combinations
		for c in combs:
			isClique = True

			# Check if the vertices are all connected
			for i in range(0, len(c) - 1):
				for j in range(i + 1, len(c)):
					# If a edge is not connected then it is not a clique
					if not g.edgeExists(c[i], c[j]):
						comparisons += 1
						isClique = False
						break

				# Break if is not a clique
				if not isClique:
					break

			# First clique found can be directly considered as the biggest
			if isClique:
				cq = graph.Graph()
				cq.vertices = c
				for i in range(0, len(c) - 1):
					for j in range(i + 1, len(c)):
						cq.addEdge(graph.Edge(c[i], c[j]))
				return cq, comparisons

		# Decrease size
		size -= 1

	return None, comparisons
