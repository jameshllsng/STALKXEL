#!/usr/bin/python
# -*- coding: utf-8 -*-
from pygame import Rect, Surface
from pygame.font import Font
import pygame.image
from code.Const import C_CYAN, C_GREEN, C_WHITE, C_YELLOW, MENU_OPTION, WIN_WIDTH

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left = 0, top = 0)

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "STALKXEL", C_GREEN, ((WIN_WIDTH/2), 70))
            self.menu_text(20, "Controls:", C_CYAN, (100, 275))
            self.menu_text(20, "ARROWS - Move / Jump", C_CYAN, (125, 295))
            self.menu_text(20, "RIGHT CTRL - Shoot", C_CYAN, (115, 315))
            self.menu_text(20, "ENTER - Select", C_CYAN, (90, 335))
            self.menu_text(20, "ESC - Back (on score screen)", C_CYAN, (175, 355))
            
            self.menu_text(20, "Objective:", C_CYAN, (700, 275))
            self.menu_text(20, "Reach the other ", C_CYAN, (690, 295))
            self.menu_text(20, "side of the map", C_CYAN, (680, 315))
            self.menu_text(20, "before timeout", C_CYAN, (690, 335))
            
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], C_YELLOW, ((WIN_WIDTH/2), 200 + 25 * i))
                else:  
                    self.menu_text(20, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH/2), 200 + 25 * i))
                        
            #Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # Close window
                    quit() # End pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN: # DOWN KEY
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP: # UP KEY
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN: #ENTER
                        return MENU_OPTION[menu_option]
                
            pygame.display.flip()
            
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)