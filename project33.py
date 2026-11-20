import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wildlife Information Display")

background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

wildlife = pygame.image.load("wildlife.png")
wildlife = pygame.transform.scale(wildlife, (300, 300))
wildlife_pos = (WIDTH // 2 - 150, 150)

heading_font = pygame.font.Font(None, 56)
fact_font = pygame.font.Font(None, 32)

heading = heading_font.render("Wildlife Information Display", True, (255, 255, 255))
fact = fact_font.render("Fact: Elephants can recognize themselves in a mirror.", True, (255, 255, 255))

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    screen.blit(wildlife, wildlife_pos)
    screen.blit(heading, (WIDTH // 2 - heading.get_width() // 2, 40))
    screen.blit(fact, (WIDTH // 2 - fact.get_width() // 2, 500))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()