import pygame
import random
import json
import math

pygame.init()

WIDTH, HEIGHT = 1200, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ZOMBIE SURVIVAL")

clock = pygame.time.Clock()

FONT = pygame.font.SysFont("arial", 30)
BIG = pygame.font.SysFont("arial", 70)

SAVE_FILE = "data/save.json"

try:
    with open(SAVE_FILE) as f:
        highscore = json.load(f)["highscore"]
except:
    highscore = 0

player = pygame.Rect(WIDTH//2, HEIGHT//2, 40, 40)

health = 100
score = 0

zombies = []

spawn_timer = 0

WHITE=(255,255,255)
GREEN=(0,255,0)
RED=(255,0,0)
BG=(20,20,20)

running = True

while running:

    clock.tick(60)

    spawn_timer += 1

    if spawn_timer > 50:

        side = random.randint(0,3)

        if side == 0:
            x,y = random.randint(0,WIDTH),0
        elif side == 1:
            x,y = WIDTH,random.randint(0,HEIGHT)
        elif side == 2:
            x,y = random.randint(0,WIDTH),HEIGHT
        else:
            x,y = 0,random.randint(0,HEIGHT)

        zombies.append(
            pygame.Rect(x,y,35,35)
        )

        spawn_timer = 0

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player.y -= 5

    if keys[pygame.K_s]:
        player.y += 5

    if keys[pygame.K_a]:
        player.x -= 5

    if keys[pygame.K_d]:
        player.x += 5

    player.x = max(0,min(WIDTH-player.width,player.x))
    player.y = max(0,min(HEIGHT-player.height,player.y))

    for zombie in zombies[:]:

        dx = player.x - zombie.x
        dy = player.y - zombie.y

        dist = max(1, math.sqrt(dx*dx + dy*dy))

        zombie.x += int(dx/dist * 2)
        zombie.y += int(dy/dist * 2)

        if player.colliderect(zombie):

            health -= 1

            if health <= 0:

                if score > highscore:

                    with open(SAVE_FILE,"w") as f:
                        json.dump(
                            {"highscore":score},
                            f,
                            indent=4
                        )

                over = True

                while over:

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

                    pygame.display.flip()

                    for e in pygame.event.get():

                        if e.type == pygame.QUIT:
                            pygame.quit()
                            exit()

        score += 0.01

    screen.fill(BG)

    pygame.draw.rect(screen,GREEN,player)

    for zombie in zombies:
        pygame.draw.rect(screen,RED,zombie)

    screen.blit(
        FONT.render(
            f"Health: {health}",
            True,
            WHITE
        ),
        (20,20)
    )

    screen.blit(
        FONT.render(
            f"Score: {int(score)}",
            True,
            WHITE
        ),
        (20,60)
    )

    screen.blit(
        FONT.render(
            f"Best: {highscore}",
            True,
            WHITE
        ),
        (20,100)
    )

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
