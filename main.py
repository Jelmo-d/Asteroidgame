# main.py
import pygame
from constants import * # Import all constants from constants.py

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize Pygame
    pygame.init()

    # Get a new GUI window (the game screen)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game Loop
    while True:
        # Step 1: Check for player inputs (and window close)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return # Exit the main function, which quits the game

        # Step 2: Update the game world (we'll add this later)
        # For now, there are no game objects to update

        # Step 3: Draw the game to the screen
        screen.fill((0, 0, 0)) # Fill the screen with black (RGB values)
        pygame.display.flip()  # Refresh the entire screen (make changes visible)

# This ensures the main() function is only called when this file is run directly
if __name__ == "__main__":
    main()