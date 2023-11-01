import random

import pygame

largeur_ecran = 1280
hauteur_ecran = 720

pygame.init()
screen = pygame.display.set_mode((largeur_ecran, hauteur_ecran))
clock = pygame.time.Clock()
running = True
dt = 0
screen.fill("grey")
ORANGE = (255, 127, 0)

pos_x_object = 0
pos_y_object = 0
WIDTH_OBJECT = 70
HEIGHT_OBJECT = 50
FPS = 10
clock = pygame.time.Clock()
number_of_enemies = 10
number_of_target = 5
score = 0
object_list = []
other_object = []

i = 0

# Création de manière aléatoire et sans chevauchement des aires des rectangles
# Ils peuvent servir de support à l'insertion d'image ou d'autres éléments

while len(object_list) < number_of_enemies:
    object_creation_process = pygame.Rect(random.randint(0, largeur_ecran - WIDTH_OBJECT), 0, WIDTH_OBJECT,
                                          HEIGHT_OBJECT)
    not_colliding = True
    for obj in object_list:
        if obj.colliderect(object_creation_process):
            not_colliding = False
    if not_colliding:
        object_list.append(object_creation_process)

while len(other_object) < number_of_target:
    object_creation_process = pygame.Rect(random.randint(0, largeur_ecran - WIDTH_OBJECT), 0, WIDTH_OBJECT,
                                          HEIGHT_OBJECT)

assert len(object_list) == number_of_enemies, "La liste des rectangles est > 10"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for obj in object_list:
                if obj.collidepoint(event.pos):
                    object_list.remove(obj)
                    score += 200

    screen.fill("grey")

    for obj in object_list:
        pygame.draw.rect(screen, ORANGE, obj, 1)
        obj.y += 10
        obj.x += 4
        if obj.y > hauteur_ecran:
            object_list.remove(obj)
        if obj.x > largeur_ecran:
            object_list.remove(obj)
            score -= 50
    if len(object_list) == 0:
        pygame.quit()

    pos_y_object = pos_y_object + 10
    print("pos_y : ", pos_y_object)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()