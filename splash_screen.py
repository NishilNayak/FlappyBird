import pygame,sys
import button

pygame.init()
audio_start = pygame.mixer.Sound('splashScreenAudio.mp3')
audio_start.play()
screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()
pygame.display.set_caption('Flappy Bird') 

start_img = pygame.image.load('flappy_start.png').convert_alpha()

start_button = button.Button(115, 110, start_img, 1)
BACKGROUND = pygame.image.load('img/background.png')
run = True
while run:
    
	screen.blit(BACKGROUND, (0, 0))

	if start_button.draw(screen):
		exec(open('textbutton.py').read())
	

	#event handler
	for event in pygame.event.get():
		#quit game
		if event.type == pygame.QUIT:
			run = False
            
	pygame.display.update()

pygame.quit()


     
pygame.display.flip()
clock.tick(60)