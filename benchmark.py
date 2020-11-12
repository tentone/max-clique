import generator
import math
import time
import graph
import pprint
import csv

# Class to store a benchmark result
#
# Stores the metrics extracted from the run, these metric can be stored as an average value.
class BenchmarkResult:
	def __init__(self, vertices, edges, connectivity, iterations, time):
		self.vertices = vertices
		self.edges = edges
		self.connectivity = connectivity
		self.iterations = iterations
		self.time = time

	def add(self, vertices, edges, connectivity, iterations, time):
		self.vertices += vertices
		self.edges += edges
		self.connectivity += connectivity
		self.iterations += iterations
		self.time += time

	def average(self, tests):
		self.vertices /= tests
		self.edges /= tests
		self.connectivity /= tests
		self.iterations /= tests
		self.time /= tests

	def __repr__(self):
		return pprint.pformat(vars(self), indent=4, width=1)

class Benchmark:
	def __init__(self):
		# How many test to do for each graph configuration
		self.tests = 30

		# Graph size
		self.vertices_from = 4
		self.vertices_to = 12
		self.vertices_steps = 1

		# Connectivity
		self.connectivity_from = 0.1
		self.connectivity_to = 0.9
		self.connectivity_steps = 0.1

	# Run a benchmark for the algorithm.
	#
	# Measures the time required to run the algorithm, the algorithm should return the result and the number of base operations performed.
	def run(self, algorithmFunc):
		# Average results for group of tests
		results = []

		connectivity = self.connectivity_from
		vertices = self.vertices_from

		while vertices <= self.vertices_to:
			connectivity = self.connectivity_from
			while connectivity <= self.connectivity_to:
				res = BenchmarkResult(0, 0, 0, 0, 0)

				for t in range(0, self.tests):
					# Calculate the number of edges for % connectivity
					edges = math.ceil(graph.Graph.maximumEdges(vertices) * connectivity)
					g = generator.GraphGenerator.generate(t, vertices, edges)

					# Run the algorithm
					start = time.perf_counter()
					_, iterations = algorithmFunc(g)
					end = time.perf_counter()

					# Update average
					res.add(vertices, edges, connectivity, iterations, end - start)

				res.average(self.tests)
				results.append(res)

				# Increase connectivity
				connectivity += self.connectivity_steps

			# Icrease number of vertices
			vertices += self.vertices_steps

		return results

	# Write the results to a CSV file for easier analysis
	@staticmethod
	def writeCSV(results, fname):
		with open(fname, 'w', newline='') as csvfile:
			fieldnames = ['vertices', 'edges', 'iterations', 'time']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()
			for r in results:
				writer.writerow({'vertices': r.vertices, 'edges': r.edges, 'iterations': r.iterations, 'time': r.time})
