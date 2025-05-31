import pygame

def load_image(path, scale=None):
    image = pygame.image.load(path).convert_alpha()
    if scale:
        image = pygame.transform.scale(image, scale)
    return image

def check_collision(obj1, obj2):
    return obj1.colliderect(obj2)
