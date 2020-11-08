import random

class Generator:
	# Generate a new graph with the provided configuration.
	#
	# Uses a new pseudo-random algorithm w/ seed as starting point to ensure repeatibility
	@staticmethod
	def generate(seed, complexity):


		for i in range(complexity):
			random.seed(seed)
