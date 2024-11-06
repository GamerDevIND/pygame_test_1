import pygame

pygame.init()
clock = pygame.time.Clock() # fps thing, can tick to whatever you want
dt = 0 # deltaTime
screen = pygame.display.set_mode((800, 600))
running = True

"""
player
"""
player_pos = pygame.Vector2(screen.get_width() / 2 , screen.get_height() / 2)
direction = pygame.Vector2(0,0)
speed = 300

# Main loop
while running:
    dt = clock.tick(60) / 1000 # initialize first so its not equals to 0 when we use it
    for event in pygame.event.get():
       if event.type == pygame.QUIT: # pygame.QUIT = cross on the top right corner
                running = False

    screen.fill((201,203,206)) # put some color in the background (grey)

    # draw rect
    pygame.draw.rect(screen, (90, 90, 90, 255), pygame.Rect(player_pos.x, player_pos.y, 150, 100))

    keys = pygame.key.get_pressed()

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