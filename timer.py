import time


def countdown(seconds):
    while seconds > 0:
        print(f"{seconds}...")
        time.sleep(1)
        seconds -= 1
    print("Zeit ist um!")

countdown(5)

import pygame
import sys
import math
import random

pygame.init()

width = 1600
height = 1200
x = 200
y = 200
speed = 2
square_size = 20
bullet_speed = 10
wave = 0
count = 0
wars = 0.01

jet = True

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Running")
clock = pygame.time.Clock()

pygame.font.init()

bullets = []
yellow_rects = []

def draw(x, y, angle):
    half_size = square_size / 2
    cos_angle = math.cos(angle)
    sin_angle = math.sin(angle)

    pygame.draw.rect(screen, (200, 200, 200), (x, y, 20, 20))

    for rect in yellow_rects:
        pygame.draw.rect(screen, (255, 255, 0), (rect[0], rect[1], 20, 20))

    points = [
        (x + half_size * cos_angle - (half_size/2) * sin_angle, y + half_size * sin_angle + (half_size/2) * cos_angle),
        (x - half_size * cos_angle - (half_size/2) * sin_angle, y - half_size * sin_angle + (half_size/2) * cos_angle),
        (x - half_size * cos_angle + (half_size/2) * sin_angle, y - half_size * sin_angle - (half_size/2) * cos_angle),
        (x + half_size * cos_angle + (half_size/2) * sin_angle, y + half_size * sin_angle - (half_size/2) * cos_angle)
    ]
    
    pygame.draw.polygon(screen, (255, 255, 0), points)
    pygame.display.flip()

def annähere_an_wert(aktueller_wert, zielwert, schritt):
    if aktueller_wert < zielwert:
        aktueller_wert += schritt
    elif aktueller_wert > zielwert:
        aktueller_wert -= schritt
    return aktueller_wert

def shoot_bullet(x, y, target_x, target_y):
    angle = math.atan2(target_y - y, target_x - x)
    bullet_dx = bullet_speed * math.cos(angle)
    bullet_dy = bullet_speed * math.sin(angle)
    bullets.append([x, y, bullet_dx, bullet_dy])

def spawn_yellow_rect():
    start_x = random.randint(0, width)
    start_y = random.randint(0, height)
    yellow_rects.append([start_x, start_y])

def check_collision(bullet, rect):
    bullet_rect = pygame.Rect(bullet[0], bullet[1], 5, 5)
    yellow_rect = pygame.Rect(rect[0], rect[1], 20, 20)
    return bullet_rect.colliderect(yellow_rect)

def check_player_collision(player_x, player_y, rect):
    player_rect = pygame.Rect(player_x, player_y, 20, 20)
    yellow_rect = pygame.Rect(rect[0], rect[1], 20, 20)
    return player_rect.colliderect(yellow_rect)

def endscreen():
    ende = pygame.image.load("endscreen.png")
    screen.blit(ende, (0, 0))
    jet = False
    pygame.display.update()

go = True

while go:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go = False
        if pygame.mouse.get_pressed()[0]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            shoot_bullet(x, y, mouse_x, mouse_y)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        x -= speed
    if keys[pygame.K_d]:
        x += speed
    if keys[pygame.K_w]:
        y -= speed
    if keys[pygame.K_s]:
        y += speed

    for rect in yellow_rects:
        rect[0] = annähere_an_wert(rect[0], x, 1)
        rect[1] = annähere_an_wert(rect[1], y, 1)

    screen.fill((0, 0, 0)) 

    for bullet in bullets[:]:
        bullet[0] += bullet[2]
        bullet[1] += bullet[3]
        if bullet[0] < 0 or bullet[0] > width or bullet[1] < 0 or bullet[1] > height:
            bullets.remove(bullet)
        else:
            for rect in yellow_rects[:]:
                if check_collision(bullet, rect):
                    bullets.remove(bullet)
                    yellow_rects.remove(rect)
                    count += 1
                    
            else:
                pygame.draw.circle(screen, (255, 0, 0), (int(bullet[0]), int(bullet[1])), 5)

#-----------------------------------------------------------------------------------------------#
#WAVE
    if count == 30:
        wave += 1
    if count == 100:
        wave += 1
    if count == 300:
        wave += 1
    if count == 700:
        wave += 1
    if count == 1400:
        wave += 1
    if count == 3000:
        wave += 1
#-------------------------------------------------------------------------------------------------#
#Count#
    if wave == 1:
        wars = 0.1
    if wave == 2:
        wars = 0.15
    if wave == 2:
        wars = 0.2
    if wave == 3:
        wars = 0.25
    if wave == 4:
        wars = 0.3
    if wave == 5:
        wars = 0.35
#-----------------------------------------------------------------------------------------------------#

    for rect in yellow_rects:
        if check_player_collision(x, y, rect):
            endscreen()

    mouse_x, mouse_y = pygame.mouse.get_pos()
    angle = math.atan2(mouse_y - y, mouse_x - x)

    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    text_surface = my_font.render('Wave: ' + str(wave) , False, (255, 0, 0))
    text_surface1 = my_font.render('Count: ' + str(count) , False, (255, 0, 0))
    screen.blit(text_surface, (760,20))
    screen.blit(text_surface1, (760, 50))

    while jet:
        draw(x, y, angle)

    if random.random() < wars: 
        spawn_yellow_rect()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
