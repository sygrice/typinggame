import os
import random
import pygame
from word import Word
from color import Color
cp = os.path.abspath(__file__)

c = Color()
GRAY = c.gray
BLACK = c.black
WHITE = c.white

W = 800
H = 600
pygame.init()
screen = pygame.display.set_mode((W,H))

# font
font = pygame.font.SysFont('Arial',24)

words = []
with open('vocab.txt', 'r') as f:
	for word in f:
		words.append(word.strip())
# the words on screen now
nowwords = []

# user's choice
speed = 2 
timeinterval = 1000 # ms
FPS = 60

# game param
timecounter = 0
clock = pygame.time.Clock()

user_input = ''

running = True
while running:
	dt = clock.tick(FPS) # seconds
	timecounter += dt # add seconds and count time

	# listening events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			# when press enter, del first satisfied word in nowwords
			if event.key == pygame.K_RETURN:
				count = 0
				# nowwords = [i for i in nowwords if i.text != user_input] # nowwords:list[Word()]
				for idx, word in enumerate(nowwords):
					if word.text == user_input:
						del nowwords[idx]
						break

				user_input=''
			elif event.key == pygame.K_BACKSPACE:
				user_input = user_input[:-1]
			else:
				user_input += event.unicode
	# print(user_input)

	if timecounter >= timeinterval: # when conuter big enough, create new word
		timecounter = 0
		text = random.choice(words)
		# random.randint's sec param: minus the input box's height
		thisword = Word(text, -len(text)//2, random.randint(50, H-100), speed, font)
		nowwords.append(thisword)
		
	for word in nowwords:
		word.move()
	nowwords = [word for word in nowwords if not word.is_out_of_bounds(W)]

	screen.fill(WHITE)

	for word in nowwords:
		word.draw(screen)

	# user input box
	box_posx = 10
	box_posy = H-40
	pygame.draw.rect(screen, GRAY, (box_posx, box_posy, 300, 30))
	text_surface = font.render(user_input, True, BLACK)
	screen.blit(text_surface, (box_posx+5, box_posy+3))

	pygame.display.flip()
pygame.quit()
