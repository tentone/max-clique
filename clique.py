import itertools
from graph import Graph, Edge

# Static class with method to process cliques in a graph.
class Clique:
	# Searches for all cliques inside of the graph.
	#
	# Uses a naive approach testing all combinations of vertexes and checking if each group has connections to each others.
	@staticmethod
	def findAllBruteForce(g):
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
					cliques.append(Clique.buildClique(c))

			# Increase size
			size += 1

			if not cliqueFound:
				break

		return cliques

	# Find the maximum clique using a naive approach testing all combinations of vertexes.
	#
	# Starts by testing the higher possible, size of the clique
	@staticmethod
	def findMaxBruteForceDown(g):
		size = len(g.vertices)
		operations = 0

		while size > 1:
			# All possible combinations of vertices
			combinations = list(itertools.combinations(g.vertices, size))

			# Iterate all combinations
			for c in combinations:
				isClique = True

				# Check if the vertices are all connected
				for i in range(0, len(c) - 1):
					for j in range(i + 1, len(c)):
						operations += 1
						# If a edge is not connected then it is not a clique
						if not g.edgeExists(c[i], c[j]):
							isClique = False
							break

					# Break if is not a clique
					if not isClique:
						break

				# First clique found can be directly considered as the biggest
				if isClique:
					return Clique.buildClique(c), operations

			# Decrease size
			size -= 1

		return None, operations

	# Find the maximum clique using a naive approach testing all combinations of vertexes.
	#
	# Starts by testing the lower possible, size of the clique
	@staticmethod
	def findMaxBruteForceUp(g):
		size = 2
		operations = 0

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
						operations += 1
						# If a edge is not connected then it is not a clique
						if not g.edgeExists(c[i], c[j]):
							isClique = False
							break

					# Break if is not a clique
					if not isClique:
						break

				# Store clique
				if isClique:
					# Store and move to next size
					maxClique = Clique.buildClique(c)
					break

			# Decrease size
			size += 1

		return maxClique, operations

	# Find the maximum clique by seraching for smaller ones first and then expanding the smaller ones found.
	#
	# Starts with 2 by 2 cliques and expands them from there.
	@staticmethod
	def findMaxGreedy(g):
		# Use the list of adjacencies as a starting point
		cliques = []
		for e in g.edges:
			base = e.v.copy()
			toTest = []
			for v in g.vertices:
				if not v in base:
					toTest.append(v)
			cliques.append(CliqueGreedy(base, toTest))

		operations = 0
		size = 2

		while len(cliques) > 1 and size < len(g.vertices):
			# Check if the cliques can be expanded further
			for clique in cliques:
				# Stop if the clique is the last one it is the maximum already
				if len(cliques) == 1:
					break

				# If the clique can be expanded
				cliqueWasExpanded = False

				# Iterate trought all other vertices that are not in the clique
				for newVert in clique.toTest:
					# Remove from list of vertice to be tested
					clique.toTest.remove(newVert)

					# Check if it has connectivity to the already exisiting vertices in the set
					hasFullConnect = True
					for vert in clique.vertices:
						operations += 1
						if not g.edgeExists(newVert, vert):
							hasFullConnect = False
							break

					# Add to the list of vertice
					if hasFullConnect:
						clique.vertices.append(newVert)
						cliqueWasExpanded = True
						break

				# Discard any cliques that could not be expanded further
				if not cliqueWasExpanded:
					cliques.remove(clique)

			size += 1

		if len(cliques) > 0:
			return Clique.buildClique(cliques[0].vertices), operations

		return None, operations


	# Build clique using a list of vertices.
	@staticmethod
	def buildClique(vertices):
		cq = Graph()
		cq.vertices = vertices
		for i in range(0, len(vertices) - 1):
			for j in range(i + 1, len(vertices)):
				cq.addEdge(Edge(vertices[i], vertices[j]))
		return cq

class CliqueGreedy:
	def __init__(self, vertices, toTest):
		self.vertices = vertices
		self.toTest = toTest
