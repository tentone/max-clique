import generator
import math
import time
import graph
import pprint
import csv

class BenchmarkResult:
	def __init__(self, vertices, edges, result, iterations, time):
		self.vertices = vertices
		self.edges = edges
		self.iterations = iterations
		self.time = time
		self.result = result

	def add(self, vertices, edges, iterations, time):
		self.vertices += vertices
		self.edges += edges
		self.iterations += iterations
		self.time += time

	def average(self, tests):
		self.vertices /= tests
		self.edges /= tests
		self.iterations /= tests
		self.time /= tests

	def __repr__(self):
		return pprint.pformat(vars(self), indent=4, width=1)

class Benchmark:
	def __init__(self):
		# How many test to do for each graph configuration
		self.tests = 10

		# Graph size
		self.vertices_from = 4
		self.vertices_to = 12
		self.vertices_steps = 2

		# Connectivity
		self.connectivity_from = 0.2
		self.connectivity_to = 0.8
		self.connectivity_steps = 0.2

	# Run a benchmark for the algorithm.
	#
	# Measures the time required to run the algorithm, the algorithm should return the result and the number of base operations performed.
	def run(self, algorithmFunc):
		# Results obtained from the benchmark
		results = []

		# Average results for group of tests
		averages = []

		connectivity = self.connectivity_from
		vertices = self.vertices_from

		while vertices <= self.vertices_to:
			connectivity = self.connectivity_from
			while connectivity <= self.connectivity_to:
				average = BenchmarkResult(0, 0, None, 0, 0)

				for t in range(0, self.tests):
					# Calculate the number of edges for % connectivity
					edges = math.ceil(graph.Graph.maximumEdges(vertices) * connectivity)
					g = generator.GraphGenerator.generate(t, vertices, edges)

					# Run the algorithm
					start = time.perf_counter()
					result, iterations = algorithmFunc(g)
					end = time.perf_counter()

					# Update average
					average.add(vertices, edges, iterations, end-start)

					# Store results
					results.append(BenchmarkResult(vertices, edges, result, iterations, end-start))

				average.average(self.tests)
				averages.append(average)

				# Increase connectivity
				connectivity += self.connectivity_steps

			# Icrease number of vertices
			vertices += self.vertices_steps

		return results, averages

	@staticmethod
	def writeCSV(results, fname):
		with open(fname, 'w', newline='') as csvfile:
			fieldnames = ['vertices', 'edges', 'iterations', 'time']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()
			for r in results:
				writer.writerow({'vertices': r.vertices, 'edges': r.edges, 'iterations': r.iterations, 'time': r.time})
