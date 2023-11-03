import pygame

COULEUR_FOND = (0, 255, 0)

pygame.init()

# Chargement de l'image du background1
background1 = pygame.image.load("assets/background/desert.jpg")
print("Dimension de l'image du background1", background1.get_size())
LARGEUR, HAUTEUR = (background1.get_width() // 4, background1.get_height() // 4)
background1 = pygame.transform.scale(background1, (LARGEUR, HAUTEUR))
background2 = pygame.image.load("assets/background/island.jpg")
background2 = pygame.transform.scale(background2, (LARGEUR, HAUTEUR))


# Initialisation de la fenêtre pygame
fen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("UFO1")
fen.fill(COULEUR_FOND)

# Préparation de de l'image du background1 dans pygame
background1 = background1.convert()

# Affichage du bambou aux coordonnées précisées en second argument

background_game = background2
continuer = True

while continuer:
    for event in pygame.event.get():
        # L'utilisateur veut-il fermer la fenêtre ?
        if event.type == pygame.QUIT:
            continuer = False
       # L'utilisateur a-t-il relâché un bouton de souris
        elif event.type == pygame.MOUSEBUTTONUP:
            print("up", event.pos)
            if background_game == background1:
                background_game = background2
            else:
                background_game= background1

    fen.blit(background_game, (0, 0))

    pygame.display.flip()

pygame.quit()


