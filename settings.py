class Settings:
    """储存《外星人游戏》所有设置的类"""

    def __init__(self):
        """初始化所有设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # 飞船速度
        self.ship_speed = 1.5
        self.ship_limit = 1

        # 子弹设置
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 5
        # 外星人设置
        self.alien_speed = 0.2
        self.fleet_drop_speed = 10
        # 设置外星人移动的方向1向右 -1向左
        self.fleet_direction = 1
        # 加快游戏节奏的速度
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # 初始化随游戏进行而变化的设置
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 0.2
        # fleet_direction 为1表示向右，为-1表示向左
        self.fleet_direction = 1
        # 计分
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
