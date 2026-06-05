import pygame
import random
import json
import os

pygame.init()

WIDTH, HEIGHT = 1600, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Typing Shooter V3")

clock = pygame.time.Clock()

FONT = pygame.font.SysFont("arial", 36)
BIG_FONT = pygame.font.SysFont("arial", 80)

WORDS = [
    "python","linux","docker","network","server",
    "security","github","terminal","database",
    "socket","kernel","cyber","hacker","cloud",
    "machine","learning","algorithm","packet"
]

HIGH_FILE = "data/highscore.json"

if os.path.exists(HIGH_FILE):
    with open(HIGH_FILE) as f:
        highscore = json.load(f)["highscore"]
else:
    highscore = 0

score = 0
combo = 0
lives = 5

typed_text = ""
locked_enemy = None

spawn_timer = 0
spawn_rate = 100

class Star:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.speed = random.uniform(0.5, 2)

    def update(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = 0
            self.x = random.randint(0, WIDTH)

    def draw(self):
        pygame.draw.circle(screen, (100,100,150), (int(self.x), int(self.y)), 2)

stars = [Star() for _ in range(120)]

class Particle:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.dx=random.uniform(-4,4)
        self.dy=random.uniform(-4,4)
        self.life=30

    def update(self):
        self.x+=self.dx
        self.y+=self.dy
        self.life-=1

    def draw(self):
        pygame.draw.circle(
            screen,
            (0,255,255),
            (int(self.x),int(self.y)),
            3
        )

particles=[]

class EnemyWord:
    def __init__(self):
        self.word=random.choice(WORDS)
        self.x=random.randint(50,WIDTH-250)
        self.y=-50
        self.speed=random.uniform(1.5,3)

    def update(self):
        self.y+=self.speed

    def draw(self):

        color=(255,255,255)

        if self == locked_enemy:
            color=(255,0,255)

        text=FONT.render(self.word,True,color)
        screen.blit(text,(self.x,self.y))

enemies=[]

running=True

while running:

    clock.tick(60)

    spawn_timer += 1

    if spawn_timer >= spawn_rate:
        enemies.append(EnemyWord())
        spawn_timer = 0

        if spawn_rate > 30:
            spawn_rate -= 1

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running=False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_BACKSPACE:
                typed_text = typed_text[:-1]

            else:

                typed_text += event.unicode.lower()

                if locked_enemy is None:

                    for enemy in enemies:
                        if enemy.word.startswith(typed_text):
                            locked_enemy = enemy
                            break

                if locked_enemy:

                    if not locked_enemy.word.startswith(typed_text):
                        typed_text=""
                        locked_enemy=None
                        combo=0

                    elif typed_text == locked_enemy.word:

                        score += 100 + combo * 50
                        combo += 1

                        for _ in range(25):
                            particles.append(
                                Particle(
                                    locked_enemy.x+50,
                                    locked_enemy.y+20
                                )
                            )

                        enemies.remove(locked_enemy)

                        locked_enemy=None
                        typed_text=""

    for star in stars:
        star.update()

    for enemy in enemies[:]:

        enemy.update()

        if enemy.y > HEIGHT:

            enemies.remove(enemy)

            lives -= 1
            combo = 0

            if enemy == locked_enemy:
                locked_enemy = None
                typed_text = ""

    for p in particles[:]:
        p.update()

        if p.life <= 0:
            particles.remove(p)

    if score > highscore:
        highscore = score

    screen.fill((5,5,20))

    for star in stars:
        star.draw()

    for enemy in enemies:
        enemy.draw()

    for p in particles:
        p.draw()

    pygame.draw.rect(
        screen,
        (15,15,35),
        (0,HEIGHT-80,WIDTH,80)
    )

    screen.blit(
        FONT.render(f"Score: {score}",True,(0,255,100)),
        (20,20)
    )

    screen.blit(
        FONT.render(f"Best: {highscore}",True,(255,255,0)),
        (20,70)
    )

    screen.blit(
        FONT.render(f"Combo: {combo}",True,(255,100,255)),
        (20,120)
    )

    screen.blit(
        FONT.render(f"Lives: {lives}",True,(255,100,100)),
        (20,170)
    )

    screen.blit(
        FONT.render("> "+typed_text,True,(0,255,255)),
        (20,HEIGHT-60)
    )

    if lives <= 0:

        with open(HIGH_FILE,"w") as f:
            json.dump(
                {"highscore":highscore},
                f,
                indent=4
            )

        text = BIG_FONT.render(
            "GAME OVER",
            True,
            (255,0,0)
        )

        screen.blit(
            text,
            (
                WIDTH//2-text.get_width()//2,
                HEIGHT//2
            )
        )

        pygame.display.flip()
        pygame.time.wait(4000)

        running=False

    pygame.display.flip()

with open(HIGH_FILE,"w") as f:
    json.dump(
        {"highscore":highscore},
        f,
        indent=4
    )

pygame.quit()
