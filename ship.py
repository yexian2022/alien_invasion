import pygame


class Ship:
    """管理飞船的类"""

    def __init__(self, ai_game):
        """初始化飞船，并设置初始属性"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        """加载飞船图像，并获取其外接矩形"""
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        """对于每艘新飞船，都将其放在屏幕底部的中央"""
        self.rect.midbottom = self.screen_rect.midbottom

        """飞船要有小数"""
        self.x = float(self.rect.x)

        """移动标志"""
        self.moving_left = False
        self.moving_right = False

    def updata(self):
        """根据飞船的移动标志来调整位置"""
        if self.moving_left:
            self.x -= self.settings.ship_speed
        if self.moving_right:
            self.x += self.settings.ship_speed

        # 根据self.x更新rect对象
        self.rect.x = self.x

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
