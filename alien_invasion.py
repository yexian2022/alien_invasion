import sys
import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏，并创建游戏资源"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

        """设置背景颜色"""
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_enents()
            self.ship.updata()
            self._update_screen()

    def _check_enents(self):
        """监视键盘和鼠标"""
        for enent in pygame.event.get():
            if enent.type == pygame.QUIT:
                sys.exit()
            elif enent.type == pygame.KEYDOWN:
                if enent.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif enent.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif enent.type == pygame.KEYUP:
                if enent.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif enent.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        """每次循环时颜色重置"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        """让最近绘制的屏幕可以看到,刷新"""
        pygame.display.flip()


if __name__ == '__main__':
    """创建游戏实例，并运行游戏"""
    ai = AlienInvasion()
    ai.run_game()
