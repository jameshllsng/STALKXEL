#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from code.Const import ENTITY_SHOT_DELAY, ENTITY_SPEED, GRAVITY_INTENSITY, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT, PLAYER_KEY_UP, JUMP_HEIGHT, VERTICAL_SPEED, WIN_WIDTH
from code.Entity import Entity
from code.PlayerShot import PlayerShot

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.surf_stop = pygame.image.load('./asset/Player-stop.png').convert_alpha()
        self.surf_walk1 = pygame.image.load('./asset/Player-walk1.png').convert_alpha()
        self.surf_walk2 = pygame.image.load('./asset/Player-walk2.png').convert_alpha()
        self.surf_walkT = pygame.image.load('./asset/Player-walktransition.png').convert_alpha()
        self.surf_jump = pygame.image.load('./asset/Player-jump.png').convert_alpha()
        self.surf_shot = pygame.image.load('./asset/Player-attack.png').convert_alpha()
        self.surf = self.surf_stop
        self.rect = self.surf.get_rect(left=position[0], bottom=position[1])
        self.v_speed = VERTICAL_SPEED[self.name]
        self.j_height = JUMP_HEIGHT[self.name]
        self.g_intensity = GRAVITY_INTENSITY[self.name]
        self.jumping = False
        self.jump_allowed = True
        self.shot_delay = 0
        self.attack_counter = 0
        self.current_frame = 0
        self.frame_counter = 0
        self.gaze_direction = 'Right'
        
    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_LEFT[self.name]] or pressed_key[PLAYER_KEY_RIGHT[self.name]]:
            if pressed_key[PLAYER_KEY_RIGHT[self.name]]:
                self.gaze_direction = 'Right'
            elif pressed_key[PLAYER_KEY_LEFT[self.name]]:
                self.gaze_direction = 'Left'
            self.frame_counter = self.frame_counter + 1
            if self.frame_counter == 8:
                self.frame_counter = 0
                feet_position = self.rect.midbottom
                if self.current_frame == 0:
                    self.surf = self.surf_walk1
                    if self.gaze_direction == 'Left':
                        self.surf = pygame.transform.flip(self.surf_walk1, True, False)
                    self.rect = self.surf.get_rect(midbottom=feet_position)
                    self.current_frame = 1
                elif self.current_frame == 1:
                    self.surf = self.surf_walkT
                    if self.gaze_direction == 'Left':
                        self.surf = pygame.transform.flip(self.surf_walkT, True, False)
                    self.rect = self.surf.get_rect(midbottom=feet_position)
                    self.current_frame = 2
                elif self.current_frame == 2:
                    self.surf = self.surf_walk2
                    if self.gaze_direction == 'Left':
                        self.surf = pygame.transform.flip(self.surf_walk2, True, False)
                    self.rect = self.surf.get_rect(midbottom=feet_position)
                    self.current_frame = 3
                elif self.current_frame == 3:
                    self.surf = self.surf_walkT
                    if self.gaze_direction == 'Left':
                        self.surf = pygame.transform.flip(self.surf_walkT, True, False)
                    self.rect = self.surf.get_rect(midbottom=feet_position)
                    self.current_frame = 0
        else:
            feet_position = self.rect.midbottom
            self.surf = self.surf_stop
            if self.gaze_direction == 'Left':
                self.surf = pygame.transform.flip(self.surf_stop, True, False)
            self.rect = self.surf.get_rect(midbottom=feet_position)
            self.frame_counter = 0
            self.current_frame = 0
        if not pressed_key[PLAYER_KEY_UP[self.name]]:
            self.jump_allowed = True
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.jump_allowed == True and self.jumping == False:
            self.jumping = True
            self.jump_allowed = False
        feet_position = self.rect.midbottom
        if self.jumping:
            self.surf = self.surf_jump
            if self.gaze_direction == 'Left':
                self.surf = pygame.transform.flip(self.surf_jump, True, False)
            self.rect = self.surf.get_rect(midbottom=feet_position)
            self.rect.y -= self.v_speed
            self.v_speed -= self.g_intensity
            if self.v_speed < -self.j_height:
                self.jumping = False
                self.v_speed = self.j_height
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]

        if self.attack_counter > 0:
            feet_position = self.rect.midbottom
            self.surf = self.surf_shot
            if self.gaze_direction == 'Left':
                self.surf = pygame.transform.flip(self.surf_shot, True, False)
            self.rect = self.surf.get_rect(midbottom=feet_position)
            self.attack_counter -= 1

    def shoot(self):
        pressed_key = pygame.key.get_pressed()
        if self.shot_delay > 0:
            self.shot_delay -= 1
        feet_position = self.rect.midbottom
        if pressed_key[PLAYER_KEY_SHOOT[self.name]] and self.shot_delay == 0:
            self.surf = self.surf_shot
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            self.attack_counter = 10
            if self.gaze_direction == 'Left':
                self.surf = pygame.transform.flip(self.surf_shot, True, False)
            self.rect = self.surf.get_rect(midbottom=feet_position)
            if self.gaze_direction == 'Right':
                return PlayerShot(name=f'{self.name}Shot', position=(self.rect.right, self.rect.top + 10), direction='Right')
            elif self.gaze_direction == 'Left':
                return PlayerShot(name=f'{self.name}Shot', position=(self.rect.left - 44, self.rect.top + 10), direction='Left')
        