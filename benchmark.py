import math
import time
import pprint
import csv
from generator import GraphGenerator
from graph import Graph

# Class that stores a testing configuration
#
# Object can be used to run tests in a algorithm.
class Benchmark:
	def __init__(self):
		# How many test to do for each graph configuration
		self.tests = 10

		# Graph size
		self.vertices_from = 3
		self.vertices_to = 22
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
		average = []

		# Min results for group of tests
		minimum = []

		# Max results for group of tests
		maximum = []

		connectivity = self.connectivity_from
		vertices = self.vertices_from

		while vertices <= self.vertices_to:
			connectivity = self.connectivity_from
			while connectivity <= self.connectivity_to:
				# Average value
				avg = BenchmarkResult(0, 0, 0, 0, 0)

				# List of results from all tests performed
				results = []

				for t in range(0, self.tests):
					# Calculate the number of edges for % connectivity
					edges = math.ceil(Graph.maximumEdges(vertices) * connectivity)
					g = GraphGenerator.generate(t, vertices, edges)

					# Run the algorithm
					start = time.perf_counter()
					_, iterations = algorithmFunc(g)
					end = time.perf_counter()

					# Update average
					results.append(BenchmarkResult(vertices, edges, connectivity, iterations, end - start))
					avg.add(vertices, edges, connectivity, iterations, end - start)

				# Calculate and store average
				avg.average(self.tests)
				average.append(avg)

				# Calculate minimum and maximum
				min, max = self.extractMinMax(results)
				minimum.append(min)
				maximum.append(max)

				# Increase connectivity
				connectivity += self.connectivity_steps

			# Icrease number of vertices
			vertices += self.vertices_steps

		return average, minimum, maximum

	# Get minimum and maximum times and iterations from list of results
	#
	# Receives a list of results as parameter.
	@staticmethod
	def extractMinMax(results):
		min = results[0]
		max = results[0]

		for r in results:
			if min.iterations > r.iterations:
				min = r
			if max.iterations < r.iterations:
				max = r

		return min, max

	# Write the results to a CSV file for easier analysis
	@staticmethod
	def writeCSV(results, fname):
		with open(fname, 'w', newline='') as csvfile:
			fieldnames = ['vertices', 'edges', 'connectivity', 'iterations', 'time']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()
			for r in results:
				writer.writerow({'vertices': r.vertices, 'edges': r.edges, 'connectivity': r.connectivity, 'iterations': r.iterations, 'time': r.time})


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
