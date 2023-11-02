import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

# Importez les fonctions de gestion des scores
high_scores = {}

def ajouter_high_score(nom, score):
    high_scores[nom] = score
# Ajoutez les joueurs avec leurs scores
ajouter_high_score("ET", 800)
ajouter_high_score("Ray Ferrier(WOW)", 1500)
ajouter_high_score("Capt.Steven Hiller(ID)", 2000)
ajouter_high_score("AGENT K (MIB)", 3000)
ajouter_high_score("Chuck Norris", 10000)

def afficher_high_scores_screen():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        SCREEN.fill((0, 0, 0))

        high_scores_title = get_font(50).render("High Scores", True, (184, 143, 64))
        high_scores_title_rect = high_scores_title.get_rect(center=(640, 50))
        SCREEN.blit(high_scores_title, high_scores_title_rect)

        # Tri des scores par ordre décroissant
        high_scores_sorted = sorted(high_scores.items(), key=lambda x: x[1], reverse=True)

        y_position = 120
        for i, (nom, score) in enumerate(high_scores_sorted[:10]):
            score_text = get_font(30).render(f"{i + 1}. {nom}: {score}", True, (255, 255, 255))
            score_rect = score_text.get_rect(center=(640, y_position))
            SCREEN.blit(score_text, score_rect)
            y_position += 30

        # Ajoutez un bouton "BACK" pour revenir au menu principal
        BACK_BUTTON = Button(image=None, pos=(100, 650),
                            text_input="BACK", font=get_font(30), base_color=(215, 252, 212), hovering_color=(255, 255, 255))
        BACK_MOUSE_POS = pygame.mouse.get_pos()
        BACK_BUTTON.changeColor(BACK_MOUSE_POS)
        BACK_BUTTON.update(SCREEN)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(BACK_MOUSE_POS):
                    main_menu()  # Revenir au menu principal

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill((0, 0, 0))

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, (255, 255, 255))
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460),
                            text_input="BACK", font=get_font(75), base_color=(255, 255, 255), hovering_color=(0, 255, 0))

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()

        if game_over:
            player_name = input("Enter your name: ")
            if player_name:
                ajouter_high_score(player_name, score)

def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill((255, 255, 255))

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, (0, 0, 0))
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                            text_input="BACK", font=get_font(75), base_color=(0, 0, 0), hovering_color=(0, 255, 0))

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():

     while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, (182, 143, 64))
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250),
                            text_input="PLAY", font=get_font(75), base_color=(215, 252, 212), hovering_color=(255, 255, 255))
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 350),
                            text_input="OPTIONS", font=get_font(75), base_color=(215, 252, 212), hovering_color=(255, 255, 255))
        HIGH_SCORES_BUTTON = Button(image=pygame.image.load("assets/High score Rect.png"), pos=(640, 450),
                            text_input="HIGH SCORES", font=get_font(75), base_color=(215, 252, 212), hovering_color=(255, 255, 255))
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
                            text_input="QUIT", font=get_font(75), base_color=(215, 252, 212), hovering_color=(255, 255, 255))

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, HIGH_SCORES_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                if HIGH_SCORES_BUTTON.checkForInput(MENU_MOUSE_POS):
                    afficher_high_scores_screen()  # Afficher l'écran des scores

        pygame.display.update()

main_menu()
