import pygame
from menu import show_main_menu
from game import start_game

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Space Invaders")

    while True:
        action = show_main_menu(screen)
        if action == "start":
            start_game(screen)
        elif action == "quit":
            break

    pygame.quit()

if __name__ == "__main__":
    main()
