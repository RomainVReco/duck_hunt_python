import random
import pygame

PATH_SOUND_EFFECTS = "Sons/Bruitage/"
PATH_MUSIC = "Sons/BO/"
piou_sounds = ["piou_1.mp3", "piou_2.mp3", "piou_3.mp3"]
boum_sounds = ["boum_1.mp3", "boum_2.mp3", "boum_3.mp3", "boum_4.mp3"]
finish_sounds = ["impressionnant_1.mp3", "wahou_1.mp3"]


def get_shot_sound():
    shot_sound = pygame.mixer.Sound("effet sonore/Shot in 357 Magnum 9mm.ogg")
    pygame.mixer.Sound.play(shot_sound)


def get_piou_sound():
    sound_to_play = piou_sounds[random.randint(0, 2)]
    piou_sound = pygame.mixer.Sound(PATH_SOUND_EFFECTS + sound_to_play)
    piou_sound.set_volume(0.7)
    pygame.mixer.Sound.play(piou_sound)


def get_boum_sound():
    sound_to_play = boum_sounds[random.randint(0, 3)]
    boum_sound = pygame.mixer.Sound(PATH_SOUND_EFFECTS + sound_to_play)
    pygame.mixer.Sound.play(boum_sound)


def get_transition_music():
    transition_music = pygame.mixer.Sound(PATH_MUSIC + "MM2_Stage_Select.mp3")
    pygame.mixer.Sound.play(transition_music)


def play_intro_music():
    pygame.mixer.music.load(PATH_MUSIC + "MM2_Intro_and_Title.mp3")
    pygame.mixer.music.play()


def finish_sound():
    sound_to_play = finish_sounds[random.randint(0, 1)]
    finish_sound = pygame.mixer.Sound(PATH_SOUND_EFFECTS + sound_to_play)
    finish_sound.set_volume(1)
    pygame.mixer.Sound.play(finish_sound)



