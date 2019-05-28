import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
def run_game():
# 初始化背景设置
    pygame.init()                                      
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
# screen = pygame.display.set_mode((1200,800))      
# 创建一个名为screen的显示窗口，窗口的尺寸1200,800像素
    pygame.display.set_caption("Alien Invasion")
# 创建一艘飞船
    ship = Ship(screen)
# 设置背景色
# bg_color = (230,230,230)

    while True:
# 监听键盘和鼠标事件
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings,screen,ship)

run_game()
