#!/opt/anaconda3/envs/typegame/bin/python
import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("打字游戏")

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 游戏主循环
running = True
while running:
    screen.fill(WHITE)  # 清屏
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # 关闭游戏

    pygame.display.flip()  # 刷新屏幕

pygame.quit()
