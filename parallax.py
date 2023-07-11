import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple Scrolling Backgrounds")

# Set up game variables
player_x = screen_width // 2
player_y = screen_height - 50
player_speed = 5

# Define the platform positions and speeds
rect1 = pygame.Rect(50, screen_height - 100, 200, 10)
rect2 = pygame.Rect(screen_width - 250, screen_height - 200, 200, 10)
platforms = [
    {"rect": rect1, "speed": 3},
    {"rect": rect2, "speed": 1}
]

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
        for platform in platforms:
            platform["rect"].x -=  platform["speed"]
    if keys[pygame.K_RIGHT] and player_x < screen_width:
        player_x += player_speed
        for platform in platforms:
            platform["rect"].x +=  platform["speed"]


    # Render the game objects
    screen.fill((0, 0, 0))

    player = pygame.Rect(player_x, player_y, 20, 20)
    pygame.draw.rect(screen, (255, 255, 255), player)

    for platform in platforms:
        pygame.draw.rect(screen, (0, 255, 0), platform["rect"])

    pygame.display.flip()

# Clean up
pygame.quit()
