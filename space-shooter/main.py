import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 50, 50)
GREEN = (50, 255, 50)

clock = pygame.time.Clock()

player = pygame.Rect(375, 500, 50, 50)

bullets = []
enemies = []

score = 0

font = pygame.font.SysFont(None, 36)

for _ in range(5):
    enemies.append(
        pygame.Rect(
            random.randint(0, WIDTH - 40),
            random.randint(-300, -40),
            40,
            40
        )
    )

running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(
                    pygame.Rect(
                        player.x + 22,
                        player.y,
                        5,
                        15
                    )
                )

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= 5

    if keys[pygame.K_RIGHT]:
        player.x += 5

    screen.fill(BLACK)

    pygame.draw.rect(screen, GREEN, player)

    for bullet in bullets[:]:
        bullet.y -= 8

        if bullet.y < 0:
            bullets.remove(bullet)
        else:
            pygame.draw.rect(screen, WHITE, bullet)

    for enemy in enemies:
        enemy.y += 3

        if enemy.y > HEIGHT:
            enemy.y = random.randint(-200, -40)
            enemy.x = random.randint(0, WIDTH - 40)

        pygame.draw.rect(screen, RED, enemy)

        if enemy.colliderect(player):
            running = False

        for bullet in bullets[:]:
            if enemy.colliderect(bullet):
                score += 1

                enemy.y = random.randint(-200, -40)
                enemy.x = random.randint(0, WIDTH - 40)

                if bullet in bullets:
                    bullets.remove(bullet)

    text = font.render(
        f"Score: {score}",
        True,
        WHITE
    )

    screen.blit(text, (10, 10))

    pygame.display.flip()

pygame.quit()
