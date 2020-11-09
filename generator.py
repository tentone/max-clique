import random
import graph

# Generate a new graph with the provided configuration.
#
# Uses a new pseudo-random algorithm w/ seed as starting point to ensure repeatibility
def generate(seed, complexity):
	assert complexity > 2, "Complexity has to be greater than 2"

	random.seed(seed)

	g = graph.Graph()

	# Vertex
	for i in range(complexity):
		success = False
		while not success:
			v = graph.Vertex(random.randint(1, 20), random.randint(1, 20))

			if not g.isOccupied(v.x, v.y):
				g.addVertex(v)
				success = True

	# Edges
	for i in range(complexity):
		success = False
		while not success:
			max = len(g.edges) - 1

			a = g.edges[random.randint(0, max)]
			b = g.edges[random.randint(0, max)]

			while b == a:
				b = g.edges[random.randint(0, max)]

			e = graph.Edge(a, b)
			if not g.edgeExists(e):
				g.addEdge(e)
				success = True
