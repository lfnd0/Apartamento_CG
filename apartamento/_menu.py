import sys, pygame
from pygame.locals import *
from pygame.constants import *
from _cena import Cena

class Menu():

    def iniciar(self):
        #criando ambiente
        pygame.init()
        pygame.mixer.init()
        tela = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption("Apartamento")
        tempo = pygame.time.Clock()
        imagemMenu = pygame.image.load("img/menu.jpg")
        pygame.mixer.music.load("sons/abertura.mp3")
        pygame.mixer.music.play(-1)
        
        while True:
            tempo.tick(30)

            for evento in pygame.event.get():
                if evento.type == QUIT:
                    pygame.quit()
                elif evento.type == KEYDOWN and evento.key == K_ESCAPE:
                    sys.exit()

                if evento.type == MOUSEBUTTONDOWN:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    # print(x)
                    # print(y)
                    if(x > 407.5 and x < 592.83 and y > 275.12 and y < 326.82):
                        pygame.mixer.music.load("sons/aperta_o_botao_jogar.mp3")
                        pygame.mixer.music.play()
                        pygame.time.delay(500)
                        cena = Cena()
                        cena.iniciar()
            tela.blit(imagemMenu, (0,0))
            pygame.display.update()