import pygame
import random
import time
from utils import load_image, check_collision
from menu import show_game_over

PLAYER_SPEED = 5
BULLET_SPEED = -7
ENEMY_SPEED = 2
ENEMY_BULLET_SPEED = 4

def start_game(screen):
    clock = pygame.time.Clock()
    width, height = screen.get_size()

    pygame.mixer.music.load("assets/music/music.mp3")
    pygame.mixer.music.play(-1)

    bravo_sound = pygame.mixer.Sound("assets/music/bravo.mp3")

    player_img = load_image("assets/player.png", (50, 50))
    enemy_img = load_image("assets/enemy.png", (40, 40))
    bullet_img = load_image("assets/bullet.png", (5, 20))

    player = pygame.Rect(width // 2 - 25, height - 60, 50, 50)
    bullets = []
    enemies = [pygame.Rect(random.randint(0, width - 40), random.randint(0, 150), 40, 40) for _ in range(6)]
    enemy_directions = [1 for _ in enemies]
    enemy_bullets = []

    score = 0
    last_bravo_score = 0
    font = pygame.font.Font(None, 36)
    message = ""
    message_timer = 0
    motivational_messages = [
        "¡Eres genial!",
        "¡Sigue disparando!",
        "¡Buen trabajo!",
        "¡No te detengas!",
        "¡Vas como un rayo!"
    ]

    enemy_fire_cooldown = 0
    running = True

    while running:
        screen.fill((10, 10, 30))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.left > 0:
            player.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] and player.right < width:
            player.x += PLAYER_SPEED
        if keys[pygame.K_SPACE]:
            if len(bullets) < 5:
                bullets.append(pygame.Rect(player.centerx - 2, player.top, 5, 20))

        for bullet in bullets[:]:
            bullet.y += BULLET_SPEED
            if bullet.bottom < 0:
                bullets.remove(bullet)

        for i, enemy in enumerate(enemies):
            enemy.x += ENEMY_SPEED * enemy_directions[i]
            if enemy.left <= 0 or enemy.right >= width:
                enemy_directions[i] *= -1
                enemy.y += 20
            if check_collision(enemy, player):
                pygame.mixer.music.stop()
                show_game_over(screen)
                return

        enemy_fire_cooldown += 1
        if enemy_fire_cooldown > 60:
            if enemies:
                shooter = random.choice(enemies)
                bullet = pygame.Rect(shooter.centerx, shooter.bottom, 5, 20)
                enemy_bullets.append(bullet)
            enemy_fire_cooldown = 0

        for bullet in enemy_bullets[:]:
            bullet.y += ENEMY_BULLET_SPEED
            if bullet.top > height:
                enemy_bullets.remove(bullet)
            elif bullet.colliderect(player):
                pygame.mixer.music.stop()
                show_game_over(screen)
                return

        for bullet in bullets[:]:
            for enemy in enemies[:]:
                if check_collision(bullet, enemy):
                    try:
                        bullets.remove(bullet)
                        enemies.remove(enemy)
                        enemies.append(pygame.Rect(random.randint(0, width - 40), random.randint(0, 100), 40, 40))
                        score += 10
                        message = random.choice(motivational_messages)
                        message_timer = time.time()
                        if score % 30 == 0 and score != last_bravo_score:
                            bravo_sound.play()
                            last_bravo_score = score
                    except ValueError:
                        pass

        screen.blit(player_img, player)
        for bullet in bullets:
            screen.blit(bullet_img, bullet)
        for bullet in enemy_bullets:
            pygame.draw.rect(screen, (255, 0, 0), bullet)
        for enemy in enemies:
            screen.blit(enemy_img, enemy)

        score_text = font.render(f"Puntos: {score}", True, (255, 255, 0))
        screen.blit(score_text, (10, 10))
        if message and time.time() - message_timer < 2:
            msg_surface = font.render(message, True, (0, 255, 0))
            screen.blit(msg_surface, (screen.get_width() // 2 - msg_surface.get_width() // 2, 50))

        pygame.display.flip()
        clock.tick(60)

    pygame.mixer.music.stop()
