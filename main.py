import pygame
import sys
import math
import random
from time import sleep

BLACK = ((0, 0, 0))
RED = ((255, 0, 0))
GREEN = ((0, 255, 0))
WHITE = ((255, 255, 255))

pygame.init()
pygame.font.init()
pygame.mixer.init()

# Basics
backgroundmusic = pygame.mixer.music.load(
    r'C:\Users\baeja\Documents\Python Scripts\cargame\assets\backgroundmusic.mp3')
pygame.mixer.music.play(-1)

icon = pygame.image.load(
    r'C:\Users\baeja\Documents\Python Scripts\cargame\assets\prof.png')
screenx = 800
screeny = 600
screen = pygame.display.set_mode((screenx, screeny))
pygame.display.set_icon(icon)

# Img files

PLAYER = pygame.image.load(
    r'C:\Users\baeja\Documents\Python Scripts\cargame\assets\CAR.png')
ROAD = pygame.image.load(
    r"C:\Users\baeja\Documents\Python Scripts\cargame\assets\road.png")
EXPLOSION = pygame.image.load(
    r'C:\Users\baeja\Documents\Python Scripts\cargame\assets\explosion.png')
ROCK = pygame.image.load(
    r'C:\Users\baeja\Documents\Python Scripts\cargame\assets\rock.png')
ROCK2 = pygame.image.load(
    r'C:\Users\baeja\Documents\Python Scripts\cargame\assets\rock2.png'
)
ROCK3 = pygame.image.load(
    r'C:\Users\baeja\Documents\Python Scripts\cargame\assets\rock3.png'
)
FOREST = pygame.image.load(
    r'C:\Users\baeja\Documents\Python Scripts\cargame\assets\forest.png')

# TODO: hit count 시스템 만들고 label 추가해서 게임 오버 그런거 만들고 화면 오른쪽 상단에 datetime 써서 시간 표시하는거 만들기, 그리고 방해물 더 만들기 

# Object variable

player_x = 400
player_y = 500
gameover = False
speed = 1.5
rockx = random.randint(70, 550)
rocky = 0
rock2x = random.randint(70, 550)
rock2y = 0
rock3x = random.randint(70, 550)
rock3y = 0
objectspeed = 2
HitCount = 0
MaxHitCount = 3

# Main func


def main():
    global player_x, player_y, rockx, rocky, gameover, objectspeed, rock2x, rock2y, rock3x, rock3y, HitCount, MaxHitCount
    while True:
        # mainloop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                x, y = pygame.mouse.get_pos()
                pygame.display.set_caption(f"Mouse at ({x}, {y})")

        # image loading
        load_image(FOREST, 0, 0)
        load_image(ROAD, 90, 0)
        load_image(PLAYER, player_x, player_y)
        load_image(ROCK, rockx, rocky)
        load_image(ROCK2, rock2x, rock2y)
        load_image(ROCK3, rock3x, rock3y)

        # Player movement
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and player_x >= 87:
            player_x -= speed
        if keys[pygame.K_RIGHT] and player_x <= 670:
            player_x += speed
        if keys[pygame.K_UP] and player_y >= 0:
            player_y -= speed
        if keys[pygame.K_DOWN] and player_y <= 520:
            player_y += speed

        # Check collosion
        if isCollision(rockx, rocky, player_x, player_y):
            load_image(EXPLOSION, player_x - 50, player_y)
            explosionmusic = pygame.mixer.Sound(
                r'C:\Users\baeja\Documents\Python Scripts\cargame\assets\Explosion.wav')
            explosionmusic.play()
            rocky = -500
            rockx = random.randint(140, 615)

        if isCollision(rock2x, rock2y, player_x, player_y):
            load_image(EXPLOSION, player_x - 50, player_y)
            explosionmusic = pygame.mixer.Sound(
                r'C:\Users\baeja\Documents\Python Scripts\cargame\assets\Explosion.wav')
            explosionmusic.play()
            rock2y = -300
            rock2x = random.randint(140, 615)

        if isCollision(rock3x, rock3y, player_x, player_y):
            load_image(EXPLOSION, player_x - 50, player_y)
            explosionmusic = pygame.mixer.Sound(
                r'C:\Users\baeja\Documents\Python Scripts\cargame\assets\Explosion.wav')
            explosionmusic.play()
            rock3y = -400
            rock3x = random.randint(140, 615)

        # Rock movement
        if gameover != True:
            rocky += objectspeed
            rock2y += objectspeed
            rock3y += objectspeed
            if rocky >= 547:
                rocky = -500
                rockx = random.randint(140, 615)
            if rock2y >= 547:
                rock2y = -300
                rock2x = random.randint(140, 615)
            if rock3y >= 547:
                rock3y = -400
                rock3x = random.randint(140, 615)

        pygame.display.update()

    pygame.quit()

# Helper func


def load_image(img, x, y):
    screen.blit(img, (math.ceil(x), math.ceil(y)))


def isCollision(rockx, rocky, player_x, player_y):
    distance = math.sqrt((math.pow(rockx - player_x, 2)) +
                         (math.pow(rocky-player_y, 2)))
    if distance < 55:
        return True
        sleep(1)
    else:
        return False


if __name__ == "__main__":
    main()