import pygame


class Flying_object(pygame.Rect):
    def __init__(self, speed, has_bounced):
        super().__init__()
