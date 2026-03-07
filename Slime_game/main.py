import pygame

import random
speed = 10
textwin = None
pygame.init()
gameover = False
font = pygame.font.Font(None, size=40)
timer = 0
timer2 = 0
screen = pygame.display.set_mode((1048, 720))
clock = pygame.time.Clock()
running = True
x = 0
y = 0
screenx = 1048
screeny = 720
xf = 0
yf = 0
player = pygame.image.load("player.png")
timerback = pygame.image.load("timer.png")
image_size = (100, 100)
player2 = pygame.transform.scale(player,image_size)
player3 = pygame.transform.flip(player2, True, False)
food = pygame.image.load("food.png")
playerfinal = player2
background = pygame.image.load("background.png")
finishback = pygame.image.load("finishback.png")


while running:
    
    
    
        
         
        timer += 1
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
                y -= speed


        if keys[pygame.K_s]:
                y += speed
                
                
        if keys[pygame.K_a]:
                x -= speed
                playerfinal = player2

        if keys[pygame.K_d]:
                x += speed
                playerfinal = player3
                
        if keys[pygame.K_r]:
                pygame.time.delay(100)
                speed = 10
                textwin = None
                pygame.init()
                gameover = False
                font = pygame.font.Font(None, size=40)
                timer = 0
                timer2 = 0
                screen = pygame.display.set_mode((1048, 720))
                clock = pygame.time.Clock()
                running = True
                x = 0
                y = 0
                screenx = 1048
                screeny = 720
                xf = 0
                yf = 0
                player = pygame.image.load("player.png")
                image_size = (100, 100)
                player2 = pygame.transform.scale(player,image_size)
                player3 = pygame.transform.flip(player2, True, False)
                food = pygame.image.load("food.png")
                playerfinal = player2

        hitboxplayer = pygame.Rect(x,y, image_size[0], image_size[1])
        hitboxfood = food.get_rect(topleft=(xf,yf))
        
        if hitboxplayer.colliderect(hitboxfood):
                xf = random.randint(0, 1048 - 100)
                yf = random.randint(0, 720 - 100)
                image_size = (image_size[0] + 2, image_size[1] + 2) 
                speed += 0.06

        if image_size[0] >= 1048:
                if image_size[1] >= 720:
                        if textwin is None:
                                textwin = font.render("You win! Time: " + str(timer2), True, (255,255,255))
                        
        
        timer2 = timer / 60
        timer2 = round(timer2, 1)
        
        text = font.render(str(timer2), True, (255, 255, 255))
        playerfinal3 = pygame.transform.scale(playerfinal, image_size)
        
        
        screen.fill((0,0,0))
        
        
        screen.blit(background, (0,0))
        screen.blit(playerfinal3, (x,y))
        screen.blit(food, (xf,yf))
        screen.blit(timerback, (480, 45))
        screen.blit(text, (490, 50))
        if textwin:
                screen.blit(finishback, (370, 295))
                screen.blit(textwin, (380, 300))
        

        
        
        
        pygame.display.flip()
        
        
        
       
        clock.tick(60)      
    
pygame.quit()