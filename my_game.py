import pygame
import random
from button import button

pygame.init()
width = 1200
height = 600

screen = pygame.display.set_mode((width, height), pygame.SCALED, vsync=1)
clock = pygame.time.Clock()

pos_x = 500
pos_y = 300
ph=100
pw=80
lives = 3
font = pygame.font.SysFont(None , 50)

#coin stuff
currycoin = 0
coin_size = 50
cra_z_coin = False
coins = []
feet = 0
feeties = ""
framedcoins = [pygame.image.load("this`llbe.png"),pygame.image.load("ooothis`ll.png"),
               pygame.image.load("beaah.png"),pygame.image.load("this`llbeabsolutlywee.png"),
               pygame.image.load("beaah.png"),pygame.image.load("ooothis`ll.png")]
for i, img in enumerate(framedcoins):
   framedcoins[i] = pygame.transform.scale(img, (coin_size,coin_size))

for coin in range (0,5):
    coin = pygame.rect.Rect( random.randint(0, width - coin_size),
                             random.randint(0, height - coin_size),
                             coin_size, coin_size)
    coins.append(coin)



da_c = 180
dash = 180

#eminie stuffffffff
enimy_size = 20
enimies = []
gp = 120
feet = 30
feeties = ":( + < 3"
enimiespeed = 4
for i in range (0,3):
    enimie = pygame.rect.Rect( random.randint(0, width - enimy_size),
                             random.randint(0, height - enimy_size),
                             enimy_size, enimy_size)
    enimies.append(enimie)
gamecontry = 0 #0 -> start,1 -> playing,-1 ->death
score = 0
speed = 5
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if gamecontry == 0:
        screen.fill((38, 250, 49))
        title_txt = font.render("funfunfunfunfunfun", True, (250, 250, 250))
        screen.blit(title_txt, (450, 100))

        startbutton =button(450,300,250,150, "start")
        startbutton.draw(screen, (250,0,100))

    if gamecontry == 1:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            pos_x -= speed
            if pos_x < 0:
                pos_x = 0
            elif keys[pygame.K_SPACE] and dash == da_c:
                pos_x -= 180
                dash = 0
        if keys[pygame.K_RIGHT]:
            pos_x += speed
            if pos_x > width - pw:
                pos_x = width - pw
            elif keys[pygame.K_SPACE] and dash == da_c:
                pos_x += 180
                dash = 0
        if keys[pygame.K_UP]:
            pos_y -= speed
            if pos_y < 0:
                pos_y = 0
            elif keys[pygame.K_SPACE] and dash == da_c:
                pos_y -= 180
                dash = 0
        if keys[pygame.K_DOWN]:
            pos_y += speed
            if pos_y > height - ph:
                pos_y = height - ph
            elif keys[pygame.K_SPACE] and dash == da_c:
                pos_y += 180
                dash = 0

        p_hit = pygame.rect.Rect(pos_x, pos_y, pw, ph)

        for coin in coins:
            if p_hit.colliderect(coin):
                feet = 60
                feeties = "+1"
                score += 1
                coin[0] = random.randint(0, width - coin_size)
                coin[1] = random.randint(0, height - coin_size)

            elif cra_z_coin:
                coin[0] += random.randint(-2500, 2500)
                if coin[0] < 0:
                    coin[0] = 0
                elif coin[0] > width - coin_size:
                    coin[0] = width - coin_size
                coin[1] += random.randint(-5, 5)
                if coin[1] < 0:
                    coin[1] = 0
                elif coin[1] > height - coin_size:
                    coin[1] = height - coin_size

        #...
        for enimy in enimies:
             if p_hit.colliderect(enimy) and gp ==0:
                 lives -=1
                 gp = 90
             moo_x = random.randint(1,10)
             moo_y = random.randint(1,10)
             if moo_x > 4:
                 enimy[0] += random.randint(-1,1)
             elif (pos_x - enimy[0]) !=0:
                 enimy[0] += enimiespeed*(pos_x - enimy[0])/abs(pos_x - enimy[0])
             if moo_y > 4:
                 enimy[1] += random.randint(-1, 1)
             elif (pos_y - enimy[1]) !=0:
                 enimy[1] += enimiespeed*(pos_y - enimy[1]) / abs(pos_y - enimy[1])


        screen.fill((38, 250, 49))
        pygame.draw.rect(screen, (100, 0, 250), (pos_x, pos_y, pw, ph))
        for coin in coins:

            screen.blit(framedcoins[currycoin//15], (coin[0], coin[1]))
        currycoin += 1
        currycoin = currycoin%90
        for enimy in enimies:
            pygame.draw.ellipse(screen, (100, 0, 50), enimy)

        s_txt = font.render("score:" + str(score), True, (250,250,250))
        screen.blit(s_txt, (30,30))
        s_txt = font.render("<3"*lives, True, (250, 0, 0))
        screen.blit(s_txt, (width-200, 30))

        if gp > 0:
            gp -= 1


        if dash < da_c:
            dash += 1
        if feet > 0:
            if (feet//10)%2 == 1:
                pickup = font.render(feeties, True, (200,250,0))
            else:
                pickup = font.render(feeties, True, (38, 250, 49))
            screen.blit(pickup, (pos_x , pos_y - 30))
            feet -= 1

    pygame.display.update()

    clock.tick(60)
pygame.quit()

