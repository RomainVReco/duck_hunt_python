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
number_of_enemies = 5
number_of_target = 5
number_of_horizontal_left = 3
number_of_horizontal_right = 3
number_of_horizontal = 3
number_of_pair = number_of_target

score = 0

object_list = []
other_object = []
horizontal_object_left = []
horizontal_object_right = []

set_pair = set()
dictionnary = {}


#Création des nombres à cliquer. Utilisation d'un set pour garantir l'absence de doublon
while len(set_pair) < number_of_pair:
    entier = random.randrange(2,100,2)
    set_pair.add(entier)

#On transforme le set en list, pour accéder aux valeurs plus facilement
list_pair = list(set_pair)
list_msg = list()

#Création de l'objet Font pour écrire dessus
police = pygame.font.Font('freesansbold.ttf', 16)

for i in range(len(list_pair)):
    list_msg.append(police.render(str(list_pair[i]), True, NOIR))

i = 0
j = 0

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

# for obj, i in object_list, list_pair:
#     list_pair[i].topleft = obj.topleft



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
        coordinates = obj.topleft
        for list_n in list_msg:
            rect = list_n.get_rect()
            rect.topleft = coordinates
            dictionnary.update({rect : list_n})

    # Création des rectangles sur l'aire de jeu
    for obj in object_list:
        screen.blit(list_msg[j], obj)
        j += 1
        obj.y += (15 / FPS)
        obj.x += (9 / FPS)
        if obj.y > hauteur_ecran:
            object_list.remove(obj)
        if obj.x > largeur_ecran:
            object_list.remove(obj)
            score -= 50
    if len(object_list) == 0:
        pygame.quit()
    j = 0

    pos_y_object = pos_y_object + 10
    print("pos_y : ", pos_y_object)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
