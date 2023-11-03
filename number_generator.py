import random
from time import sleep

import pygame

from HUD.hud_bar import generate_hud, draw_hud
from Sons.sound_effects import get_boum_sound, get_piou_sound, get_shot_sound, finish_sound
from integer_hexa_generator import interger_generator, set_difficulty
from movements import target_movements, decoy_movements

largeur_ecran = 1280
hauteur_ecran = 720

pygame.init()
screen = pygame.display.set_mode((largeur_ecran, hauteur_ecran))
clock = pygame.time.Clock()
pygame.display.set_caption("Nerd shooter")
running = True
dt = 0
# Création de l'objet Font pour écrire dessus
FONT_SIZE = 32
police = pygame.font.Font('freesansbold.ttf', FONT_SIZE)

# Initialisation de variables de couleurs
ORANGE = (255, 127, 0)
NOIR = (0, 0, 0)
BLEU = (0, 0, 255)
INDIGO = (75, 0, 130)
GRIS = (211, 211, 211)

# Initialisation des tailles, framerate et gravité
pos_x_object = 0
pos_y_object = 0
WIDTH_OBJECT = 70
HEIGHT_OBJECT = 50
FPS = 30
GRAVITY = 1.3
SPEED_X = round(60 // FPS)
SPEED_Y = round(90 // FPS)
i = 0
j = 0

# Chargement de l'image du background
background1 = pygame.image.load("assets/background/desert.jpg")
LARGEUR, HAUTEUR = (background1.get_width() // 4, background1.get_height() // 4)
background1 = pygame.transform.scale(background1, (LARGEUR, HAUTEUR))
background2 = pygame.image.load("assets/background/island.jpg")
background2 = pygame.transform.scale(background2, (LARGEUR, HAUTEUR))
list_background = [background1, background2]
current_background = list_background[random.randint(0,1)]

# Position initiale de la cible
target_x_cible, target_y_cible = largeur_ecran//2, hauteur_ecran//2
# Pour cacher le curseur de la souris
pygame.mouse.set_visible(False)

clock = pygame.time.Clock()
number_of_target = 5
number_of_decoy = 5
decoy_hit = 0
number_of_horizontal_left = 3
number_of_horizontal_right = 3
number_of_horizontal = 3
number_of_pair = number_of_target
score = 0
list_of_onscreen_items = [number_of_target, decoy_hit, score]
list_speeds_target = [(SPEED_X, SPEED_Y * 1.1), (SPEED_X * 2, SPEED_Y * 1.5), (-SPEED_X * 4, SPEED_Y), (-SPEED_X*2, SPEED_Y)]
list_speeds_decoy = [(SPEED_X * 2, SPEED_Y * 1.2), (SPEED_X * 2.2, SPEED_Y * 1.5), (-SPEED_X * 3, SPEED_Y * 1.45), (-SPEED_X*2, SPEED_Y)]
has_bounced_sides, has_bounced_ceiling = 0, 0
has_bounced_sides_decoy, has_bounced_ceiling_decoy = 0, 0
integer = 0
is_hexa = -1

# A partir des entrées utilisateurs, défini le niveau de difficulté avec les mutliples à dégommer, les leurres à éviter
# et si la représentation des chiffres doit être décimale ou héxadécimale
integer, is_hexa = set_difficulty(integer, is_hexa)

# En fonction de la difficulté, défini les variables de variation du score
if is_hexa:
    SCORE_INCREMENT = 500
    SCORE_DECREMENT = 100
else:
    SCORE_INCREMENT = 200
    SCORE_DECREMENT = 75

object_list = []
other_object = []
horizontal_object_left = []
horizontal_object_right = []
dictionnary_of_target = {}
dictionnary_of_decoy = {}

# Variable utilisée pour ne pas supprimer une donnée pendant le parcours du dictionnaire
key_to_remove = None

# Création des nombres à cliquer. Utilisation d'un set pour garantir l'absence de doublon
# et création des nombres des leurres
list_msg, list_msg_decoy = interger_generator(integer, number_of_target, police, NOIR, number_of_decoy, is_hexa)

# Création de manière aléatoire et sans chevauchement des aires des rectangles
# Ils peuvent servir de support à l'insertion d'image ou d'autres éléments
while len(object_list) < number_of_target:
    object_creation_process = pygame.Rect(random.randint(0, largeur_ecran - WIDTH_OBJECT), 0, WIDTH_OBJECT,
                                          HEIGHT_OBJECT)
    not_colliding = True
    for obj in object_list:
        if obj.colliderect(object_creation_process):
            not_colliding = False
    if not_colliding:
        object_list.append(object_creation_process)
assert len(object_list) == number_of_target, ("La liste des rectangles est différente de ", number_of_target)

# Boucle de création du dictionnaire pour placer les messages sur l'écran
for obj in object_list:
    coordinates = obj.topleft
    rect = list_msg[j].get_rect()
    rect.topleft = coordinates
    speed_temp = list_speeds_target[random.randint(0, 3)]
    dictionnary_of_target.update({list_msg[j]: [rect, has_bounced_sides, has_bounced_ceiling, speed_temp]})
    print(dictionnary_of_target)
    j += 1
j = 0
del coordinates, rect

# Création des supports des leurres
while len(other_object) < number_of_decoy:
    object_creation_process = pygame.Rect(random.randint(0, largeur_ecran - WIDTH_OBJECT), 0, WIDTH_OBJECT,
                                          HEIGHT_OBJECT)
    not_colliding = True
    for other in other_object:
        if other.colliderect(object_creation_process):
            not_colliding = False
    if not_colliding:
        other_object.append(object_creation_process)
assert len(other_object) == number_of_decoy, ("La liste des leurres est différente de ", number_of_decoy)

# Création des leurres
for other in other_object:
    coordinates = other.topleft
    rect = list_msg_decoy[j].get_rect()
    rect.topleft = coordinates
    speed_temp = list_speeds_decoy[random.randint(0, 3)]
    dictionnary_of_decoy.update(
        {list_msg_decoy[j]: [rect, has_bounced_sides_decoy, has_bounced_ceiling_decoy, speed_temp]})
    print(dictionnary_of_target)
    j += 1
j = 0
del coordinates, rect

HUD = generate_hud(largeur_ecran, hauteur_ecran, NOIR)

while running:
    screen.blit(current_background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            target_x_cible, target_y_cible = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            get_piou_sound()
            for dicK, dicV in dictionnary_of_target.items():
                if dicV[0].collidepoint(event.pos):
                    key_to_remove = dicK
                    score += SCORE_INCREMENT
                    get_boum_sound()
                    number_of_target -= 1
                    list_of_onscreen_items[0], list_of_onscreen_items[2] = number_of_target, score
            for decoy_key, decoy_values in dictionnary_of_decoy.items():
                if decoy_values[0].collidepoint(event.pos):
                    score -= SCORE_DECREMENT
                    decoy_hit += 1
                    list_of_onscreen_items[1], list_of_onscreen_items[2] = decoy_hit, score

    if key_to_remove is not None:
        dictionnary_of_target.pop(key_to_remove)
        key_to_remove = None

    pos_y_object += (12 / FPS) * GRAVITY

    # Création des CIBLES sur leur support
    dictionnary_of_target = target_movements(dictionnary_of_target, screen, largeur_ecran, FONT_SIZE, hauteur_ecran).copy()

    # Création des LEURRES sur leur support
    dictionnary_of_decoy = decoy_movements(dictionnary_of_decoy, screen, largeur_ecran, FONT_SIZE, hauteur_ecran).copy()

    if len(dictionnary_of_target.keys()) == 0:
        finish_sound()
        sleep(2.0)
        pygame.quit()

    # Dessin du réticule de visée
    pygame.draw.circle(screen, (0, 0, 0), (target_x_cible, target_y_cible), 16, 2)
    pygame.draw.line(screen, (0,0,0),( target_x_cible-1, target_y_cible-14), (target_x_cible-1, target_y_cible+14),2)
    pygame.draw.line(screen, (0,0,0),( target_x_cible-14, target_y_cible-1), (target_x_cible+14, target_y_cible-1),2)

    # Dessin du HUD
    draw_hud(screen, GRIS, HUD, list_of_onscreen_items, NOIR)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()