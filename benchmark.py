import generator


def benchmark(graph, maxCliqueFunc):
	# Results obtained from the benchmark
	results = []

	# How many test to do for each graph size
	test = 10

	# Graph size
	vertices_from = 3
	vertices_to = 6
	vertices_steps = 1

	# Connectivity
	connectivity_from = 0
	connectivity_to = 100
	connectivity_steps = 20

	a = generator.generate(0, 1, 40)


