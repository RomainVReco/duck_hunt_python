import time
import pygame


# Initialisation de Pygame
pygame.init()

pygame.mixer.init()

pygame.mixer.music.load("effet sonore/Shot in 357 Magnum 9mm.ogg")

# Configuration de la fenêtre
width, height = 900, 700
screen = pygame.display.set_mode((width, height))



################ Pour remplacer le cursur de la souris par une cible importé(image)#######
# Pour cacher le curseur de la souris
pygame.mouse.set_visible(False)

# image du curseur d'arme
#gun_cursor = pygame.image.load("img/cible_or.jpg.webp")
# Redimensionne l'image du curseur d'arme
#new_width, new_height = 70, 70  # Nouvelles dimensions
#gun_cursor = pygame.transform.scale(gun_cursor, (new_width, new_height))
########################################################################################


mouse_is_pressed = False
bullet_impacts = []
movement_traces = []


# Position initiale de la cible
target_x, target_y = 400, 300

# Vitesse de déplacement du rectangle
#speed = 3


# Boucle principale du jeu
running = True
while running:
    current_time = time.time()
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEMOTION:
            target_x, target_y = pygame.mouse.get_pos()
            movement_traces.append((target_x, target_y))

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_is_pressed = True
            pygame.mixer.music.play()

        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_is_pressed = False
            pygame.mixer.music.stop()

            bullet_impacts.append((target_x, target_y, current_time))


    # Limiter les mouvements dans la fenêtre
    target_x = max(0, min(target_x, width))
    target_y = max(0, min(target_y, height))

    # Dessiner le fond et le rectangle
    screen.fill((255, 255, 255))  # Blanc

    # Dessiner l'image du curseur d'arme

    #screen.blit(gun_cursor, (target_x, target_y))

    pygame.draw.circle(screen, (255, 0, 0), (target_x, target_y), 20)
    pygame.draw.circle(screen, (0, 0, 0), (target_x, target_y), 16)
    pygame.draw.circle(screen, (255, 0, 0), (target_x, target_y), 12)
    pygame.draw.circle(screen, (0, 0, 0), (target_x, target_y), 8)
    pygame.draw.circle(screen, (255, 0, 0), (target_x, target_y), 4)

    # Dessiner impact de balle
    for impact in bullet_impacts:
        x, y, impact_time = impact
        # Vérifie si l'impact est trop vieux (plus de 5 secondes)
        if current_time - impact_time > 5:
            bullet_impacts.remove(impact)
        else:
            pygame.draw.circle(screen, (0,0,0), (x,y), 5)

    # Mettre à jour l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
