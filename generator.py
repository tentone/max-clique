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

		# Generate vertex
		for i in range(complexity):
			v = graph.Vertex(random.randint(1, 20), random.randint(1, 20))


