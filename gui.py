import _thread
import pygame
from pygame import Vector2
from pygame.locals import *

# GUI to visualize the created graph and its adjacencies.
#
# Each graph vertex is drawn in the grid with its connection to other graph vertices.
class GUI:
	def __init__(self):
		# Window resolution
		self.resolution = (800, 600)

		# Camera position		
		self.camera = (200, 400)

		# Zoom
		self.zoom = 20

		# Mouse position
		self.mouse = (0, 0)

		pygame.font.init()
		pygame.init()
		pygame.display.set_caption("Graph")
		pygame.display.set_mode(self.resolution, pygame.RESIZABLE)

		self.surface = pygame.display.get_surface();
		self.font = pygame.font.SysFont(None, 20)

	# Update the GUI to draw the updated graph
	def update(self, events):
		for event in events:
			# Exit the GUI if the ESC key was pressed
			if event.type == QUIT or event.key == K_ESCAPE:
				pygame.quit()
				quit()
			# Update the screen resolution if the window was resized
			elif event.type == VIDEORESIZE:
				self.resolution = event.size
				self.surface = pygame.display.set_mode(event.size, pygame.RESIZABLE)

		# If the mouse button is pressed move the camera position
		if pygame.mouse.get_pressed()[0]:
			self.camera = (self.camera[0] + (pygame.mouse.get_pos()[0]-self.mouse[0]), self.camera[1] - (pygame.mouse.get_pos()[1]-self.mouse[1]))

		self.mouse = pygame.mouse.get_pos()

		pygame.draw.circle(self.surface, Color(255, 0, 0), Vector2(0, 0), 10)
		pygame.display.flip()

	# Transform a point using the camera position and zoom level
	def transform(self, val):
		return ((int)(val[0]*self.zoom+self.camera[0]), (int)(self.resolution[1]-(val[1]*self.zoom+self.camera[1])))

	# Draw a line from init to end
	def line(self, color, ini, end):
		pygame.draw.line(self.surface, color, self.transform(ini), self.transform(end), 2)

	# Draw a circle into the screen
	def circle(self, color, center, radius, inner_radius = 0):
		pygame.draw.circle(self.surface, color, self.transform(center), radius, inner_radius)

	# Draw a point into the screen
	def point(self, color, pos):
		pygame.draw.circle(self.surface, color, self.transform(pos), 2, 0)

	# Loop to keep the GUI updated runs in a thread that is started by the run() method.
	def loop(self):
		while True:
			self.update(pygame.event.get())

	def run(self):
		try:
			_thread.start_new_thread(self.loop)
		except:
			print("Failed to start GUI thread")
