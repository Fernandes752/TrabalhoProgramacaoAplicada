import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Meu Jogo")  # Título da janela
        self.clock = pygame.time.Clock()  # Controle de FPS

    def run(self):
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)

        menu = Menu(self.window)  # Inicializa o menu

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            menu.run()  # Renderiza o menu
            self.clock.tick(60)  # Limita a 60 FPS

        pygame.quit()
