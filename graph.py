class Vertex:
	def __init__(self, x, y):
		assert x > 0 and x <= 20 and y > 0 and y <= 20

		self.x = x
		self.y = y

class Edge:
	def __init__(self, a, b):
		self.a = a
		self.b = b

class Graph:
	def __init__(self):
		self.vertices = []
		self.edges = []
