import gui
import generator
import clique

def main():
	a = generator.generate(63944, 20, 100)
	q = clique.findAllCliquesNaive(a)

	g = gui.GUI()
	g.addGraph(a, (255, 0, 0), (255, 255, 0))
	if len(q) > 0:
		g.addGraph(q[-1], (0, 0, 255), (0, 255, 255))

	g.run()

if __name__ == "__main__":
	main()
