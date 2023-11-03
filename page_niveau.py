import pygame
import sys


ETAPE_CHOIX = 1
ETAPE_EXPLICATION = 2
ETAPE_JOUER = 3


etape_jeux= ETAPE_CHOIX


# Initialisation de Pygame
pygame.init()
pygame.mixer.init()
# Configuration de la fenêtre
width_niveau, height_niveau = 800, 600
screen = pygame.display.set_mode((width_niveau, height_niveau))

pygame.display.set_caption("Selection niveau")

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

# Police pour les textes
font = pygame.font.Font(None, 36)

# Création du dictionnaire "boutons_niveau" avec leur initiales
button_niveau = {
    "Facile": {"target_rect": pygame.Rect(500, 200, 200, 50), "current_y": -50},
    "Moyen": {"target_rect": pygame.Rect(500, 300, 200, 50), "current_y": -50},
    "Difficile": {"target_rect": pygame.Rect(500, 400, 200, 50), "current_y": -50}
}

# chargez l'effet sonore
click_sound = pygame.mixer.Sound("effet sonore/Shot of Winchester Magnum XTR.ogg")
# variable effet de pression sur le bouton enfoncé
pressed_button_niveau = None

# Boucle principale du jeu
running = True
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if etape_jeux == ETAPE_CHOIX:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                for level, info in button_niveau.items():
                    if info["target_rect"].collidepoint(mouse_pos):
                        print(f"Niveau choisi : {level}")
                        pressed_button_niveau = level
                        click_sound.play()

                        if level == "Facile":
                            pygame.time.wait(2000)
                            from fonction_page_intermediaire_facile import page_intermediaire_facile
                            page_intermediaire_facile()
                        if level == "Moyen":
                            pygame.time.wait(2000)
                            from fonction_page_intermediaire_medium import page_intermediaire_medium
                            page_intermediaire_medium()
                        if level == "Difficile":
                            pygame.time.wait(2000)
                            from fonction_page_intermediaire_difficile import page_intermediaire_difficile
                            page_intermediaire_difficile()

                            etape_jeux = ETAPE_EXPLICATION


                #etape_jeux = ETAPE_EXPLICATION


    # Affichage de l'écran
    screen.fill(WHITE)

    if etape_jeux == ETAPE_CHOIX:

        # Ajout du titre
        titre_surface_niveau = font.render('Choisissez le niveau de jeu', True, BLACK)
        titre_rect = titre_surface_niveau.get_rect(center=(width_niveau // 2, 50))
        screen.blit(titre_surface_niveau, titre_rect)

        # Dessiner les boutons en 3D
        for level, info in button_niveau.items():
            target_rect = info["target_rect"]
            current_y = info["current_y"]

            # Mettre à jour la position y pour faire glisser le bouton vers le bas
            if current_y < target_rect.y:
                current_y += 1
                info["current_y"] = current_y

            # Dessiner le bouton
            button_rect = pygame.Rect(target_rect.x, current_y, target_rect.width, target_rect.height)

            # Si le bouton est enfoncé, décaler le rendu de l'ombre et du texte

            pression = 5 if pressed_button_niveau == level else 0

            pygame.draw.rect(screen, GRAY, (button_rect.x + 5 + pression, button_rect.y + 5 + pression, button_rect.width, button_rect.height))
            pygame.draw.rect(screen, BLACK, (button_rect.x + pression, button_rect.y + pression, button_rect.width, button_rect.height), 2)
            text_surface = font.render(level, True, BLACK)
            screen.blit(text_surface, (button_rect.x + 50 + pression, button_rect.y + 10 + pression))

    #elif etape_jeux == ETAPE_EXPLICATION:
    # en fonction du level afficher explication

    #elif etape_jeux
    #entrer le jeux
    pygame.display.flip()
   # print(".", end="")

# Quitter Pygame
pygame.quit()
sys.exit()

