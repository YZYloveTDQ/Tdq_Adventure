"""人物"""
import pygame


class Tdq():
    def __init__(self):
        self.rect = pygame.Rect(0, 0, 0, 0) # 初始化人物窗口
        self.jump_state = False # 跳跃状态
        self.jump_height = 130 # 跳跃的高度
        # self.lowest_y = 140 # 最低坐标
        self.jump_value = 0 # 跳跃增变量
        self.tdq = pygame.image.load('image/tdq.png').convert_alpha() # 加载图片
        self.jump_audio = pygame.mixer.Sound('audio/jump.wav') # 跳跃音效
        
        self.rect.size = self.tdq.get_size() # 人物窗口为图片大小

        # -----初始窗口左侧位置-------------------------
        self.x = 50 
        self.y = 140
        self.rect.topleft = (self.x, self.y) 

    def jump(self):
        self.jump_state = True

    def move(self):
        if self.jump_state:
            if self.rect.y >= self.y: # 如果人物站在地面
                self.jump_value = -5 # 以5个像素向上移动
            elif self.rect.y <= self.y - self.jump_height: # 跳跃到顶部
                self.jump_value = 5 # 以5个像素向下移动
            
            self.rect.y += self.jump_value # 移动

            if self.rect.y >= self.y: # 回到地面
                self.jump_state = False

    def tdq_update(self, screen):
        screen.blit(self.tdq, (self.rect.x, self.rect.y))