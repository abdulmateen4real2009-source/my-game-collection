import pygame
import random
import json

pygame.init()

WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("NEON RUNNER")

clock = pygame.time.Clock()

FONT = pygame.font.SysFont("consolas", 30)
BIG = pygame.font.SysFont("consolas", 70)

SAVE_FILE = "data/save.json"

try:
    with open(SAVE_FILE) as f:
        highscore = json.load(f)["highscore"]
except:
    highscore = 0

player = pygame.Rect(120, HEIGHT - 140, 50, 50)

gravity = 0
jumping = False

obstacles = []

score = 0
speed = 8

CYAN = (0,255,255)
PINK = (255,0,255)
GREEN = (0,255,120)
RED = (255,80,80)
BG = (5,5,15)

spawn_timer = 0

running = True

while running:

    clock.tick(60)

    spawn_timer += 1

    if spawn_timer > 60:
        obstacles.append(
            pygame.Rect(
                WIDTH,
                HEIGHT - 130,
                40,
                40
            )
        )
        spawn_timer = 0

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE and not jumping:
                gravity = -15
                jumping = True

    gravity += 0.8
    player.y += gravity

    if player.y >= HEIGHT - 140:
        player.y = HEIGHT - 140
        gravity = 0
        jumping = False

    for obstacle in obstacles[:]:

        obstacle.x -= speed

        if obstacle.right < 0:
            obstacles.remove(obstacle)
            score += 1

        if player.colliderect(obstacle):

            if score > highscore:
                highscore = score

                with open(SAVE_FILE,"w") as f:
                    json.dump(
                        {"highscore":highscore},
                        f,
                        indent=4
                    )

            game_over = True

            while game_over:

                screen.fill(BG)

                text = BIG.render(
                    "GAME OVER",
                    True,
                    RED
                )

                screen.blit(
                    text,
                    (
                        WIDTH//2-text.get_width()//2,
                        HEIGHT//2-50
                    )
                )

                screen.blit(
                    FONT.render(
                        f"Score: {score}",
                        True,
                        CYAN
                    ),
                    (
                        WIDTH//2-80,
                        HEIGHT//2+40
                    )
                )

                pygame.display.flip()

                for e in pygame.event.get():

                    if e.type == pygame.QUIT:
                        pygame.quit()
                        exit()

    if score > highscore:
        highscore = score

    if score % 20 == 0 and score > 0:
        speed = min(speed + 0.01, 18)

    screen.fill(BG)

    for y in range(0, HEIGHT, 40):
        pygame.draw.line(
            screen,
            (20,20,40),
            (0,y),
            (WIDTH,y)
        )

    pygame.draw.rect(screen,CYAN,player)

    for obstacle in obstacles:
        pygame.draw.rect(screen,PINK,obstacle)

    screen.blit(
        FONT.render(
            f"Score: {score}",
            True,
            GREEN
        ),
        (20,20)
    )

    screen.blit(
        FONT.render(
            f"Best: {highscore}",
            True,
            CYAN
        ),
        (20,60)
    )

    pygame.display.flip()

pygame.quit()
