import pygame
import random 
from math import pi, sin, cos
 
BLACK = (0, 0, 0)
GREEN = (0, 255, 255)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WAGON_LENGTH = 10
WAGON_WIDTH = 20

class Trains(object):
    def __init__(self):
        self.length = random.randint(4, 25)
        self.light = [random.choice([True, False]) 
                    for x in range(self.length)]
        self.light[0] = True
        self.count = 0


def draw_trains():
    for i in range(len(coordinates)):
        if trains.light[i]:
            color = YELLOW
        else:
            color = BLACK
        pygame.draw.rect(screen, color,
        coordinates[i] + [WAGON_LENGTH, WAGON_WIDTH])

def wagon_center_coord(cur):
    return (coordinates[cur][0] + WAGON_LENGTH / 2, 
            coordinates[cur][1] + WAGON_WIDTH / 2)

pygame.init()
myfont = pygame.font.SysFont("monospace", 20)
size = [600, 600]
screen = pygame.display.set_mode(size)
screen.fill(WHITE)
pygame.display.set_caption("Trains count problem")
clock = pygame.time.Clock()

trains = Trains()
radius = trains.length*10
coordinates = [[int(size[0] // 2 + radius*cos(2*pi*i / trains.length)),
                int(size[0] // 2 + radius*sin(2*pi*i / trains.length))] 
                for i in range(trains.length)]

draw_trains()
pygame.display.flip()
count = 1
cur = 0

done = False
forward = True
last_loop = False
end = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
    
    clock.tick(8)
    screen.fill(WHITE)

    draw_trains()
    label = myfont.render("Counter: {0}".format(count + 1), 1, (0, 0, 0))
    screen.blit(label, (10, 10))
    label = myfont.render("Current: {0}".format(cur), 1, (0, 0, 0))
    screen.blit(label, (10, 40))
    if end:
        pygame.draw.circle(screen, GREEN, wagon_center_coord(cur) , 30, 3)
        pygame.display.flip()
        break
    else:
        pygame.draw.circle(screen, RED, wagon_center_coord(cur) , 30, 3)
    
    pygame.display.flip()

    if cur == trains.length - 1 and not last_loop and forward:
        cur = 0
        last_loop = True
        forward = False
        trains.light[cur] = False
        continue

    if forward:
        cur += 1
        if trains.light[cur] == True:
            trains.light[cur] = False
            forward = False
    elif cur == 0 and not last_loop:
        forward = True
    else:
        if last_loop and cur == 0: 
            cur = trains.length - 1
            trains.light[cur] = False 
        else: cur -= 1   
    
    if last_loop and cur == 0:
        end = True

    if cur > count:
        count = cur


done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

pygame.quit()