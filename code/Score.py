import sys
from datetime import datetime

import pygame
from pygame import Surface, Rect, KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font

from code.Const import SCORE_POS, MENU_OPTION, C_ORANGE
from code.DBProxy import DBProxy


class Score:

    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/Score.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def save(self, game_mode: str, player_score: list[int]):
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)
        db_proxy = DBProxy('DBScore')
        name = ''

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(100, 'Você ganhou!', (255, 140, 0), SCORE_POS['Title'])
            text = 'Coloque o nome do Jogador 1! (4 caracteres):'
            score = player_score[0]
            if game_mode == MENU_OPTION[0]:
                score = player_score[0]
            if game_mode == MENU_OPTION[1]:
                score = (player_score[0] + player_score[1]) / 2
                text = 'Coloque o nome do time! (4 caracteres):'
            if game_mode == MENU_OPTION[2]:
                if player_score[0] >= player_score[1]:
                    score = player_score[0]
                    text = 'Coloque o nome do Jogador 1! (4 caracteres):'
                else:
                    score = player_score[1]
                    text = 'Coloque o nome do Jogador 2! (4 caracteres):'
            self.score_text(60, text, (240, 230, 200), SCORE_POS['EnterName'])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 4:
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                        self.show()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name += event.unicode
            self.score_text(60, name, (255, 69, 0), SCORE_POS['Name'])
            pygame.display.flip()
            pass

    def show(self):
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(130, 'TOP 10 SCORE', (255, 215, 0), SCORE_POS['Title'])
        self.score_text(90, 'NAME SCORE DATE ', (255, 165, 0), SCORE_POS['Label'])
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for player_score in list_score:
            id, name, score, date = player_score
            self.score_text(20, f'{name} {score :05d} {date}', C_ORANGE,
                            SCORE_POS[list_score.index(player_score)])

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucid Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)


def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"