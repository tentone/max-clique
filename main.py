import gui
import generator
import clique

def main():
	a = generator.generate(63944, 10)
	q = clique.findCliques(a)

	g = gui.GUI()
	g.addGraph(a, (255, 0, 0), (255, 255, 0))
	g.run()

if __name__ == "__main__":
	main()
