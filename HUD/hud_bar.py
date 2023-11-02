import pygame


def generate_hud(largeur_ecran, hauteur_ecran, NOIR):
    police_hud = pygame.font.Font('freesansbold.ttf', 16)
    hud_labels = ["Cibles : ", "Leurre : ", "Score : "]
    hud_size = (largeur_ecran, hauteur_ecran * 0.10)
    hud_background = pygame.Rect(0, hauteur_ecran - hud_size[1], hud_size[0], hud_size[1])

    # Calcul des placements des rectangles container de libellé
    modele_component_hud = police_hud.render("Leurre : 999", True, NOIR)
    rect_component_hud = [modele_component_hud.get_rect()]
    list_rect_component_hud = list()
    division_hud_largeur = hud_size[0] // 3
    division_hud_hauteur = hud_size[1] // 3
    margin_hud = division_hud_largeur // 3
    for n in range(len(hud_labels)):
        rect_temp = rect_component_hud.copy()
        rect_temp = (margin_hud + (n * division_hud_largeur), hauteur_ecran - (division_hud_hauteur * 1.75))
        list_rect_component_hud.append(rect_temp)
        del rect_temp
    return hud_background, hud_labels, list_rect_component_hud, police_hud


def draw_hud(screen, GRIS, HUD, list_of_onscreen_items, NOIR):
    hud_background = HUD[0]
    hud_labels = HUD[1]
    list_rect_component_hud = HUD[2]
    police_hud = HUD[3]

    pygame.draw.rect(screen, GRIS, hud_background)

    # Placement du contenu du HUD
    for i in range(len(HUD[1])):
        msg = police_hud.render(hud_labels[i] + str(list_of_onscreen_items[i]), True, NOIR)
        screen.blit(msg, list_rect_component_hud[i])
