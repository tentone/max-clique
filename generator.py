import random
import graph

class Generator:
	# Generate a new graph with the provided configuration.
	#
	# Uses a new pseudo-random algorithm w/ seed as starting point to ensure repeatibility
	@staticmethod
	def generate(seed, complexity):
		random.seed(seed)

		g = graph.Graph()

		# Vertex
		for i in range(complexity):
			v = graph.Vertex(random.randint(1, 20), random.randint(1, 20))

			if not g.occupied(v.x, v.y):
				g.addVertex(v)

		# Edges
		for i in range(complexity):
			e = graph.Edge()

