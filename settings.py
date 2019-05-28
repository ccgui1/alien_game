# 每次循环时都重绘屏幕
class Settings():
    """存储 外星人 的所有设置的类 """

    def __init__(self):
        """初始化游戏的设置"""

        # 屏幕设置
        self.screen_width = 640
        self.screen_height = 480
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_speed_factor = 1.5
