import pygame
import sys
import random

pygame.init()


screen = pygame.display.set_mode((1600, 1200))
pygame.display.set_caption("Hello World")


player_pos = [200, 200]
player_size = 20

speed = 5


yellow_blocks = []
block_size = 20


SPAWN_YELLOW_BLOCK = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_YELLOW_BLOCK, 5000)


running = True
clock = pygame.time.Clock()

def spawn_yellow_block():
    x = random.randint(0, screen.get_width() - block_size)
    y = random.randint(0, screen.get_height() - block_size)
    yellow_blocks.append(pygame.Rect(x, y, block_size, block_size))

def move_player(keys, player_pos):
    if keys[pygame.K_a]:
        player_pos[0] -= speed
    if keys[pygame.K_d]:
        player_pos[0] += speed
    if keys[pygame.K_w]:
        player_pos[1] -= speed
    if keys[pygame.K_s]:
        player_pos[1] += speed

    
    player_pos[0] = max(0, min(player_pos[0], screen.get_width() - player_size))
    player_pos[1] = max(0, min(player_pos[1], screen.get_height() - player_size))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == SPAWN_YELLOW_BLOCK:
            spawn_yellow_block()

    
    keys = pygame.key.get_pressed()
    move_player(keys, player_pos)

    
    screen.fill((0, 0, 0))
    player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size, player_size)
    pygame.draw.rect(screen, (200, 200, 200), player_rect)

    for block in yellow_blocks:
        pygame.draw.rect(screen, (255, 255, 0), block)
        if player_rect.colliderect(block):
            speed += 2
            yellow_blocks.remove(block)  
            
    pygame.display.flip()
    clock.tick(60)  

pygame.quit()
sys.exit()
