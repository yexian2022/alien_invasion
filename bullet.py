#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022-09-02 15:21
# @Author  : 弦崽
# @Site    : 
# @File    : bullet.py
# @Software: PyCharm
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """管理飞船所有发射的子弹"""

    def __init__(self, ai_game):
        """在飞船当前位置创建一个子弹对象"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # 创建矩形必须要有位置信息
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # 储存用小数表示的子弹位置
        self.y = float(self.rect.y)

    def update(self):
        """向上移动子弹"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上画子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
