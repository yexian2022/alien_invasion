import sys
from time import sleep
import pygame

from settings import Settings
from game_stats import Gamestats
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏，并创建游戏资源"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        # 创建一个用于储存游戏统计信息的实例
        self.stats = Gamestats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        # 创建外星人群组
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        """设置背景颜色"""
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_enents()
            if self.stats.game_active:
                self.ship.updata()
                self._update_bullets()
                self._update_aliens()
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
        self._check_bullet_alien_collisions()

    def _update_screen(self):
        """每次循环时颜色重置"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)
        """让最近绘制的屏幕可以看到,刷新"""
        pygame.display.flip()

    def _fire_bullet(self):
        """创建一个子弹，并将其加入到编组bullets中"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):
        """创建外星人群组"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        # 计算屏幕可以容纳多少行外星人
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - 3 * alien_height - ship_height
        number_rows = available_space_y // (2 * alien_height)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        # 创建一个外星人
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_aliens(self):
        # 更新外星人的方法
        self._check_fleet_edgs()
        self.aliens.update()

        # 检查外星人是否跟飞船碰撞了
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # 检查是否有外星人到达屏幕底端
        self._check_aliens_bottom()

    def _check_fleet_edgs(self):
        # 判断是否碰到边缘
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        # 将整群外星人下移动，并改变他们的方向
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_bullet_alien_collisions(self):
        """
                检查是否有子弹击中外星人
                如果是，就删除相应的子弹和外星人
                """
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, False, True)
        # 如果外星人都没有了，就再创建一组新的外星人
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _ship_hit(self):
        """外星人撞到飞船"""
        if self.stats.ships_left > 0:
            # 将ships_left  -1
            self.stats.ships_left -= 1

            # 清空余下的外星人和子弹
            self.aliens.empty()
            self.bullets.empty()

            # 创建一群新的外星人，并将飞船放到屏幕底下中间
            self._create_fleet()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.stats.game_active = False

    def _check_aliens_bottom(self):
        """检查外星人是否到达屏幕低端"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # 跟处理外星人被碰撞一样处理
                self._ship_hit()
                break


if __name__ == '__main__':
    """创建游戏实例，并运行游戏"""
    ai = AlienInvasion()
    ai.run_game()
