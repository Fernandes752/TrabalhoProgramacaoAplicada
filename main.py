import pygame

print('Setup Start')
pygame.init()
window = pygame.display.set_mode(size=(600, 480))
print('Setup End')

print('Loop Start')
while True:
    # Cheque todos os eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Saindo...')
            pygame.quit()  # Fechar janela
            quit()  # fechar o pygame
