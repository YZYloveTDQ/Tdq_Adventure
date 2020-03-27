"""背景音乐按钮"""
import pygame


class Music_button():
    is_open = True
    def __init__(self):
        self.open_img = pygame.image.load('image/btn_open.png').convert_alpha()
        self.close_img = pygame.image.load('image/btn_close.png').convert_alpha()
        self.bg_music = pygame.mixer.Sound('audio/bg_music.wav')
    
    def is_select(self):
        point_x, point_y = pygame.mouse.get_pos() # 获取鼠标的坐标
        w, h = self.open_img.get_size() # 按钮图片的大小

        # -----判断鼠标是否在图片范围内的判断-------
        in_x = point_x > 20 and point_x < 20+w
        in_y = point_y > 20 and point_y < 20+h
        return in_x and in_y
