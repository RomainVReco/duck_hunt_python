import pygame

def page_intermediaire_facile():

    # Initialisation de Pygame
    pygame.init()

    # Configuration de la fenêtre
    width_page_intermediaire, height_page_intermediaire = 800, 600
    screen = pygame.display.set_mode((width_page_intermediaire, height_page_intermediaire))

    #  chargement de l'image de fond
    img_fond_intermediaire = pygame.image.load("img/interior-intermediaire.jpeg").convert()
    img_fond_intermediaire = pygame. transform.scale(img_fond_intermediaire, (width_page_intermediaire, height_page_intermediaire))

    click_sound = pygame.mixer.Sound("effet sonore/Shot in 357 Magnum 9mm.ogg")

    # Texte d'explication
    font_text_intermediaire = pygame.font.Font(None, 40)
    text_explication_intermediaire = [
        "NIVEAU FACILE",
        "NOMBRE DE CIBLE: ",
        "NOMBRE DE LEURRE: ",
        "NOMBRE D'OBSTACLE: ",
    ]
    spacing = 30
    column_width = width_page_intermediaire // len(text_explication_intermediaire)
    total_text_height = len(text_explication_intermediaire) * spacing
    start_y = (height_page_intermediaire - total_text_height) //3


    #Bouton commencer
    button_commencer_jeu = pygame.Surface((200, 50))
    button_commencer_jeu.fill((50, 100, 50))
    button_commencer_jeu_rect = button_commencer_jeu.get_rect(center=(width_page_intermediaire // 2, height_page_intermediaire - 100))
    button_commencer_text = font_text_intermediaire.render("Commencer", True, (255, 255, 255))
    button_commencer_text_rect = button_commencer_text.get_rect(center=button_commencer_jeu_rect.center)


    # Pour manipuler la clarté de l'image de fond.
    DARKEN_IMG_FOND_INTER = 2
    for x in range(img_fond_intermediaire.get_width()):
        for y in range(img_fond_intermediaire.get_height()):
            r, g, b, a = img_fond_intermediaire.get_at((x, y))
            img_fond_intermediaire.set_at((x, y), (r // DARKEN_IMG_FOND_INTER, g // DARKEN_IMG_FOND_INTER, b // DARKEN_IMG_FOND_INTER))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button_commencer_jeu_rect.collidepoint(mouse_pos):
                    print(f"Commencer le jeu : Niveau Facile")
                    click_sound.play()

        screen.blit(img_fond_intermediaire,(0,0))

        #Affichage des lignes de texte
        for index, line in enumerate(text_explication_intermediaire):
            text_surface = font_text_intermediaire.render(line, True, (255, 255, 255))
            text_explication_intermediaire_rect = text_surface.get_rect(center=(width_page_intermediaire // 2, start_y + index * spacing))
            screen.blit(text_surface, text_explication_intermediaire_rect.topleft)

        screen.blit(button_commencer_jeu, button_commencer_jeu_rect.topleft)
        screen.blit(button_commencer_text, button_commencer_text_rect.topleft)


        pygame.display.flip()

    #if __name__ == "__page_niveau__":
page_intermediaire_facile()

pygame.quit()











# chargement de la cible
'''img_cible_intermediaire = pygame.image.load("img/cible_or.jpg.webp").convert_alpha()
img_cible_intermediaire_width = 50
img_cible_intermediaire_height = 50
img_cible_intermediaire = pygame.transform.scale(img_cible_intermediaire,(img_cible_intermediaire_width, img_cible_intermediaire_height))
img_cible_intermediaire_rect = img_cible_intermediaire.get_rect(topleft=(100.0, 50.0))
img_cible_intermediaire_speed = [1,1] #c'est la vitesse de x et y

limit_superieur = height_page_intermediaire // 4 # Pour limiter au quart supérieur'''



'''img_cible_intermediaire_rect.move_ip(img_cible_intermediaire_speed)

        # Pour faire rebondir l'image cible
    if img_cible_intermediaire_rect.left < 0 or img_cible_intermediaire_rect.right > width_page_intermediaire:
        img_cible_intermediaire_speed[0] = -img_cible_intermediaire_speed[0]
    if img_cible_intermediaire_rect.top < 0 or img_cible_intermediaire_rect.bottom > limit_superieur:
        img_cible_intermediaire_speed[1] = -img_cible_intermediaire_speed[1]'''

#screen.blit(img_cible_intermediaire, img_cible_intermediaire_rect.topleft)