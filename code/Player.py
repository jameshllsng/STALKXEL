#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from code.Const import ENTITY_SHOT_DELAY, ENTITY_SPEED, GRAVITY_INTENSITY, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT, PLAYER_KEY_UP, JUMP_HEIGHT, VERTICAL_SPEED, WIN_WIDTH
from code.Entity import Entity
from code.PlayerShot import PlayerShot

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.surf = pygame.image.load('./asset/Player-stop.png').convert_alpha()
        self.surf_walk1 = pygame.image.load('./asset/Player-walk1.png').convert_alpha()
        self.surf_walk2 = pygame.image.load('./asset/Player-walk2.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], bottom=position[1])
        self.v_speed = VERTICAL_SPEED[self.name]
        self.j_height = JUMP_HEIGHT[self.name]
        self.g_intensity = GRAVITY_INTENSITY[self.name]
        self.jumping = False
        self.jump_allowed = True
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.current_frame = 0
        self.frame_counter = 0
        
    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_LEFT[self.name]] or pressed_key[PLAYER_KEY_RIGHT[self.name]]:
            self.frame_counter = self.frame_counter + 1
            if self.frame_counter == 8:
                self.frame_counter = 0
                self.current_frame = self.current_frame + 1
        
        if not pressed_key[PLAYER_KEY_UP[self.name]]:
            self.jump_allowed = True
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.jump_allowed == True and self.jumping == False:
            self.jumping = True
            self.jump_allowed = False
        if self.jumping:
                self.rect.y -= self.v_speed
                self.v_speed -= self.g_intensity
                if self.v_speed < -self.j_height:
                    self.jumping = False
                    self.v_speed = self.j_height
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            pressed_key = pygame.key.get_pressed()
            if pressed_key[PLAYER_KEY_SHOOT[self.name]]:
                return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))