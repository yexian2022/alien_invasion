import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏，并创建游戏资源"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        """设置背景颜色"""
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_enents()
            self.ship.updata()
            self._update_bullets()
            self._update_screen()

    def _check_enents(self):
        """监视键盘和鼠标"""
        for enent in pygame.event.get():
            if enent.type == pygame.QUIT:
                sys.exit()
            elif enent.type == pygame.KEYDOWN:
                self._check_keydown_enents(enent)
            elif enent.type == pygame.KEYUP:
                self._check_keyup_enents(enent)

    def _check_keydown_enents(self, enent):
        """响应按键"""
        if enent.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif enent.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif enent.key == pygame.K_q:
            sys.exit()
        elif enent.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_enents(self, enent):
        """响应松开"""
        if enent.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif enent.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_bullets(self):
        """更新子弹的位置并删除消失的子弹"""
        # 更新子弹的位置
        self.bullets.update()
        # 删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        print(len(self.bullets))

    def _update_screen(self):
        """每次循环时颜色重置"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        """让最近绘制的屏幕可以看到,刷新"""
        pygame.display.flip()

    def _fire_bullet(self):
        """创建一个子弹，并将其加入到编组bullets中"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


if __name__ == '__main__':
    """创建游戏实例，并运行游戏"""
    ai = AlienInvasion()
    ai.run_game()
