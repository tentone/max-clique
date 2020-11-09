import gui
import generator

def main():
	g = generator.generate(63944, 10)

	gui.GUI(g).run()

if __name__ == "__main__":
	main()
