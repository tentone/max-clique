import gui
import generator
import clique

def main():
	a = generator.generate(63944, 6, 12)
	q = clique.findCliques(a)

	print(q)

	g = gui.GUI()
	g.addGraph(a, (255, 0, 0), (255, 255, 0))
	if len(q) > 0:
		g.addGraph(q[-1], (0, 0, 255), (0, 255, 255))

	g.run()

if __name__ == "__main__":
	main()
