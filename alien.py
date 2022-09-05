#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022-09-05 13:01
# @Author  : 弦崽
# @Site    : 
# @File    : alien.py
# @Software: PyCharm
import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    # 表示单个外星人的类
    def __init__(self, ai_game):
        # 初始化外星人，并给他个初始位置
        super().__init__()
        self.screen = ai_game.screen
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕的左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 储存单个外星人的精确水平位置
        self.x = float(self.rect.x)
