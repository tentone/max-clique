import json
import uuid

# Stores a vertex in a position of the graph.
#
# Vertices have (x, y) integer position associated.
class Vertex:
	def __init__(self, x, y):
		# UUID of the vertex, used for serialization.
		self.id = uuid.uuid4()

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

# Stores the full undirected graph data.
class Graph:
	def __init__(self):
		# List of all vertices that compose the graph
		self.vertices = []

		# Edges that connect the edges togheter
		self.edges = []

	# Max number of edges that a graph can have based of its number of vertices
	@staticmethod
	def maximumEdges(v):
		return v * (v - 1) / 2

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

	# Generate a adjacency matrix for the graph.
	#
	# May be useful for analysis in some scenarios.
	def adjacencyMatrix(self):
		matrix = []

		for a in range(0, len(self.vertices)):
			for b in range(0, len(self.vertices)):
				matrix.append(0 if (self.vertices[a] == self.vertices[b] or not self.edgeExists(self.vertices[a], self.vertices[b])) else 1)

		return matrix

	# Serialize the graph into a JSON file.
	#
	# The exported files contains all the vertices and the edges by id.
	def toJSON(self):
		edges = []
		for e in self.edges:
			edge = []
			for v in e.v:
				edge.append(str(v.id))
			edges.append(edge)

		vertices = []
		for v in self.vertices:
			vertices.append({
				'id': str(v.id),
				'x': v.x,
				'y': v.y
			})

		return json.dumps({
			'vertices': vertices,
			'edges': edges
		}, indent=4)
