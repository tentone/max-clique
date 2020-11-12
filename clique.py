import itertools
import graph

class Clique:
	# Searches for all cliques inside of the graph.
	#
	# Uses a naive approach testing all combinations of vertexes and checking if each group has connections to each others.
	@staticmethod
	def findAllNaive(g):
		# List of cliques found in the graph
		cliques = []

		size = 2

		while True:
			if size > len(g.vertices):
				break

			cliqueFound = False

			# All possible combinations of vertices
			combinations = list(itertools.combinations(g.vertices, size))

			# Iterate all combinations
			for c in combinations:
				isClique = True

				# Check if the vertices are all connected
				for i in range(0, len(c) - 1):
					for j in range(i + 1, len(c)):
						if not g.edgeExists(c[i], c[j]):
							isClique = False

				if isClique:
					cliqueFound = True

					# Create the subgraph and store
					clique = graph.Graph()
					clique.vertices = c
					for i in range(0, len(c) - 1):
						for j in range(i + 1, len(c)):
							clique.addEdge(graph.Edge(c[i], c[j]))
					cliques.append(clique)

			# Increase size
			size += 1

			if not cliqueFound:
				break

		return cliques

	# Find the maximum clique using a naive approach testing all combinations of vertexes.
	#
	# Starts by testing the higher possible, size of the clique
	@staticmethod
	def findMaxNaiveDown(g):
		size = len(g.vertices)
		comparisons = 0

		while size > 1:
			# All possible combinations of vertices
			combinations = list(itertools.combinations(g.vertices, size))

			# Iterate all combinations
			for c in combinations:
				isClique = True

				# Check if the vertices are all connected
				for i in range(0, len(c) - 1):
					for j in range(i + 1, len(c)):
						comparisons += 1
						# If a edge is not connected then it is not a clique
						if not g.edgeExists(c[i], c[j]):
							isClique = False
							break

					# Break if is not a clique
					if not isClique:
						break

				# First clique found can be directly considered as the biggest
				if isClique:
					clique = graph.Graph()
					clique.vertices = c
					for i in range(0, len(c) - 1):
						for j in range(i + 1, len(c)):
							clique.addEdge(graph.Edge(c[i], c[j]))
					return clique, comparisons

			# Decrease size
			size -= 1

		return None, comparisons

	# Find the maximum clique using a naive approach testing all combinations of vertexes.
	#
	# Starts by testing the lower possible, size of the clique
	@staticmethod
	def findMaxNaiveUp(g):
		size = 2
		comparisons = 0

		maxClique = None

		while size <= len(g.vertices):
			# All possible combinations of vertices
			combs = list(itertools.combinations(g.vertices, size))

			# Iterate all combinations
			for c in combs:
				isClique = True

				# Check if the vertices are all connected
				for i in range(0, len(c) - 1):
					for j in range(i + 1, len(c)):
						comparisons += 1
						# If a edge is not connected then it is not a clique
						if not g.edgeExists(c[i], c[j]):
							isClique = False
							break

					# Break if is not a clique
					if not isClique:
						break

				# Store clique
				if isClique:
					clique = graph.Graph()
					clique.vertices = c
					for i in range(0, len(c) - 1):
						for j in range(i + 1, len(c)):
							clique.addEdge(graph.Edge(c[i], c[j]))

					# Store and move to next size
					maxClique = clique
					break

			# Decrease size
			size += 1

		return maxClique, comparisons


	# Build clique using a list of vertices.
	def buildClique(vertices):
		cq = graph.Graph()
		cq.vertices = vertices
		for i in range(0, len(vertices) - 1):
			for j in range(i + 1, len(vertices)):
				cq.addEdge(graph.Edge(vertices[i], vertices[j]))
		return
