#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.Const import ENTITY_SPEED, PLAYER_KEY_RIGHT, WIN_WIDTH
from code.Entity import Entity

class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_RIGHT['Player1']]:
            self.rect.centerx -= ENTITY_SPEED[self.name]
            if self.rect.right <= 0:
                self.rect.left = WIN_WIDTH    
        
