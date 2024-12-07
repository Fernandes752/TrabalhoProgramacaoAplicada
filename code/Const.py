import pygame

# C

COLOR_WHITE = (180, 220, 220)
COLOR_CIANO = (0, 255, 200)
COLOR_NEON = (0, 100, 80)
COLOR_GREEN = (0, 255, 100)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
    'Player1': 8,
    'Player2': 8,
    'Enemy1': 3,
    'Enemy2': 2,
    'Enemy3': 4,
    'Enemy4': 3
}

# M
MENU_OPTION = ('Novo Jogo - 1 Jogador',
               'Novo Jogo - 2 Jogadores - Cooperativo',
               'Novo Jogo - 2 Jogadores - Competitivo',
               'Recordes',
               'Sair')

# P

PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                    'Player2': pygame.K_LCTRL}

# S
SPAWN_TIME = 4000
# w
WIN_WIDTH = 1400
WIN_HEIGHT = 1000
