import pygame


def game_over(screen):
    bump_audio = pygame.mixer.Sound('audio/bump.wav')  # 撞击声音
    bump_audio.play()  # 播放撞击的声音

    over_img = pygame.image.load('image/over.jpg').convert_alpha()
    screen.blit(over_img, (300, 0))
