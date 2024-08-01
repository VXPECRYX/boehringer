import pygame
import sys
import math
import random

def anfang(screen):
    startscreen = pygame.image.load("startscreen.png")
    screen.blit(startscreen, (0, 0))
    pygame.display.update()

def load_cursor():
    cursor_surface = pygame.image.load('gun-pointer.png')
    cursor_surface_32x32 = pygame.transform.scale(cursor_surface, (32, 32))
    hotspot = (0, 0)  
    cursor = pygame.cursors.Cursor(hotspot, cursor_surface_32x32)
    pygame.mouse.set_cursor(cursor)
    pygame.display.flip()

def main():
    pygame.init()
    pygame.mixer.init()

    schiessen = pygame.mixer.Sound('shootsound.wav')

    width = 1600
    height = 1200
    x = 200
    y = 200
    speed = 2
    boost_speed = 5
    square_size = 20
    bullet_speed = 10
    wave = 0
    count = 0
    wars = 0.01
    lives = 4
    leben = 4
    boost = 100
    boost_max = 200
    boost_recharge_time = 2000  
    last_boost_time = 0
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Running")
    clock = pygame.time.Clock()
    pygame.font.init()
    bullets = []
    yellow_rects = []
    green_rects = []

    anfang(screen)
    load_cursor()

    def draw(x, y, angle):
        half_size = square_size / 2
        cos_angle = math.cos(angle)
        sin_angle = math.sin(angle)
        pygame.draw.rect(screen, (200, 200, 200), (x, y, 20, 20))
        for rect in yellow_rects:
            pygame.draw.rect(screen, (255, 255, 0), (rect[0], rect[1], 20, 20))
        for rect in green_rects:
            pygame.draw.rect(screen, (255, 0, 0), (rect[0], rect[1], 20, 20))
        points = [
            (x + half_size * cos_angle - (half_size/2) * sin_angle, y + half_size * sin_angle + (half_size/2) * cos_angle),
            (x - half_size * cos_angle - (half_size/2) * sin_angle, y - half_size * sin_angle + (half_size/2) * cos_angle),
            (x - half_size * cos_angle + (half_size/2) * sin_angle, y - half_size * sin_angle - (half_size/2) * cos_angle),
            (x + half_size * cos_angle + (half_size/2) * sin_angle, y + half_size * sin_angle - (half_size/2) * cos_angle)
        ]
        pygame.draw.polygon(screen, (255, 255, 0), points)
        
        img = pygame.image.load("gun-pointer.png")
        rekt1 = pygame.transform.scale(img, (32, 32))
        
        for rect in yellow_rects:
            pygame.draw.rect(screen, (255, 255, 0), (rect[0], rect[1], 20, 20))
            screen.blit(rekt1, (rect[0], rect[1]))
        

        boost_bar_length = 200
        boost_bar_height = 20
        boost_ratio = boost / boost_max
        boost_bar_color = (255 * (1 - boost_ratio), 255 * boost_ratio, 0)
        pygame.draw.rect(screen, boost_bar_color, (20, 20, boost_bar_length * boost_ratio, boost_bar_height))
        pygame.draw.rect(screen, (255, 255, 255), (20, 20, boost_bar_length, boost_bar_height), 2)
        
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

    def spawn_green_rect():
        start_x = random.randint(0, width)
        start_y = random.randint(0, height)
        green_rects.append([start_x, start_y])

    def check_collision(bullet, rect):
        bullet_rect = pygame.Rect(bullet[0], bullet[1], 5, 5)
        target_rect = pygame.Rect(rect[0], rect[1], 20, 20)
        return bullet_rect.colliderect(target_rect)

    def check_player_collision(player_x, player_y, rect):
        player_rect = pygame.Rect(player_x, player_y, 20, 20)
        target_rect = pygame.Rect(rect[0], rect[1], 20, 20)
        return player_rect.colliderect(target_rect)

    def endscreen(count):
        ende = pygame.image.load("endscreen.png")
        screen.blit(ende, (0, 0))
        pygame.display.update()
        with open("record.txt", "r") as file:
            rec = int(file.read().strip())
        if count > rec:
            print(count)
            with open("record.txt", "w") as file:
                file.write(str(count))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if 690 <= mouse_x <= 890 and 851 <= mouse_y <= 921:
                        pygame.quit()
                        sys.exit()
                    elif 690 <= mouse_x <= 890 and 651 <= mouse_y <= 721:
                        main()

    go = True
    ends = False
    while go:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                go = False
            if pygame.mouse.get_pressed()[0]:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                shoot_bullet(x, y, mouse_x, mouse_y)
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

        if keys[pygame.K_SPACE] and boost > 0:
            current_speed = boost_speed
            boost -= 1
            last_boost_time = pygame.time.get_ticks()
        else:
            current_speed = speed
            if boost < boost_max and pygame.time.get_ticks() - last_boost_time > boost_recharge_time:
                boost += 1

        if keys[pygame.K_a] and x - current_speed > 0:
            x -= current_speed
        if keys[pygame.K_d] and x + current_speed < width - square_size:
            x += current_speed
        if keys[pygame.K_w] and y - current_speed > 0:
            y -= current_speed
        if keys[pygame.K_s] and y + current_speed < height - square_size:
            y += current_speed

        for rect in yellow_rects:
            rect[0] = annähere_an_wert(rect[0], x, 1)
            rect[1] = annähere_an_wert(rect[1], y, 1)
        screen.fill((30, 30, 250))

        bullets_to_remove = []
        yellow_rects_to_remove = []
        green_rects_to_remove = []

        for bullet in bullets:
            bullet[0] += bullet[2]
            bullet[1] += bullet[3]
            if bullet[0] < 0 or bullet[0] > width or bullet[1] < 0 or bullet[1] > height:
                bullets_to_remove.append(bullet)
            else:
                collision_detected = False
                for rect in yellow_rects:
                    if check_collision(bullet, rect):
                        bullets_to_remove.append(bullet)
                        yellow_rects_to_remove.append(rect)
                        count += 1
                        collision_detected = True
                        break
                if not collision_detected:
                    for rect in green_rects:
                        if check_collision(bullet, rect):
                            bullets_to_remove.append(bullet)
                            green_rects_to_remove.append(rect)
                            lives += 1
                            if lives > leben:
                                lives = leben
                            break
                pygame.draw.circle(screen, (255, 0, 0), (int(bullet[0]), int(bullet[1])), 5)

        for bullet in bullets_to_remove:
            if bullet in bullets:
                bullets.remove(bullet)
        for rect in yellow_rects_to_remove:
            if rect in yellow_rects:
                yellow_rects.remove(rect)
        for rect in green_rects_to_remove:
            if rect in green_rects:
                green_rects.remove(rect)
        
        if count >= (wave + 1) * (20 + wave * 10):  
            wave += 1
            for _ in range(wave * 5): 
                spawn_yellow_rect()
            for _ in range(wave):  
                spawn_green_rect()

        for rect in yellow_rects:
            if check_player_collision(x, y, rect):
                lives -= 1
                yellow_rects.remove(rect)
                if lives <= 0:
                    ends = True
        if ends:
            endscreen(count)
            ends = False
        mouse_x, mouse_y = pygame.mouse.get_pos()
        angle = math.atan2(mouse_y - y, mouse_x - x)
        with open("record.txt", "r") as file:
            recsbl = int(file.read().strip())
        if recsbl <= count:
            recsbl = count
        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        text_surface = my_font.render('Wave: ' + str(wave), False, (255, 0, 0))
        text_surface1 = my_font.render('Count: ' + str(count), False, (255, 0, 0))
        text_surface2 = my_font.render('Record: ' + str(recsbl), False, (255, 0, 0))
        text_surface3 = my_font.render('Leben: ' + str(lives), False, (255, 0, 0))
        screen.blit(text_surface, (760, 20))
        screen.blit(text_surface1, (760, 50))
        screen.blit(text_surface2, (760, 80))
        screen.blit(text_surface3, (1410, 90))
        health_bar_length = 200
        health_bar_height = 20
        health_ratio = lives / leben
        health_bar_color = (255 * (1 - health_ratio), 255 * health_ratio, 0)
        pygame.draw.rect(screen, health_bar_color, (width - health_bar_length - 20, 20, health_bar_length * health_ratio, health_bar_height))
        draw(x, y, angle)

        if random.random() < wars:
            spawn_yellow_rect()
        elif random.random() < 0.00003:
            spawn_green_rect()



        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

def game_start():
    pygame.init()
    width = 1600
    height = 1200
    screen = pygame.display.set_mode((width, height))
    anfang(screen)

    start = False
    while not start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if 690 <= mouse_x <= 890 and 651 <= mouse_y <= 721:
                    main()
                elif 690 <= mouse_x <= 890 and 851 <= mouse_y <= 921:
                        pygame.quit()
                        sys.exit()



if __name__ == "__main__":
    game_start()