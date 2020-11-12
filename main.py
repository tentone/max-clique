from benchmark import Benchmark
import gui
import generator
import clique
import pprint

def main():
	# Benchmark
	# b = Benchmark()
	# _, average = b.run(clique.Clique.findMaxNaive)
	# Benchmark.writeCSV(average, 'test.csv')
	#pprint.pprint(results)

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

	q, _ = clique.Clique.findMaxNaive(a)
	g.addGraph(q, (0, 0, 255), (0, 255, 255))

	g.run()

if __name__ == "__main__":
	main()
