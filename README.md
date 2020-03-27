# Tdq_Adventure
模仿“超级玛丽”小游戏

## 学习pygame模块的游戏开发
---

【1】pygame的核心：**窗口**
> 图片加载到窗口rect，操作对象为窗口
> 循环体中要进行screen.blit绘图



【2】窗口是一个fps刷新循环，绘制的过程

【3】坐标是从**左上角**开始的（0， 0）

【4】动图：图片的循环切换

【5】pyagme.init()：初始化检测，检测Pygame()的子模块
> pygame.displaay.init()

> pygame.font.init()

> pygame.joystick.init()

> pygame.mixer.init()

> pygame.cdrom.init()

> pygame.time.init()

> (6, 0)# (子模块正确数，错误数)


【6】地图的滚动：
> 创建两个地图对象，连续排列（通过坐标）

> 借助主循环向左移动坐标

> 移动出的图片重新赋给新的坐标位置（放到右边）

【7】人物的跳动
> 左上角为坐标开始点

> self.rect.size = self.img.get_size() # 获取窗口大小为图片大小

【8】判断按键
> for event in pygame.event.get():
    if event.type == KEYDOWN and event.key == K_SPACE # 按键类型为键盘 and 按键的具体位置

【9】退出程序
> pygame.quit() # 退出窗口，窗口还在运行

>sys.exit() 关闭窗口

【10】障碍物的创建
> **障碍物的创建要随着主循环持续创建**

> **障碍物本身也需要有循环持续跟踪，这样它才会持续移动**

【11】显示分数
> 只需要获取分数的位数上的数字即可

> int(x) for x in list(str(score))
---

## 困难
> 显示分数时，当跃过一个障碍物后，分数一直在增加

> 调试之后发现，原来因为循环中一直在判断这个障碍物跃过了，但是循环不能改，所以利用局部变量score=1，再重置为0使得在调用得分函数时，一个障碍物最多只会加一分
