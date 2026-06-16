import pygame

from code.Const import ENTITY_SPEED
from code.Entity import Entity

class PlayerShot(Entity):
    def __init__(self, name: str, position: tuple, direction: str):
      super().__init__(name, position)
      self.shot_direction = direction

    def move(self):
      if self.shot_direction == 'Right':
        self.rect.centerx += ENTITY_SPEED[self.name]
      elif self.shot_direction == 'Left':
        self.rect.centerx -= ENTITY_SPEED[self.name]