import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Sprite Adventure")
clock = pygame.time.Clock()

BACKGROUND = (30, 30, 40)
WHITE = (255, 255, 255)
RED = (230, 60, 60)
GREEN = (60, 200, 90)
BLUE = (60, 120, 230)
YELLOW = (240, 210, 60)
ORANGE = (255, 140, 0)

sprite = pygame.Rect(375, 275, 50, 50)
speed = 5
sprite_color = ORANGE

solid_demo = pygame.Rect(40, 40, 80, 50)
outline_demo = pygame.Rect(140, 40, 80, 50)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        sprite.x -= speed
    if keys[pygame.K_RIGHT]:
        sprite.x += speed
    if keys[pygame.K_UP]:
        sprite.y -= speed
    if keys[pygame.K_DOWN]:
        sprite.y += speed

    sprite.x = max(0, min(sprite.x, WIDTH - sprite.width))
    sprite.y = max(0, min(sprite.y, HEIGHT - sprite.height))

    if sprite.left == 0:
        sprite_color = RED
    elif sprite.right == WIDTH:
        sprite_color = GREEN
    elif sprite.top == 0:
        sprite_color = BLUE
    elif sprite.bottom == HEIGHT:
        sprite_color = YELLOW

    screen.fill(BACKGROUND)
    pygame.draw.rect(screen, WHITE, solid_demo)
    pygame.draw.rect(screen, WHITE, outline_demo, 3)
    pygame.draw.rect(screen, sprite_color, sprite)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()