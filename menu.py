import pygame
import sys

FONT = None

def show_text_centered(screen, text, y, size=40, color=(255, 255, 255)):
    global FONT
    if FONT is None or FONT.get_height() != size:
        FONT = pygame.font.Font(None, size)
    rendered = FONT.render(text, True, color)
    rect = rendered.get_rect(center=(screen.get_width() // 2, y))
    screen.blit(rendered, rect)

def show_main_menu(screen):
    clock = pygame.time.Clock()
    while True:
        screen.fill((0, 0, 30))
        show_text_centered(screen, "SPACE INVADERS", 200, 60)
        show_text_centered(screen, "Presiona [ENTER] para jugar", 300)
        show_text_centered(screen, "Presiona [ESC] para salir", 350)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return "start"
                if event.key == pygame.K_ESCAPE:
                    return "quit"
        clock.tick(60)

def show_game_over(screen):
    screen.fill((30, 0, 0))
    show_text_centered(screen, "¡Game Over!", 250, 60)
    show_text_centered(screen, "Presiona [ENTER] para volver al menú", 320)
    pygame.display.flip()
    wait_for_enter()

def wait_for_enter():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return
