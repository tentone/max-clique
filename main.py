import graph
import gui
import generator
def main():
	g = generator.generate(63944, 5)

	gui.GUI(g).run()

if __name__ == "__main__":
	main()
