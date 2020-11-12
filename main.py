from benchmark import Benchmark
import gui
import generator
import clique
import pprint

def main():
	b = Benchmark()

	# Benchmark Naive Down
	results = b.run(clique.Clique.findMaxNaiveDown)
	Benchmark.writeCSV(results, 'naive_down.csv')

	# Benchmark Naive Up
	# results = b.run(clique.Clique.findMaxNaiveUp)
	# Benchmark.writeCSV(results, 'up.csv')

	# Benchmark expand
	# results = b.run(clique.Clique.findMaxNaiveUp)
	# Benchmark.writeCSV(results, 'up.csv')


	return

	# Graph
	g = gui.GUI()
	a = generator.GraphGenerator.generate(63944, 10, 40)
	# print(a.toJSON())
	# print(a.adjacencyMatrix())

	g.addGraph(a, (255, 0, 0), (255, 255, 0))

	# All cliques
	#q = clique.Clique.findAllNaive(a)
	#if len(q) > 0:
	# 	g.addGraph(q[-1], (0, 0, 255), (0, 255, 255))

	q, _ = clique.Clique.findMaxNaiveUp(a)
	g.addGraph(q, (0, 0, 255), (0, 255, 255))

	g.run()

if __name__ == "__main__":
	main()
