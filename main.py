import time
from benchmark import Benchmark
import gui
from generator import GraphGenerator
from clique import Clique
import pprint

def main():
	b = Benchmark()

	# Benchmark Naive Down
	# results, min, max = b.run(Clique.findMaxNaiveDown)
	# Benchmark.writeCSV(results, 'naive_down_avg.csv')
	# Benchmark.writeCSV(min, 'naive_down_min.csv')
	# Benchmark.writeCSV(max, 'naive_down_max.csv')

	# Benchmark Naive Up
	# results, min, max = b.run(Clique.findMaxNaiveUp)
	# Benchmark.writeCSV(results, 'naive_up_avg.csv')
	# Benchmark.writeCSV(min, 'naive_up_min.csv')
	# Benchmark.writeCSV(max, 'naive_up_max.csv')

	# Benchmark expand
	# results = b.run(Clique.findMaxExpansion)
	# Benchmark.writeCSV(results, 'expansion.csv')

	# Graph
	# g = gui.GUI()
	# a = GraphGenerator.generate(63944, 10, 40)
	# print(a.toJSON())
	# print(a.adjacencyMatrix())

	# g.addGraph(a, (255, 0, 0), (255, 255, 0))

	# All cliques
	#q = Clique.findAllNaive(a)
	#if len(q) > 0:
	# 	g.addGraph(q[-1], (0, 0, 255), (0, 255, 255))

	# q, _ = Clique.findMaxNaiveUp(a)
	# g.addGraph(q, (0, 0, 255), (0, 255, 255))

	# g.run()

if __name__ == "__main__":
	main()
