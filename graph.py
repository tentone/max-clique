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

	# Check if the edge contains one of the vertices
	def contains(self, v):
		return v in self.v

	# Check if the edge has the vertices a and b
	def hasVertices(self, a, b):
		return a in self.v and b in self.v

# Stores the full graph data.
#
# Vertex and edge data is stored separatelly.
class Graph:
	def __init__(self):
		self.vertices = []
		self.edges = []

	# Get the edges for a specific vertex
	def getEdges(self, v):
		edges = []
		for e in self.edges:
			if e.contains(v):
				edges.append(e)

		return edges

	# Add a new vertex to the graph
	def addVertex(self, v):
		self.vertices.append(v)

	# Add a edge to the graph
	def addEdge(self, e):
		self.edges.append(e)

	# Check if a edge that connects a and b exists
	def edgeExists(self, a, b):
		for e in self.edges:
			if e.hasVertices(a, b):
				return True
		return False

	# Check a position in the graph is occupied
	def isOccupied(self, x, y):
		for v in self.vertices:
			if v.x == x and v.y == y:
				return True
		return False

	# Check a the graph is occupied around a position in a neighborhood
	#
	# The manhattan distance between points is used.
	def isOccupiedRadius(self, x, y, radius):
		for v in self.vertices:
			if x >= v.x - radius and x <= v.x + radius and y >= v.y - radius and y <= v.y + radius:
				return True
		return False
