from pygame import*
import random

ballpic = image.load('ball.png')
ballpic.set_colorkey((0,0,0))

numBalls = 5
delay = 5

done = False

balls = []
 
for count in range(numBalls):
	balls.append(dict)
	balls[count] = {'x':count + 10,'y':random.randint(0,1),'ballxmove':random.randint(1,2),'ballymove':random.randint(1,2)}

	


init()
mixer.init()
screen = display.set_mode((640,480))
display.set_caption('Ball Game')
event.set_grab(1)

mixer.music.load('bgmusic.mp3')
mixer.music.play(-1)

while done == False:
	screen.fill(0)
	
	for count in range(numBalls):
		screen.blit(ballpic,(balls[count]['x'],balls[count]['y']))
	
	display.update()
	
	time.delay(delay)
	
	for count in range(numBalls):
		balls[count]['x'] = balls[count]['x'] + balls[count]['ballxmove']
		balls[count]['y'] = balls[count]['y'] + balls[count]['ballymove']
	
	for count in range(numBalls):
		if balls[count]['x'] > 620:
			balls[count]['ballxmove'] = random.randint(-2,0)
			
		if balls[count]['x'] < -1:
			balls[count]['ballxmove'] = random.randint(0,2)
			
		if balls[count]['y'] > 470:
			balls[count]['ballymove'] = random.randint(-2,0)
			
		if balls[count]['y'] < -1:
			balls[count]['ballymove'] = random.randint(0,2)
	
	for e in event.get():
		if e.type==KEYUP:
			if e.key == K_ESCAPE:
				done = True
	
	if screen.get_at((mouse.get_pos())) == (255,255,255,255):
		mixer.music.load('YouLost.mp3')
		mixer.music.play(0)
		time.delay(500)
		done = True
		
	print "You lasted for ",time.get_ticks()/1000,"seconds!"
		