import random
import graph

class GraphGenerator:
	# Generate a new graph with the provided configuration.
	#
	# Uses a new pseudo-random algorithm w/ seed as starting point to ensure repeatibility
	@staticmethod
	def generate(seed, vertices, edges):
		random.seed(seed)

		g = graph.Graph()

		# Vertices
		for i in range(vertices):
			success = False
			while not success:
				v = graph.Vertex(random.randint(1, 20), random.randint(1, 20))

				if not g.isOccupiedRadius(v.x, v.y, 1):
					g.addVertex(v)
					success = True

		# Edges
		for i in range(edges):
			success = False
			while not success:
				max = len(g.vertices) - 1

				a = g.vertices[random.randint(0, max)]
				b = g.vertices[random.randint(0, max)]

				while b == a:
					b = g.vertices[random.randint(0, max)]

				if not g.edgeExists(a, b):
					e = graph.Edge(a, b)
					g.addEdge(e)
					success = True

		return g
