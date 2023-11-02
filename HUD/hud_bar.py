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

# Initialisation de variables de couleurs et de framerate
ORANGE = (255, 127, 0)
NOIR = (0, 0, 0)
BLEU = (0, 0, 255)
INDIGO = (75, 0, 130)
FPS = 30

# Initialisation des variables d'itération
i = 0
j = 0

clock = pygame.time.Clock()
number_of_target = 5
number_of_decoy = 5
number_of_pair = number_of_decoy
score = 0

object_list = []
other_object = []
horizontal_object_left = []
horizontal_object_right = []

# Variables du HUD
hud_labels = ["Cibles : ", "Leurre : ", "Score : "]
# la taille de list_of_onscreen_items doit être la même que hud_labels
list_of_onscreen_items = (number_of_target, number_of_decoy, score)

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
margin_hud = division_hud_largeur//3
for i in range(len(hud_labels)):
    rect_temp = rect_component_hud.copy()
    rect_temp = (margin_hud + (i * division_hud_largeur), hauteur_ecran - (division_hud_hauteur * 1.75))
    list_rect_component_hud.append(rect_temp)
    del rect_temp
i = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Dessin du HUD
    pygame.draw.rect(screen, GRIS, hud_background)

    # Placement du contenu du HUD
    for i in range(len(hud_labels)):
        msg = police.render(hud_labels[i] + str(list_of_onscreen_items[i]), True, NOIR)
        screen.blit(msg, list_rect_component_hud[i])
    i = 0

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
