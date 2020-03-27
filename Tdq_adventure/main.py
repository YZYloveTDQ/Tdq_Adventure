# _*_ encoding:utf-8 _*_
import pygame
from pygame.locals import* # 导入pygame中俄常量
import sys # 导入系统的模块
import random
from tdq_adventure.map import Map
from tdq_adventure.tdq import Tdq
from tdq_adventure.obstacle import Obstacle
from tdq_adventure.music_button import Music_button
from tdq_adventure.over import game_over


# -------窗口参数----------------------------
screen_width = 822
screen_height = 199
fps = 30 # 窗口画面刷新时间
screen = ''
fps_clock = ''

# -----主函数-------------------------------
def main():
    score = 0 # 得分
    over = False # 游戏结束标志
    global screen, fps_clock # 定义为全局变量
    pygame.init() # （6，0）pygame模块使用前的检测初始化
    
    # ------窗体-------------------
    fps_clock = pygame.time.Clock() # 使用时钟控制窗口循环多久刷新一次
    screen = pygame.display.set_mode((screen_width, screen_height)) # 创建一个窗体
    pygame.display.set_caption('超级唐邓琦')

    # ---创建地图---------------------
    """两个地图，一个在窗体那，一个在后面排队"""
    bg1 = Map(0, 0)
    bg2 = Map(800, 0)

    # ---创建人物-------------------
    tdq = Tdq()

    # ----创建障碍物----------------
    add_obstacle = 0
    obstacle_list = []

    # ----背景音乐按钮----------
    music_button = Music_button()
    btn_img = music_button.open_img # 设置默认音乐按钮
    music_button.bg_music.play() # 播放

    # =======窗体的刷新（核心函数）========
    while True:
        """窗体是持续刷新的"""
        for event in pygame.event.get(): # 获取单机事件
            # ----单机关闭---------
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit() # 退出窗口
                sys.exit() # 关闭窗口

            # ----是否按下空格跳跃-----------
            if event.type == KEYDOWN and event.key == K_SPACE:
                if tdq.rect.y >= tdq.y: # 在地面
                    tdq.jump()
                    tdq.jump_audio.play() # 播放音乐

            # -----判断是否点击音乐按钮----------
            if event.type == pygame.MOUSEBUTTONUP: # 鼠标是否点击
                if music_button.is_select(): # 鼠标在范围内
                    if music_button.is_open:
                        btn_img = music_button.close_img
                        music_button.is_open = False
                        music_button.bg_music.stop()
                    else:
                        btn_img = music_button.close_img
                        music_button.is_open = True
                        music_button.bg_music.play()
        
        if over == False:
            # ---地图更新---------------
            bg1.map_update(screen)
            bg1.map_rolling()
            bg2.map_update(screen)
            bg2.map_rolling()

            # ----人物更新--------------
            tdq.move()
            tdq.tdq_update(screen)

            # ----障碍物-------------
            if add_obstacle >= 1000:
                obstacle = Obstacle()
                obstacle_list.append(obstacle)
                add_obstacle = 0
            for i in range(len(obstacle_list)):
                obstacle_list[i].obstacle_move()
                obstacle_list[i].obstacle_update(screen)

                # ----是否发生碰撞---------------------------------
                if pygame.sprite.collide_rect(tdq, obstacle_list[i]):
                    over = True
                    music_button.bg_music.stop()
                    game_over(screen)
                else:
                    if (obstacle_list[i].rect.x + obstacle_list[i].rect.width) < tdq.rect.x:  # 越过了障碍物
                        score += obstacle_list[i].get_score()
                obstacle_list[i].show_score(screen, score)  # 显示分数

            add_obstacle += 30
        
        # ----音乐按钮--------
        screen.blit(btn_img, (20, 20))

        # ----更新整个窗体------
        pygame.display.update()
        fps_clock.tick(fps)


if __name__ == "__main__":
    main()
