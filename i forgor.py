import pygame
import sys

# Initialize Pygame
pygame.init()



# Set up the window
screen_width = 800
screen_height = 600
window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Super Mario Bros")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load assets
ground_img = pygame.image.load("ground.png").convert()
mario_img = pygame.image.load("mario.png").convert()

# Scale assets
ground_img = pygame.transform.scale(ground_img, (screen_width, 50))
mario_img = pygame.transform.scale(mario_img, (50, 50))  # Assuming Mario is 50x50 pixels

# Define initial position for Mario
mario_x = 50
mario_y = screen_height - 100  # Place Mario above the ground
# Define level layout
level_layout = [
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "                               ",
    "               xxxxx           ",
    "                               ",
    "                               ",
    "      xxxxx                    ",
    "                               ",
    "                               ",
    "     xxxxx                     ",
    "                               ",
    "                               ",
    "    xxxxx                      ",
    "                               ",
    "                               ",
    "   xxxxx                       ",
    "                               ",
    "                               ",
    "  xxxxx                        ",
    "                               ",
    "                               ",
    " xxxxx                         ",
    "                               ",
    "                               ",
    "xxxxx                          ",
    "                               ",
    "==============================="
]

def draw_level(layout):
    # Define tile size
    tile_size = 50  # Adjust as needed

    # Draw level layout
    for y, row in enumerate(layout):
        for x, char in enumerate(row):
            if char == "x":
                window.blit(ground_img, ((x * tile_size) - camera_x, y * tile_size))

# Inside the main loop
# Draw level layout
camera_x = 0

# Main game loop
def main():
    # Initial camera position

    mario_x = 50
    mario_y = screen_height - 150  # Place Mario above the ground
    mario_x_speed = 0
    mario_y_speed = 0
    mario_x = 50
    gravity = 0.5  # Adjust as needed
    jump_strength = -10  # Adjust as needed
    while True:
        draw_level(level_layout)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Apply gravity
        mario_y_speed += gravity

        # Check for collisions with ground
        if mario_y + mario_y_speed > screen_height - 100:
            mario_y_speed = 0
            mario_y = screen_height - 100
            # Reset jump
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                mario_y_speed = jump_strength

        # Handle horizontal movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            mario_x_speed = -5  # Adjust speed as needed
        elif keys[pygame.K_RIGHT]:
            mario_x_speed = 5  # Adjust speed as needed
        else:
            mario_x_speed = 0

        # Update Mario's position
        mario_x += mario_x_speed
        mario_y += mario_y_speed

        # Update camera position to follow Mario horizontally
        camera_x = max(0, mario_x - screen_width // 2)  # Center camera on Mario

        # Clear the screen
        window.fill(BLACK)

        # Draw ground tiles
        ground_tile_width = ground_img.get_width()
        for i in range(screen_width // ground_tile_width + 1):
            window.blit(ground_img, (i * ground_tile_width - camera_x, screen_height - 50))

        # Draw Mario
        window.blit(mario_img, (mario_x - camera_x, mario_y))

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        pygame.time.Clock().tick(60)  # Adjust as needed





# Run the game
if __name__ == "__main__":
    main()
