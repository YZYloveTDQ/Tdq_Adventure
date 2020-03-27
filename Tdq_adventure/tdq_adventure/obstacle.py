"""障碍物"""
import pygame
import random
screen_width = 822
screen_height = 199


class Obstacle():
    score = 1 # 局部变量
    def __init__(self):
        self.rect = pygame.Rect(0, 0, 0, 0) # 初始化窗口
        self.missile = pygame.image.load('image/missile.png').convert_alpha()
        self.pipe = pygame.image.load('image/pipe.png').convert_alpha()
        self.scores = (pygame.image.load('image/0.png').convert_alpha(),
                       pygame.image.load('image/1.png').convert_alpha(),
                       pygame.image.load('image/2.png').convert_alpha(),
                       pygame.image.load('image/3.png').convert_alpha(),
                       pygame.image.load('image/4.png').convert_alpha(),
                       pygame.image.load('image/5.png').convert_alpha(),
                       pygame.image.load('image/6.png').convert_alpha(),
                       pygame.image.load('image/7.png').convert_alpha(),
                       pygame.image.load('image/8.png').convert_alpha(),
                       pygame.image.load('image/9.png').convert_alpha())
        self.score_audio = pygame.mixer.Sound('audio/score.wav')  # 加分

        # ------随机产生桶或者子弹--------------
        r = random.randint(0, 1)
        if r == 0:
            self.obstacle = self.missile # 子弹障碍物
            self.move = 15 # 子弹速度
            self.obstacle_y = 100 # 子弹高度
        else:
            self.obstacle = self.pipe # 桶障碍物
            self.move = 5 # 桶的移动速度和地图速度一样
            self.obstacle_y = 150 # 桶的位置
        
        # ---------窗口尺寸为图片大小--------------------
        self.rect.size = self.obstacle.get_size() 

        # -------------窗口中心初始位置----------------
        self.x = 800 
        self.y = self.obstacle_y
        self.rect.center = (self.x, self.y) 

    def obstacle_move(self):
        self.rect.x -= self.move

    def obstacle_update(self, screen):
        screen.blit(self.obstacle, (self.rect.x, self.rect.y))

    def get_score(self):
        """每一次调用说明越过了障碍物，score=1.结束的时候score=0。因为
        判断障碍物越过只需要加一次分数，不然越过的障碍物一直在加分"""
        self.score
        tmp = self.score
        if tmp == 1:
            self.score_audio.play()
        self.score = 0
        return tmp
        
    def show_score(self, screen, score):
        self.score_digits = [int(x) for x in list(str(score))] # 显示分数的时候考虑其位数即可
        total_width = 0 # 要显示的数字的总宽度

        for digit in self.score_digits:
            total_width += self.scores[digit].get_width() # 图片的宽

        x_offset = (screen_width - (total_width+30)) # 分数横向位置

        for digit in self.score_digits:
            screen.blit(self.scores[digit], (x_offset, screen_height*0.1))
            x_offset += self.scores[digit].get_width()
