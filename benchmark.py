import generator
import math
import time

class BenchmarkResult:
	def __init__(self, result, iterations, time):
		self.result = result
		self.iterations = iterations
		self.time = time

class Benchmark:
	def __init__(self):
		# How many test to do for each graph configuration
		self.test = 10

		# Graph size
		self.vertices_from = 3
		self.vertices_to = 6
		self.vertices_steps = 1

		# Connectivity
		self.connectivity_from = 0
		self.connectivity_to = 1.0
		self.connectivity_steps = 0.2

	# Run a benchmark for the algorithm.
	#
	# Measures the time required to run the algorithm, the algorithm should return the result and the number of base operations performed.
	def run(self, graph, algorithmFunc):
		# Results obtained from the benchmark
		results = []

		connectivity = self.connectivity_from
		vertices = self.vertices_from

		while vertices < self.vertices_to:
			connectivity = self.connectivity_from
			while connectivity < self.connectivity_to:
				# Calculate the number of edges for % connectivity
				edges = math.ceil(graph.Graph.maximumEdges(vertices) * connectivity)
				graph = generator.generate(0, vertices, edges)

				# Run the algorithm
				start = time.perf_counter()
				result, iterations = algorithmFunc(graph)
				end = time.perf_counter()

				# Store results
				results.append(BenchmarkResult(result, iterations, end-start))

				# Increase connectivity
				connectivity += self.connectivity_steps

			# Icrease number of vertices
			vertices += self.vertices_steps

		return results




