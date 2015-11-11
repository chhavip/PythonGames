import pygame
import time
import random
pygame.init()


display_width = 600
display_height = 800

white = (255,255,255)
black = (0,0,0)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)

car_width = 73

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('Yeah whatever')

clock = pygame.time.Clock()

carImg = pygame.image.load('racecar.png')

def things_dodged(count, speed):
	font = pygame.font.SysFont(None, 25)
	text = font.render("Dodged: "+str(count), True, black)
	gameDisplay.blit(text,(0,0))

def things(thingx, thingy, w, h, color):
	pygame.draw.rect(gameDisplay, color, [thingx,thingy, w,h])

def car(x,y):
	gameDisplay.blit(carImg,(x,y))#has to be a tuple

def crash():
	message_display('You crashed')

def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf',50)
	TextSurf, TextRect = text_objects(text,largeText)
	TextRect.center = ((display_width/2),(display_height/2))
	gameDisplay.blit(TextSurf,TextRect)
	pygame.display.update()
	time.sleep(2)
	game_loop()

def text_objects(text,font):
	textSurface = font.render(text,True,black)
	return textSurface, textSurface.get_rect()

def game_intro():
	intro  = True

	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		gameDisplay.fill(white)
		largeText = pygame.font.Font('freesansbold.ttf',50)
		TextSurf, TextRect = text_objects("A bit Racey",largeText)
		TextRect.center = ((display_width/2),(display_height/2))
		gameDisplay.blit(TextSurf,TextRect)

		mouse = pygame.mouse.get_pos()
		#print mouse

		if 120 + 100 > mouse[0] > 150 and 450 + 50 > mouse[1] > 450:
			pygame.draw.rect(gameDisplay, green, (120,450,100,50))
		else:
		    pygame.draw.rect(gameDisplay, bright_green, (120,450,100,50))

		smallText = pygame.font.Font("freesansbold.ttf",20)
		textSurf, textRect = text_objects("GO !", smallText)
		textRect.center = ( (120 + (100/2)) , (450 + (50/2)) )
		gameDisplay.blit(textSurf, textRect)

		pygame.draw.rect(gameDisplay, red, (350,450,100,50))

		pygame.display.update()
		clock.tick(15)







def game_loop():
	x = (display_width*0.45)
	y = (display_height*0.8)

	x_change = 0
	y_change = 0
	gameExit = False
	dodged = 0
	thing_count = 1

	thing_startx = random.randrange(0, display_width)
	thing_starty = -600
	thing_speed = 6
	thing_width = 100
	thing_height = 100

	while not gameExit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -5
				elif event.key == pygame.K_RIGHT:
					x_change = 5
				elif event.key == pygame.K_DOWN:
					y_change = 5
				elif event.key == pygame.K_UP:
					y_change = -5

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					y_change = 0


		x+=x_change
		y+=y_change

		


		gameDisplay.fill(white)
	#	for i in 0 , 10:
		for i in 0, thing_count:
			things(thing_startx,thing_starty, thing_width, thing_height, black)
			thing_starty += thing_speed
		car(x,y)
		things_dodged(dodged,thing_speed)
		if x> display_width - car_width or x < 0:
			crash()

		if thing_starty > display_height:
			thing_starty = 0 - thing_height
			thing_startx =x + random.randrange(-50, 50)
			dodged+=1
			if dodged % 15 == 0:
				thing_speed+=2

		if y < thing_starty + thing_height:
			#print 'step 1'

			if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
				#print 'collision'
				crash()



		pygame.display.update()
		clock.tick(60)
game_intro()
game_loop()
pygame.quit()
quit()