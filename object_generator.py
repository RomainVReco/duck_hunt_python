import random

import pygame

largeur_ecran = 1280
hauteur_ecran = 720

pygame.init()
screen = pygame.display.set_mode((largeur_ecran, hauteur_ecran))
clock = pygame.time.Clock()
running = True
dt = 0
screen.fill("grey")
ORANGE = (255,127,0)

pos_x_object = 0
pos_y_object = 0
WIDTH_OBJECT = 70
HEIGHT_OBJECT = 50

object_list=[]

i=0

# object_list.append(pygame.draw.rect(screen, ORANGE, [random.randint(0,largeur_ecran-WIDTH_OBJECT),0,WIDTH_OBJECT,HEIGHT_OBJECT]))

while len(object_list) < 10 :
    object_creation_process = pygame.draw.rect(screen, ORANGE, [random.randint(0,largeur_ecran-WIDTH_OBJECT),0,WIDTH_OBJECT,HEIGHT_OBJECT])
    not_colliding = True
    for obj in object_list :
        if obj.colliderect(object_creation_process):
            not_colliding = False
    if not_colliding:
        object_list.append(object_creation_process)

assert len(object_list) == 10, "La liste des rectangles est > 10"


pygame.draw.rect(screen, ORANGE, [pos_x_object, pos_y_object,WIDTH_OBJECT, HEIGHT_OBJECT])

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
pygame.quit()