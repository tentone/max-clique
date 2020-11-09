# Stores a vertex in a position of the graph.
class Vertex:
	def __init__(self, x, y):
		assert x > 0 and x <= 20 and y > 0 and y <= 20

		self.x = x
		self.y = y

# Stores an edge that connects two vertices togheter
#
# Edges dont have direction associated with them.
class Edge:
	def __init__(self, a, b):
		assert not a == b

		self.v = [a, b]

	def contains(self, a, b):
		return a in self.v and b in self.v

# Stores the full graph data.
#
# Vertex and edge data is stored separatelly.
class Graph:
	def __init__(self):
		self.vertices = []
		self.edges = []

	def addVertex(self, v):
		self.vertices.append(v)

	def addEdge(self, e):
		self.edges.append(e)

	def edgeExists(self, a, b):
		for e in self.edges:
			if e.contains(a, b):
				return True
		return False

	def isOccupied(self, x, y):
		for v in self.vertices:
			if v.x == x and v.y == y:
				return True
		return False
