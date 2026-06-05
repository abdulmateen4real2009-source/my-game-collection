import pygame
import random

pygame.init()

WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Typing Shooter V2")

clock = pygame.time.Clock()

FONT = pygame.font.SysFont("arial", 36)
BIG_FONT = pygame.font.SysFont("arial", 72)

WORDS = [
    "python",
    "linux",
    "network",
    "cyber",
    "hacker",
    "nexara",
    "server",
    "database",
    "terminal",
    "cloud",
    "socket",
    "github",
    "docker",
    "kernel",
    "security",
]

score = 0
combo = 0
lives = 5

typed_text = ""

spawn_rate = 120
spawn_timer = 0

class EnemyWord:
    def __init__(self):
        self.word = random.choice(WORDS)
        self.x = random.randint(50, WIDTH - 250)
        self.y = -50
        self.speed = random.uniform(1.5, 3)

    def update(self):
        self.y += self.speed

    def draw(self):
        color = (255, 255, 255)

        if self.word.startswith(typed_text) and typed_text != "":
            color = (0, 255, 255)

        text = FONT.render(self.word, True, color)
        screen.blit(text, (self.x, self.y))

enemies = []

running = True

while running:

    clock.tick(60)

    spawn_timer += 1

    if spawn_timer >= spawn_rate:
        enemies.append(EnemyWord())
        spawn_timer = 0

        if spawn_rate > 35:
            spawn_rate -= 1

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_BACKSPACE:
                typed_text = typed_text[:-1]

            else:

                typed_text += event.unicode.lower()

                matched_prefix = False

                for enemy in enemies:
                    if enemy.word.startswith(typed_text):
                        matched_prefix = True
                        break

                if not matched_prefix:
                    typed_text = ""
                    combo = 0

                for enemy in enemies[:]:

                    if typed_text == enemy.word:

                        enemies.remove(enemy)

                        combo += 1
                        score += 100 * combo

                        typed_text = ""

                        break

    screen.fill((5, 5, 20))

    for enemy in enemies[:]:

        enemy.update()
        enemy.draw()

        if enemy.y > HEIGHT:

            enemies.remove(enemy)

            lives -= 1
            combo = 0

    score_text = FONT.render(
        f"Score: {score}",
        True,
        (0, 255, 0),
    )

    combo_text = FONT.render(
        f"Combo: {combo}",
        True,
        (255, 255, 0),
    )

    lives_text = FONT.render(
        f"Lives: {lives}",
        True,
        (255, 100, 100),
    )

    input_text = FONT.render(
        f"> {typed_text}",
        True,
        (0, 200, 255),
    )

    screen.blit(score_text, (20, 20))
    screen.blit(combo_text, (20, 70))
    screen.blit(lives_text, (20, 120))

    pygame.draw.rect(
        screen,
        (20, 20, 40),
        (0, HEIGHT - 80, WIDTH, 80)
    )

    screen.blit(input_text, (20, HEIGHT - 60))

    if lives <= 0:

        over = BIG_FONT.render(
            "GAME OVER",
            True,
            (255, 0, 0),
        )

        screen.blit(
            over,
            (
                WIDTH // 2 - over.get_width() // 2,
                HEIGHT // 2,
            ),
        )

        pygame.display.flip()
        pygame.time.wait(4000)

        running = False

    pygame.display.flip()

pygame.quit()
