#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, MENU_OPTION, COLOR_WHITE, COLOR_NEON, COLOR_CIANO, COLOR_GREEN


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            # Desenhada as imagens
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(80, "Shadowed", COLOR_CIANO, ((WIN_WIDTH / 2), 150))
            self.menu_text(80, "Paths", COLOR_NEON, ((WIN_WIDTH / 2), 200))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(40, MENU_OPTION[i], COLOR_GREEN, ((WIN_WIDTH / 2), 630 + 40 * i))
                else:
                    self.menu_text(40, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 630 + 40 * i))

            pygame.display.flip()

            #  Checar todos os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Fechar janela
                    quit()  # Finalizar pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # Tecla para baixo
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # Tecla para cima
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:  # Enter
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucid Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
