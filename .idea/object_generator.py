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
NOIR = (0, 0, 0)
BLEU = (0, 0, 255)
INDIGO = (75,0,130)

pos_x_object = 0
pos_y_object = 0
WIDTH_OBJECT = 70
HEIGHT_OBJECT = 50
FPS = 30
clock = pygame.time.Clock()
number_of_enemies = 8
number_of_target = 5
number_of_horizontal_left = 3
number_of_horizontal_right = 3
number_of_horizontal = 3

score = 0

object_list = []
other_object = []
horizontal_object_left = []
horizontal_object_right = []

nombre_pair = set()
while len(nombre_pair) < 5:
    entier = random.randrange(2,100,2)
    nombre_pair.add(entier)
police = pygame.font.Font('freesansbold.ttf', 16)
msg_test = police.render("Bobby",True, NOIR)

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

assert len(object_list) == number_of_enemies, "La liste des rectangles est différente de 10"

#Création de cible supplémentaire
while len(other_object) < number_of_target:
    object_creation_process = pygame.Rect(random.randint(0, largeur_ecran - WIDTH_OBJECT), 0, WIDTH_OBJECT // 2,
                                          HEIGHT_OBJECT // 2)
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

assert len(other_object) == number_of_target, "La liste des cibles est différente de 5"

# Création des objets horizontaux partant de la gauche
while len(horizontal_object_left) < number_of_horizontal_left:
    object_creation_process = pygame.Rect(0, random.randint(hauteur_ecran/8, hauteur_ecran - HEIGHT_OBJECT*3),
                                          WIDTH_OBJECT // 1.25,
                                          HEIGHT_OBJECT // 1.25)
    not_colliding = True
    for horizon_left in horizontal_object_left:
        if horizon_left.colliderect(object_creation_process):
            not_colliding = False
    if not_colliding:
        horizontal_object_left.append(object_creation_process)

assert len(horizontal_object_left) == number_of_horizontal_left, ("La liste des rectangles est différente de ", number_of_horizontal_left)

# Création des objets horizontaux partant de la droite
while len(horizontal_object_right) < number_of_horizontal_right:
    object_creation_process = pygame.Rect(largeur_ecran - (WIDTH_OBJECT // 1.25), random.randint(hauteur_ecran/4, hauteur_ecran - HEIGHT_OBJECT*2),
                                          WIDTH_OBJECT // 1.25,
                                          HEIGHT_OBJECT // 1.25)
    not_colliding = True
    for horizon_right in horizontal_object_right:
        if horizon_right.colliderect(object_creation_process):
            not_colliding = False
    if not_colliding:
        horizontal_object_right.append(object_creation_process)

assert len(horizontal_object_right) == number_of_horizontal_right, ("La liste des rectangles est différente de ", number_of_horizontal_right)

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

    # Création des rectangles sur l'aire de jeu
    for obj in object_list:
        pygame.draw.rect(screen, ORANGE, obj, 1)
        obj.y += (15 / FPS)
        obj.x += (9 / FPS)
        if obj.y > hauteur_ecran:
            object_list.remove(obj)
        if obj.x > largeur_ecran:
            object_list.remove(obj)
            score -= 50
    if len(object_list) == 0:
        pygame.quit()

    # Création des cibles sur l'air de jeu
    for other in other_object:
        pygame.draw.rect(screen, NOIR, other, 1)
        other.y += (15 / FPS)
        other.x += (120 / FPS)

    # Création ds objets horizontaux sur l'aire de jeu
    for horizon_left in horizontal_object_left:
        pygame.draw.rect(screen, BLEU, horizon_left, 1)
        horizon_left.y += (5 / FPS)
        horizon_left.x += (15 / FPS)

    for horizon_right in horizontal_object_right:
        print("Boucle horizon_right : ", horizon_right.x)
        pygame.draw.rect(screen, INDIGO, horizon_right, 1)
        horizon_right.y += (5 / FPS)
        horizon_right.x -= (90 / FPS)
        print("Boucle fin horizon_right : ", horizon_right.x)

    pos_y_object = pos_y_object + 10
    print("pos_y : ", pos_y_object)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
