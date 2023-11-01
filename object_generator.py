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
NOIR = (0,0,0)

pos_x_object = 0
pos_y_object = 0
WIDTH_OBJECT = 70
HEIGHT_OBJECT = 50
FPS = 30
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
    object_creation_process = pygame.Rect(random.randint(0, largeur_ecran - WIDTH_OBJECT), 0, WIDTH_OBJECT//2,
                                          HEIGHT_OBJECT//2)
    not_colliding_with_existing_object = True

    for obj in object_list:
        if obj.colliderect(object_creation_process):
            not_colliding_with_existing_object = False

    not_colliding = True

    if not_colliding_with_existing_object:
        for other in other_object:
            if other.colliderect(object_creation_process):
                not_colliding = False

    if not_colliding and not_colliding_with_existing_object:
        other_object.append(object_creation_process)


assert len(object_list) == number_of_enemies, "La liste des rectangles est différente de 10"
assert len(other_object) == number_of_target, "La liste des cibles est différente de 5"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for obj in object_list:
                if obj.collidepoint(event.pos):
                    object_list.remove(obj)
                    score += 200
            for other in other_object:
                if other.collidepoint(event.pos):
                    other_object.remove(other)
                    score += 200

    screen.fill("grey")

    for obj in object_list:
        pygame.draw.rect(screen, ORANGE, obj, 1)
        obj.y += (15/FPS)
        obj.x += (9/FPS)
        if obj.y > hauteur_ecran:
            object_list.remove(obj)
        if obj.x > largeur_ecran:
            object_list.remove(obj)
            score -= 50
    if len(object_list) == 0:
        pygame.quit()

    for other in other_object:
        pygame.draw.rect(screen, NOIR, other,1)
        other.y += (15/FPS)
        other.x += (9/FPS)

    pos_y_object = pos_y_object + 10
    print("pos_y : ", pos_y_object)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()