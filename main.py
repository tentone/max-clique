import time
import pprint
from benchmark import Benchmark
from gui import GUI
from generator import GraphGenerator
from clique import Clique

def main():
	b = Benchmark()

	# Benchmark Naive Down
	# results, min, max = b.run(Clique.findMaxBruteForceDown)
	# Benchmark.writeCSV(results, 'naive_down_avg.csv')
	# Benchmark.writeCSV(min, 'naive_down_min.csv')
	# Benchmark.writeCSV(max, 'naive_down_max.csv')

	# Benchmark Naive Up
	# results, min, max = b.run(Clique.findMaxBruteForceUp)
	# Benchmark.writeCSV(results, 'naive_up_avg.csv')
	# Benchmark.writeCSV(min, 'naive_up_min.csv')
	# Benchmark.writeCSV(max, 'naive_up_max.csv')

	# Benchmark expand
	results, min, max = b.run(Clique.findMaxGreedy)
	Benchmark.writeCSV(results, 'greedy_avg.csv')
	Benchmark.writeCSV(min, 'greedy_min.csv')
	Benchmark.writeCSV(max, 'greedy_max.csv')

	# Graph
	g = GUI()
	a = GraphGenerator.generate(63944, 10, 40)

	g.addGraph(a, (255, 0, 0), (255, 255, 0))

	# q, _ = Clique.findMaxBruteForceDown(a)
	# g.addGraph(q, (0, 0, 255), (0, 255, 255))

	q, _ = Clique.findMaxGreedy(a)
	g.addGraph(q, (0, 0, 255), (0, 255, 255))

	g.run()

if __name__ == "__main__":
	main()
