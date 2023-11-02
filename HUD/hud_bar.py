import random
import pygame

largeur_ecran = 1280
hauteur_ecran = 720

pygame.init()
screen = pygame.display.set_mode((largeur_ecran, hauteur_ecran))
clock = pygame.time.Clock()
running = True
dt = 0
# Création de l'objet Font pour écrire dessus
police = pygame.font.Font('freesansbold.ttf', 16)

screen.fill("grey")
ORANGE = (255, 127, 0)
NOIR = (0, 0, 0)
BLEU = (0, 0, 255)
INDIGO = (75, 0, 130)

pos_x_object = 0
pos_y_object = 0
WIDTH_OBJECT = 70
HEIGHT_OBJECT = 50
FPS = 30
GRAVITY = 1.3

# Initialisation des variables d'itération
i = 0
j = 0

clock = pygame.time.Clock()
number_of_target = 5
number_of_decoy = 5
number_of_horizontal_left = 3
number_of_horizontal_right = 3
number_of_horizontal = 3
number_of_pair = number_of_decoy
score = 0

object_list = []
other_object = []
horizontal_object_left = []
horizontal_object_right = []

# Variables du HUD
hud_labels = ["Cibles : ", "Leurre : ", "Score : "]
list_of_onscreen_items = (
number_of_target, number_of_decoy, score)  # la taille de list_of_onscreen_items doit être la même que hud_labels
ingame_target_to_kill = 0
ingame_decoy_destroy = 0
score = 0
hud_size = (largeur_ecran, hauteur_ecran * 0.15)
GRIS = (211, 211, 211)
hud_background = pygame.Rect(0, hauteur_ecran - hud_size[1], hud_size[0], hud_size[1])
hud_components = list()

# Calcul des placements des rectangles container de libellé
modele_component_hud = police.render("Leurre : 999", True, NOIR)
rect_component_hud = [modele_component_hud.get_rect()]
list_rect_component_hud = list()
division_hud_largeur = hud_size[0] // 3
division_hud_hauteur = hud_size[1] // 3
margin_hud = 8
for i in range(len(hud_labels)):
    rect_temp = rect_component_hud.copy()
    rect_temp = (margin_hud + (i * division_hud_largeur), hauteur_ecran - (division_hud_hauteur * 2))
    list_rect_component_hud.append(rect_temp)
    del rect_temp
i = 0

set_pair = set()
dictionnary = {}
# Variable utilisée pour ne pas supprimer une donnée pendant le parcours du dictionnaire
key_to_remove = None

# Création des nombres à cliquer. Utilisation d'un set pour garantir l'absence de doublon
while len(set_pair) < number_of_pair:
    entier = random.randrange(2, 100, 2)
    set_pair.add(entier)

# On transforme le set en list, pour accéder aux valeurs plus facilement
list_pair = list(set_pair)
list_msg = list()

# Les multiples sont transformés en message affichable à l'écran
for i in range(len(list_pair)):
    list_msg.append(police.render(str(list_pair[i]), True, NOIR))

i = 0

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

assert len(object_list) == number_of_target, "La liste des rectangles est différente de 10"

# Boucle de création du dictionnaire pour placer les messages sur l'écran
for obj in object_list:
    coordinates = obj.topleft
    rect = list_msg[j].get_rect()
    rect.topleft = coordinates
    dictionnary.update({list_msg[j]: rect})
    j += 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for dicK, dicV in dictionnary.items():
                if dicV.collidepoint(event.pos):
                    key_to_remove = dicK
                    score += 200
    if key_to_remove is not None:
        dictionnary.pop(key_to_remove)
        key_to_remove = None
    screen.fill("grey")

    pos_y_object += (12 / FPS) * GRAVITY
    # Création des rectangles sur l'aire de jeu avec les nombres
    for msg, rect in dictionnary.items():
        screen.blit(msg, rect)
        j += 1
        rect.y += pos_y_object
        rect.x += (15 / FPS)

    if len(dictionnary) == 0:
        pygame.quit()
    j = 0

    # Dessin du HUD
    pygame.draw.rect(screen, GRIS, hud_background)

    # Placement du contenu du HUD
    for i in range(len(hud_labels)):
        msg = police.render(hud_labels[i] + str(list_of_onscreen_items[i]), True, NOIR)
        screen.blit(msg, list_rect_component_hud[i])
    i = 0
    print("pos_y : ", pos_y_object)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
