#imported libraries
import pygame as pg
import time
import random

pg.init()

#sound upload
a=pg.mixer.Sound
crash_s = a("crash.wav")
intro1 = a("introtune.wav")
pg.mixer.music.load("intro.wav")

#car image n game icon upload
carImg = pg.image.load('car.png')
feImg = pg.image.load('fe.png')
pg.display.set_icon(feImg)

#outlay of window
window_width = 1450
window_height = 810


#colour RGB codes
dr = (144, 40, 247)
red = (200, 0, 0)
green = (0,155,0)
white = (255, 255, 255)
black = (0, 0, 0)
skyblue = (135,206,250)
maroon = (102, 0, 0)
bright_red = (255,0 , 0)
bright_green = (0,255,0)

#imp. declarations
pause = False
crash = True

car_width = 120

clock=pg.time.Clock()

screen = pg.display.set_mode((window_width,window_height))
pg.display.set_caption('Death Race')

#this funtion ends the program
def terminate():
    pg.quit()
    quit()

#unpauses the program
def unpause():
    global pause

    pg.mixer.music.unpause()
    #a.unpause()
    pause = False
    
#pauses the game
def paused():

    #stops music
    pg.mixer.music.pause()
    #a.pause()
    #defining
    screen.fill(black)
    font_format = pg.font.Font('freesansbold.ttf', 225)
    textsurface,  text_in_rec = text_objects('Paused', font_format)
    text_in_rec.center = ((window_width/2),(window_height/4))
    screen.blit(textsurface, text_in_rec)
    

    while pause:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                terminate()

#Button
        button("let's Go !",250,690,100,50,green,bright_green,unpause)

        button("QUIT!",850,690,100,50,red,bright_red,terminate)

        pg.display.update()
        clock.tick(15)




#counts the Score object
def objects_Score(count):
    font = pg.font.SysFont(None, 25)
    text = font.render('Score: '+ str(count), True,black)

    screen.blit(text,(0,0))

#creation of blocks
def objects(objectx, objecty, objectw, objecth, color):
    pg.draw.rect(screen, color, [objectx, objecty, objectw, objecth])

#fix the position of car on screen
def car(x,y):
    screen.blit(carImg,(x,y))

#
def text_objects(text, font): #color
    textsurfaceace = font.render(text, True,white)
    return textsurfaceace, textsurfaceace.get_rect()             

#message_format_formation
def message_display(text):
    font_format = pg.font.Font('freesansbold.ttf', 225)
    textsurface,  text_in_rec = text_objects(text, font_format)
    text_in_rec.center = ((window_width/2),(window_height/2))
    screen.blit(textsurface, text_in_rec)

    pg.display.flip()
    
    game_loop()

#This function when we crash
def crash():
    pg.mixer.music.stop()
    a.play(crash_s)
    
    font_format = pg.font.Font('C:\Windows\Fonts\Arial.ttf', 170)
    textsurface,  text_in_rec = text_objects('Rest in Pieces !!!', font_format)
    text_in_rec.center = ((window_width/2),(window_height/4))
    screen.blit(textsurface, text_in_rec)
    

    while crash:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                terminate()

       
        button("Play Again",250,690,130,45,green,bright_green,game_loop)

        button("Cry and go Home!",850,690,200,45,red,bright_red,terminate)
        


        #pg.draw.rect(screen, red,(850,690,100,50))

        pg.display.update()
        clock.tick(15)


#giving functionality to buttons
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()

        #clicking on button
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pg.draw.rect(screen, ac,(x,y,w,h))    
        if click[0] == 1 and action != None:
            action()
         
    else:
            
#BUTTON
        pg.draw.rect(screen, ic,(x,y,w,h))
    smallText = pg.font.Font("freesansbold.ttf",20)

    textsurface, text_in_rec = text_objects(msg, smallText)
    text_in_rec.center = ((x+(w/2)), (y+(h/2)))
    screen.blit(textsurface, text_in_rec)


#intro window editing, creating buttons, giving functionality to buttons
def game_intro():
    a.play(intro1,1)
    intro = True

    while intro:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        screen.fill(black)
        font_format = pg.font.Font('freesansbold.ttf', 225)
        textsurface,  text_in_rec = text_objects('Death Race', font_format)
        text_in_rec.center = ((window_width/2),(window_height/4))
        screen.blit(textsurface, text_in_rec)

        button("Go and Drift!!!",250,690,150,45,green,bright_green,game_loop)

        button("QUIT!",850,690,100,45,red,bright_red,terminate)
        


        #pg.draw.rect(screen, red,(850,690,100,50))

        pg.display.update()
        clock.tick(15)


def game_loop():
    global pause
    pg.mixer.music.play(-1)

    
    x = (window_width * 0.45)
    y = (window_height * 0.70)
    x_change = 0
    object_dx = random.randrange(0, window_width)
    object_dy = -600
    object_speed = 8
    object_width = 185
    object_height = 100

    Score = 0                   
    
    gameexit = False

#event handling loop
    while not gameexit:

        for event in pg.event.get():
            if event.type == pg.QUIT: 
                pg.quit()
                terminate()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    x_change = -5
                if event.key == pg.K_RIGHT:
                    x_change = 5
                if event.key == pg.K_p:
                    pause = True
                    paused()

            if event.type == pg.KEYUP:
                if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                    x_change = 0                
                
                
        x += x_change
    
        screen.fill(skyblue)
     
        objects(object_dx, object_dy, object_width, object_height,maroon)
        object_dy += object_speed
        
        car(x,y)

        objects_Score(Score)
    
        if x > window_width - car_width or x < 0:
            crash()
            #terminate()

        if object_dy > window_height:
            object_dy = 0 - object_height
            object_dx = random.randrange(0,window_width)
            Score += 1
            object_speed += 0.2
            object_width += (Score * 2)

#crashing code
        if y < object_dy + object_height:
            
            if x > object_dx and x < object_dx + object_width or x +car_width > object_dx and x + car_width<object_dx + object_width:
                 
                 crash()
        
        pg.display.flip()
       
        clock.tick(120)

game_intro()
game_loop()
pg.quit()
quit()



