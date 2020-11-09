import gui
import generator

def main():
	a = generator.generate(63944, 10)

	g = gui.GUI()
	g.addGraph(a, (255, 0, 0), (255, 255, 0))
	g.run()

if __name__ == "__main__":
	main()
