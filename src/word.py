BLACK = (0,0,0)

class Word:
	def __init__(self,text, x, y, speed, font):
		self.text = text
		self.x = x
		self.y = y
		self.speed = speed
		self.font = font
		self.surface = font.render(text, True, BLACK)

	def move(self):
		# move to left
		self.x += self.speed

	def draw(self, screen):
		screen.blit(self.surface, (self.x, self.y))

	def is_out_of_bounds(self, width):
		return self.x > width

