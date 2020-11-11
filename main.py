import gui
import generator
import clique

def main():
	g = gui.GUI()

	# Graph
	a = generator.generate(63944, 10, 40)
	print(a.serialize())
	g.addGraph(a, (255, 0, 0), (255, 255, 0))

	# All cliques
	#q = clique.findAllCliquesNaive(a)
	#if len(q) > 0:
	#	g.addGraph(q[-1], (0, 0, 255), (0, 255, 255))

	q = clique.findMaximumCliqueNaive(a)
	g.addGraph(q, (0, 0, 255), (0, 255, 255))

	g.run()

if __name__ == "__main__":
	main()
