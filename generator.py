import random
import graph

# Generate a new graph with the provided configuration.
#
# Uses a new pseudo-random algorithm w/ seed as starting point to ensure repeatibility
def generate(seed, complexity):
	assert complexity > 2 and complexity < 20, "Complexity is out of range"

	random.seed(seed)

	g = graph.Graph()

	# Vertex
	for i in range(complexity):
		success = False
		while not success:
			v = graph.Vertex(random.randint(1, 20), random.randint(1, 20))

			if not g.isOccupiedRadius(v.x, v.y, 0):
				g.addVertex(v)
				success = True

	# Edges
	for i in range(complexity):
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
