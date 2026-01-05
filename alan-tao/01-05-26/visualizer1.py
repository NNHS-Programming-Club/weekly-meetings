import pygame
import random
import sys
import time

# ---------------- CONFIG ----------------
LEN = 5
SIMULATIONS = 5

WIDTH, HEIGHT = 900, 400
HOLE_RADIUS = 30
FPS = 60

PAUSE_TIME = 0.6  # seconds between steps

# Colors
BG = (30, 30, 30)
HOLE = (200, 200, 200)
GUESS = (220, 60, 60)
HOG = (160, 100, 40)
TEXT = (255, 255, 255)
BUTTON = (70, 70, 70)

# ---------------------------------------
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Groundhog Strategy Simulator")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)

# Hole positions
spacing = WIDTH // (LEN + 1)
holes = [(spacing * (i + 1), HEIGHT // 2) for i in range(LEN)]

# Buttons
start_button = pygame.Rect(50, 330, 120, 40)
reset_button = pygame.Rect(200, 330, 120, 40)

# Game state
guesses = []
running_sim = False
current_sim = 0
current_guess = -1
caught = 0
escape = 0
pos = None
show_guess = None
phase = "input"  # input, guess, move, done
last_time = 0
escaped = False


def move_groundhog(pos):
    if pos == 1:
        return 2
    elif pos == LEN:
        return LEN - 1
    return pos + random.choice([-1, 1])


def clicked_hole(mouse):
    mx, my = mouse
    for i, (x, y) in enumerate(holes, start=1):
        if (mx - x) ** 2 + (my - y) ** 2 <= HOLE_RADIUS**2:
            return i
    return None


def reset_game():
    global guesses, running_sim, current_sim, current_guess, caught, escape
    global pos, show_guess, phase, escaped
    guesses = []
    running_sim = False
    current_sim = 0
    current_guess = -1
    caught = 0
    escape = 0
    pos = None
    show_guess = None
    phase = "input"
    escaped = False


# ---------------- MAIN LOOP ----------------
while True:
    clock.tick(FPS)
    screen.fill(BG)

    now = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if phase == "input":
                hole = clicked_hole(event.pos)
                if hole:
                    guesses.append(hole)

                if start_button.collidepoint(event.pos) and guesses:
                    running_sim = True
                    phase = "guess"
                    current_sim = 1
                    current_guess = 0
                    pos = random.randint(1, LEN)
                    last_time = now

            if reset_button.collidepoint(event.pos):
                reset_game()

    # ---------------- SIMULATION LOGIC ----------------
    if running_sim:
        if phase == "guess" and now - last_time > PAUSE_TIME:
            if current_guess < len(guesses):
                show_guess = guesses[current_guess]
                last_time = now

                if show_guess == pos:
                    caught += 1
                    phase = "done"
                else:
                    phase = "move"
            else:
                escape += 1
                phase = "done"

        elif phase == "move" and now - last_time > PAUSE_TIME:
            show_guess = None
            pos = move_groundhog(pos)
            current_guess += 1
            phase = "guess"
            last_time = now

        elif phase == "done" and now - last_time > PAUSE_TIME:
            if current_sim < SIMULATIONS:
                current_sim += 1
                current_guess = 0
                pos = random.randint(1, LEN)
                show_guess = None
                phase = "guess"
                last_time = now
            else:
                running_sim = False

    # ---------------- DRAWING ----------------
    # Draw holes
    for i, (x, y) in enumerate(holes, start=1):
        pygame.draw.circle(screen, HOLE, (x, y), HOLE_RADIUS, 2)

        if show_guess == i:
            pygame.draw.circle(screen, GUESS, (x, y), HOLE_RADIUS, 4)

        if pos == i and running_sim:
            pygame.draw.circle(screen, HOG, (x, y), HOLE_RADIUS - 8)

    # Buttons
    pygame.draw.rect(screen, BUTTON, start_button)
    pygame.draw.rect(screen, BUTTON, reset_button)

    screen.blit(font.render("Start", True, TEXT), (80, 338))
    screen.blit(font.render("Reset", True, TEXT), (230, 338))

    # Text info
    if phase == "input":
        msg = "Click holes to set guesses"
    elif running_sim:
        msg = f"Simulation {current_sim}/{SIMULATIONS}"
    else:
        msg = f"Caught: {caught}; Escaped: {escape}"

    screen.blit(font.render(msg, True, TEXT), (WIDTH // 2 - 100, 30))

    screen.blit(font.render(f"Guesses: {guesses}", True, TEXT), (WIDTH // 2 - 150, 70))

    pygame.display.flip()
