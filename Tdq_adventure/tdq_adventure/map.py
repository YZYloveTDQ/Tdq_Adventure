"""定义地图"""
import pygame


class Map():
    """移动的地图"""

    def __init__(self, x, y):
        self.bg = pygame.image.load("image/bg.png").convert_alpha()  # 加载图片，convert_alpha()使得图像具有像素透明度
        self.x = x # 地图相对screen的位置
        self.y = y

    def map_rolling(self):
        if self.x < -790: # 地图图片大小未800*199，左边的位置小于了-790则说明移动出了窗体
            self.x = 800 # 图片直接移动到新的坐标点
        else:
            self.x -= 5 # 向左移动5个像素
    
    def map_update(self, screen):
        screen.blit(self.bg, (self.x, self.y))

if __name__ == "__main__":
    pass