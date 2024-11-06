import pygame

pygame.init()
clock = pygame.time.Clock()
dt = 0
screen = pygame.display.set_mode((800, 600))
running = True

"""
player
"""
player_pos = pygame.Vector2(screen.get_width() / 2 , screen.get_height() / 2)
direction = pygame.Vector2(0,0)
speed = 300


while running:
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
       if event.type == pygame.QUIT: # pygame.QUIT = croix en faut de la fenêtre
                running = False

    screen.fill((201,203,206))

    pygame.draw.rect(screen, (90, 90, 90, 255), pygame.Rect(player_pos.x, player_pos.y, 150, 100))

    keys = pygame.key.get_pressed()
    direction = pygame.Vector2()

    if keys[pygame.K_z]:
        direction.y -= 1
    if keys[pygame.K_s]:
        direction.y += 1
    if keys[pygame.K_q]:
        direction.x -= 1
    if keys[pygame.K_d]:
        direction.x += 1

    if direction != pygame.Vector2():
        direction.normalize_ip()
        player_pos += direction * dt * speed


    pygame.display.flip()
pygame.quit()