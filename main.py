import random

import pygame

pygame.init()
clock = pygame.time.Clock() # fps thing, can tick to whatever you want
dt = 0 # deltaTime
screen = pygame.display.set_mode((800, 600))
running = True

"""
PLAYER
"""
player_pos = pygame.Vector2(screen.get_width() / 2 , screen.get_height() / 2)
direction = pygame.Vector2(0,0)
speed = 300

"""
MOVING CIRCLE
"""
circle_position = pygame.Vector2() # init circle at (0,0)
circle_movement = pygame.Vector2(1,1) # init circle movement at (1,1)

# Main loop
while running:
    dt = clock.tick(60) / 1000 # initialize first so its not equals to 0 when we use it
    for event in pygame.event.get():
       if event.type == pygame.QUIT: # pygame.QUIT = cross on the top right corner
                running = False

    screen.fill((201,203,206)) # put some color in the background (grey)

    # draw rect
    rect = pygame.draw.rect(screen, (90, 90, 90, 255), pygame.Rect(player_pos.x, player_pos.y, 150, 100))

    if pygame.mouse.get_pressed()[0]:
        rect = pygame.draw.rect(screen, (10, 10, 10, 255), pygame.Rect(player_pos.x, player_pos.y, 150, 100))

    pygame.draw.circle(screen, (255,255,255), circle_position, 15)

    circle_position.x += circle_movement.x * speed * dt
    circle_position.y += circle_movement.y * speed * dt

    if circle_position.x > screen.get_width() or circle_position.x < 0:
        circle_movement.x *= -1
    if circle_position.y > screen.get_height() or circle_position.y < 0:
        circle_movement.y *= -1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False

    # set direction to a new vector2, it should be equal to (0,0)
    direction = pygame.Vector2()

    if keys[pygame.K_z]:
        direction.y -= 1
    if keys[pygame.K_s]:
        direction.y += 1
    if keys[pygame.K_q]:
        direction.x -= 1
    if keys[pygame.K_d]:
        direction.x += 1

    # if direction is not (0,0)
    if direction != pygame.Vector2():
        direction.normalize_ip() # normalize so it has a constant speed
        player_pos += direction * dt * speed # add deltaTime and speed


    pygame.display.flip()
pygame.quit()