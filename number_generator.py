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
FONT_SIZE = 32
police = pygame.font.Font('freesansbold.ttf', FONT_SIZE)

screen.fill("grey")

# Initialisation de variables de couleurs
ORANGE = (255, 127, 0)
NOIR = (0, 0, 0)
BLEU = (0, 0, 255)
INDIGO = (75, 0, 130)

# Initialisation des tailles, framerate et gravité
pos_x_object = 0
pos_y_object = 0
WIDTH_OBJECT = 70
HEIGHT_OBJECT = 50
FPS = 30
GRAVITY = 1.3
SPEED_X = (60 // FPS)
SPEED_Y = (90 // FPS)

clock = pygame.time.Clock()
number_of_target = 5
number_of_decoy = 5
number_of_horizontal_left = 3
number_of_horizontal_right = 3
number_of_horizontal = 3
number_of_pair = number_of_target
list_speeds = [(SPEED_X, SPEED_Y*1.1), (SPEED_X * 2, SPEED_Y * 1.5), (SPEED_X * 4, SPEED_Y)]
has_bounced_sides = 0
has_bounced_ceiling = 0

score = 0

object_list = []
other_object = []
horizontal_object_left = []
horizontal_object_right = []

set_pair = set()
dictionnary_of_target = {}

# Variable utilisée pour ne pas supprimer une donnée pendant le parcours du dictionnaire
key_to_remove = None

# Création des nombres à cliquer. Utilisation d'un set pour garantir l'absence de doublon
while len(set_pair) < number_of_pair:
    entier = random.randrange(10, 200, 2)
    set_pair.add(entier)

# On transforme le set en list, pour accéder aux valeurs plus facilement
list_pair = list(set_pair)
list_msg = list()

# Les multiples sont transformés en message affichable à l'écran
for i in range(len(list_pair)):
    list_msg.append(police.render(str(list_pair[i]), True, NOIR))

i = 0
j = 0

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
    speed_temp = list_speeds[random.randint(0, 2)]
    dictionnary_of_target.update({list_msg[j]: [rect, has_bounced_sides, has_bounced_ceiling, speed_temp]})
    print(dictionnary_of_target)
    j += 1
j = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for dicK, dicV in dictionnary_of_target.items():
                if dicV[0].collidepoint(event.pos):
                    key_to_remove = dicK
                    score += 200
    if key_to_remove is not None:
        dictionnary_of_target.pop(key_to_remove)
        key_to_remove = None
    screen.fill("grey")

    pos_y_object += (12 / FPS) * GRAVITY
    # Création des rectangles sur l'aire de jeu avec les nombres
    for msg, stats_items in dictionnary_of_target.items():
        screen.blit(msg, stats_items[0])
        rect_temp = stats_items[0]
        speed_temp = stats_items[3]
        rect_temp.x += speed_temp[0]
        rect_temp.y += speed_temp[1]
        if rect_temp.x > largeur_ecran-FONT_SIZE or rect_temp.x < 0:
            new_speed_x = (speed_temp[0] * -1, speed_temp[1])
            stats_items[3] = new_speed_x
            if stats_items[1] == 0:
                has_bounced_sides = 1
            else:
                has_bounced_sides = 0
            stats_items[1] = has_bounced_sides
            dictionnary_of_target.update({msg: stats_items})
        if rect_temp.y > (hauteur_ecran - (round(hauteur_ecran * 0.15))) or rect_temp.y < 0:
            new_speed_y = (speed_temp[0], speed_temp[1] * -1)
            stats_items[3] = new_speed_y
            if stats_items[2] == 0:
                has_bounced_ceiling = 1
            else:
                has_bounced_ceiling = 0
            stats_items[2] = has_bounced_ceiling
            dictionnary_of_target.update({msg: stats_items})

    if len(dictionnary_of_target.keys()) == 0:
        pygame.quit()
    j = 0

    print("pos_y : ", pos_y_object)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
