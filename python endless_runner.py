import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Endless Runner")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player settings
player_width = 50
player_height = 50
player_x = 100
player_y = SCREEN_HEIGHT - player_height - 50
player_velocity = 10
player_jump = False
jump_count = 10

# Obstacle settings
obstacle_width = 50
obstacle_height = 50
obstacle_x = SCREEN_WIDTH
obstacle_y = SCREEN_HEIGHT - obstacle_height - 50
obstacle_velocity = 5

# Score
score = 0
font = pygame.font.SysFont("comicsans", 30)

# Clock
clock = pygame.time.Clock()

# Functions
def draw_player(x, y):
    pygame.draw.rect(screen, RED, (x, y, player_width, player_height))

def draw_obstacle(x, y):
    pygame.draw.rect(screen, BLACK, (x, y, obstacle_width, obstacle_height))

def display_score(score):
    text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(text, (10, 10))

def check_collision(player_x, player_y, obstacle_x, obstacle_y):
    if (player_x < obstacle_x + obstacle_width and
        player_x + player_width > obstacle_x and
        player_y < obstacle_y + obstacle_height and
        player_y + player_height > obstacle_y):
        return True
    return False

# Game loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not player_jump:
                player_jump = True

    # Player movement
    if player_jump:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            player_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            player_jump = False
            jump_count = 10

    # Obstacle movement
    obstacle_x -= obstacle_velocity
    if obstacle_x < 0:
        obstacle_x = SCREEN_WIDTH
        obstacle_y = SCREEN_HEIGHT - obstacle_height - 50
        score += 1

    # Collision detection
    if check_collision(player_x, player_y, obstacle_x, obstacle_y):
        print("Game Over! Final Score:", score)
        running = False

    # Draw player and obstacle
    draw_player(player_x, player_y)
    draw_obstacle(obstacle_x, obstacle_y)

    # Display score
    display_score(score)

    # Update display
    pygame.display.update()
    clock.tick(30)

pygame.quit()
