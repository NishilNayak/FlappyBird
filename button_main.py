import pygame
import button

#create display window
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1000

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird')

#load button images
start_img = pygame.image.load('start_btn.png').convert_alpha()
exit_img = pygame.image.load('exit_btn.png').convert_alpha()

#create button instances
start_button = button.Button(200, 400, start_img, 0.8)
exit_button = button.Button(600, 400, exit_img, 0.8)

BACKGROUND = pygame.image.load('img/background.png')
#game loop
run = True
while run:
    
	screen.blit(BACKGROUND, (0, 0))

	if start_button.draw(screen):
		exec(open('flappybird.py').read())
	if exit_button.draw(screen):
		exec(open('flappybird.py').read())

	#event handler
	for event in pygame.event.get():
		#quit game
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()