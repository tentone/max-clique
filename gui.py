import threading
import pygame
from pygame import Vector2
from pygame.locals import *

# GUI to visualize the created graph and its adjacencies.
#
# Each graph vertex is drawn in the grid with its connection to other graph vertices.
class GUI:
	def __init__(self, graph):
		# Graph to be presented
		self.graph = graph

		# Window resolution
		self.resolution = (800, 600)

		# Camera position
		self.camera = (200, 400)

		# Zoom
		self.zoom = 1

		# Mouse position
		self.mouse = (0, 0)

		pygame.font.init()
		pygame.init()
		pygame.display.set_caption("DAA - Graph Clique")
		pygame.display.set_mode(self.resolution, pygame.RESIZABLE)

		self.surface = pygame.display.get_surface();
		self.font = pygame.font.SysFont(None, 20)

	# Update the GUI to draw the updated graph
	def update(self, events):

		for event in events:
			if event.type == QUIT:
				pygame.quit()
				quit()
			# Exit the GUI if the ESC key was pressed
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					quit()
			# Update the screen resolution if the window was resized
			elif event.type == VIDEORESIZE:
				self.resolution = event.size
				self.surface = pygame.display.set_mode(event.size, pygame.RESIZABLE)
			elif event.type == MOUSEWHEEL:
				self.zoom += event.y
				if self.zoom <= 0:
					self.zoom = 1

		# If the mouse button is pressed move the camera position
		if pygame.mouse.get_pressed()[0]:
			self.camera = (self.camera[0] + (pygame.mouse.get_pos()[0]-self.mouse[0]), self.camera[1] - (pygame.mouse.get_pos()[1]-self.mouse[1]))

		self.mouse = pygame.mouse.get_pos()

		self.surface.fill(Color(0, 0, 0))

		# Spacing between the graph nodes
		sp = 3

		# Draw grid
		for x in range(1, 21):
			self.line((100, 100, 100), Vector2(x * sp, sp), Vector2(x * sp, 20 * sp))
			self.line((100, 100, 100), Vector2(sp, x * sp), Vector2(20 * sp, x * sp))

		# Draw the graph into the screen
		for e in self.graph.edges:
			self.line((255, 255, 0), Vector2(e.v[0].x * sp, e.v[0].y * sp), Vector2(e.v[1].x * sp, e.v[1].y * sp))

		for v in self.graph.vertices:
			self.circle(Color(255, 0, 0), Vector2(v.x * sp, v.y * sp), 1)

		pygame.display.flip()

	# Transform a point using the camera position and zoom level
	def transform(self, val):
		return ((int)(val[0] * self.zoom + self.camera[0]), (int)(self.resolution[1] - (val[1] * self.zoom + self.camera[1])))

	# Draw a line from init to end
	def line(self, color, ini, end):
		pygame.draw.line(self.surface, color, self.transform(ini), self.transform(end), 2)

	# Draw a circle into the screen
	def circle(self, color, center, radius, inner_radius = 0):
		pygame.draw.circle(self.surface, color, self.transform(center), radius * self.zoom, inner_radius * self.zoom)

	# Draw a point into the screen
	def point(self, color, pos):
		pygame.draw.circle(self.surface, color, self.transform(pos), 2, 0)

	# Loop to keep the GUI updated runs in a thread that is started by the run() method.
	def run(self):
		while True:
			self.update(pygame.event.get())

	# Run the GUI in a separate thread
	def start(self):
		t = None
		try:
			t = threading.Thread(self.run)
			t.start()
		except:
			print("Failed to start GUI thread")

		return t
