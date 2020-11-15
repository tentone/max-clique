import time
import pprint
import math
from benchmark import Benchmark
from gui import GUI
from generator import GraphGenerator
from clique import Clique
from graph import Graph

def main():
	# Graph
	g = GUI()
	a = GraphGenerator.generate(63944, 10, 40)

	g.addGraph(a, (255, 0, 0), (255, 255, 0))

	# q, _ = Clique.findMaxBruteForceUp(a)
	# g.addGraph(q, (0, 0, 255), (0, 255, 255))

	# q, _ = Clique.findMaxBruteForceDown(a)
	# g.addGraph(q, (0, 0, 255), (0, 255, 255))

	q, _ = Clique.findMaxGreedy(a)
	g.addGraph(q, (0, 0, 255), (0, 255, 255))

	g.run()

if __name__ == "__main__":
	main()
