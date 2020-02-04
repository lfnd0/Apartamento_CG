import sys, pygame
from pygame.locals import *
from pygame.constants import *
from OpenGL.GL import *
from OpenGL.GLU import *
from _OBJFileLoader import *
from _iluminacao import *

class Cena():

    def iniciar(self):
        from _menu import Menu
        menu = Menu()
        
        pygame.init()
        pygame.mixer.init()
        viewport = (1000, 600)
        tela = pygame.display.set_mode(viewport, OPENGL | DOUBLEBUF)
        pygame.display.set_caption("Apartamento")
        tempo = pygame.time.Clock()
        pygame.mixer.music.load("sons/cena.mp3")
        pygame.mixer.music.play(-1)

        paredes = [
            OBJ('parede_1.obj'),
            OBJ('parede_2.obj'),
            OBJ('parede_3.obj'),
            OBJ('parede_4.obj'),
            OBJ('parede_5.obj'),
            OBJ('parede_6.obj'),
            OBJ('parede_7.obj'),
            OBJ('parede_8.obj'),
            OBJ('parede_9.obj'),
            OBJ('parede_10.obj'),
            OBJ('parede_11.obj'),
            OBJ('parede_12.obj'),
            OBJ('parede_13.obj'),
            OBJ('parede_14.obj'),
            OBJ('parede_15.obj')
        ]

        porta_fora_2 = OBJ("colisao_porta_2.obj",isTrigger=True)
        porta_dentro_2 = OBJ("colisao_quarto_porta_2.obj",isTrigger=True)

        porta_fora_3 = OBJ("colisao_porta_3.obj",isTrigger=True)
        porta_dentro_3 = OBJ("colisao_banheiro_porta_3.obj",isTrigger=True)

        acabamento_1 = OBJ('acabamento_1.obj')
        acabamento_2 = OBJ('acabamento_2.obj')

        porta_1 = OBJ('porta_1.obj')
        porta_2 = OBJ('porta_2.obj')
        porta_3 = OBJ('porta_3.obj')

        piso_1 = OBJ('piso_1.obj')
        piso_2 = OBJ('piso_2.obj')
        piso_3 = OBJ('piso_3.obj')

        tomme = OBJ('tomme.obj', pos=[0, 0, 0])

        fogao = OBJ('fogao.obj')
        pia_geladeira = OBJ('pia_geladeira.obj')
        tapete_1 = OBJ('tapete_1.obj')
        tomadas = OBJ('tomadas.obj')

        tapete_2 = OBJ('tapete_2.obj')
        rack_1_TV = OBJ('rack_1_TV.obj')
        sofa = OBJ('sofa.obj')
  
        cama = OBJ('cama.obj')
        guarda_roupa = OBJ('guarda_roupa.obj')
        rack_2 = OBJ('rack_2.obj')

        vaso_sanitario = OBJ('vaso_sanitario.obj')
        pia_banheiro = OBJ('pia_banheiro.obj')
        banheira = OBJ('banheira.obj')
        rack_3 = OBJ('rack_3.obj')

        colisoes_sala_cozinha = [fogao, pia_geladeira, rack_1_TV, sofa] # acabamento_1, acabamento_2, sofa
        for i in range(len(paredes)):
            colisoes_sala_cozinha.append(paredes[i])

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        #mouse camera
        width, height = viewport
        gluPerspective(70.0, width/float(height), 1, 100.0)
        glEnable(GL_DEPTH_TEST)
        glMatrixMode(GL_MODELVIEW)
        rx, ry = (-90,88)
        tx, ty = (4, -1)
        zpos = 9

        rotacao_tomme = 0
        rotacao_mouse = False
        mover_camera = False

        mover_para_frente = False
        mover_para_tras    = False
        mover_para_esquerda    = False
        mover_para_direita   = False
        mover_tomme   = 0.2

        abrir_porta_2 = False
        abrir_porta_3 = False

        luz_ligada = False
        
        colisoes_quarto = [paredes[8], paredes[9], paredes[10], cama, guarda_roupa, rack_2, OBJ('porta_aberta_2.obj')]
        colisoes_banheiro = [paredes[3], paredes[4], paredes[5], vaso_sanitario, pia_banheiro, banheira, rack_3, OBJ('porta_aberta_3.obj')]

        while True:
            tempo.tick(30)

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glLoadIdentity()

            # renderizar objetos ================
            glPushMatrix()
            glTranslate(tx/20., ty/20., - zpos)
            glRotate(ry, 1, 0, 0)
            glRotate(rx, 0, 1, 0)

            # iluminação ================
            iluminacao_da_cena(luz_ligada)
            
            for parede in paredes:
                parede.render()
            acabamento_1.render()
            acabamento_2.render()
            
            porta_1.render()
            
            if(abrir_porta_2):
                porta_2 = OBJ('porta_aberta_2.obj')
                porta_2.render()            
            else:
                porta_2 = OBJ('porta_2.obj')
                porta_2.render()
            if(abrir_porta_3):
                porta_3 = OBJ('porta_aberta_3.obj')
                porta_3.render()
            else:
                porta_3 = OBJ('porta_3.obj')
                porta_3.render()    
            
            piso_1.render()
            piso_2.render()
            piso_3.render()
            tomme.render()

            fogao.render()
            pia_geladeira.render()
            tomadas.render()
            # tomada_1.render()
            # tomada_2.render()
            tapete_1.render()
            
            rack_1_TV.render()
            sofa.render()
            tapete_2.render()

            cama.render()
            guarda_roupa.render()
            rack_2.render()

            vaso_sanitario.render()
            pia_banheiro.render()
            banheira.render()
            rack_3.render()

            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                elif e.type == KEYDOWN:
                    if e.key == K_w:
                        mover_para_frente = True
                    elif e.key == K_s:
                        mover_para_tras    = True
                    elif e.key == K_a:
                        mover_para_esquerda    = True
                    elif e.key == K_d:
                        mover_para_direita   = True  
                    if e.key == K_q:
                        if luz_ligada:
                            luz_ligada = False
                        else:
                            luz_ligada = True
                    elif e.key == K_ESCAPE:
                        sys.exit()               
                elif e.type == KEYUP:
                    if e.key == K_w:
                        mover_para_frente = False
                    elif e.key == K_s:
                        mover_para_tras    = False
                    elif e.key == K_a:
                        mover_para_esquerda    = False
                    elif e.key == K_d:
                        mover_para_direita   = False

                elif e.type == MOUSEBUTTONDOWN:
                    if e.button == 4:
                        zpos = max(1, zpos-1)
                    elif e.button == 5:
                        zpos += 1
                    elif e.button == 1:
                        rotacao_mouse = True
                    elif e.button == 3:
                        mover_camera = True
                elif e.type == MOUSEBUTTONUP:
                    if e.button == 1:
                        rotacao_mouse = False
                    elif e.button == 3:
                        mover_camera = False
                elif e.type == MOUSEMOTION:
                    i, j = e.rel
                    if rotacao_mouse:
                        rx += i
                        ry += j
                    if mover_camera:
                        tx += i
                        ty -= j

            if(abrir_porta_2):
                colisao_tomme = chek_collisions(tomme, colisoes_quarto)
            elif(abrir_porta_3):
                colisao_tomme = chek_collisions(tomme, colisoes_banheiro)
            else:
                colisao_tomme = chek_collisions(tomme, colisoes_sala_cozinha)
            colisao_porta_2 = chek_collisions(tomme,[porta_fora_2, porta_dentro_2])
            colisao_porta_3 = chek_collisions(tomme,[porta_fora_3, porta_dentro_3])

            # porta_dentro_2
            # colisao_porta_3 = chek_collisions(tomme,[local_fora_porta_3])

            if colisao_porta_2['right'] != 0 or colisao_porta_2['left'] != 0 or colisao_porta_2['up'] != 0 or colisao_porta_2['down'] != 0:
                abrir_porta_2 = True
            else:
                abrir_porta_2 = False
            if colisao_porta_3['right'] != 0 or colisao_porta_3['left'] != 0 or colisao_porta_3['up'] != 0 or colisao_porta_3['down'] != 0:
                abrir_porta_3 = True
            else:
                abrir_porta_3 = False

            if (mover_para_frente and colisao_tomme['up'] == 0):
                posicao = list(tomme.pos)       
                posicao[0] -= mover_tomme
                tomme.pos = tuple(posicao)
            elif (mover_para_tras and colisao_tomme['down'] == 0): 
                posicao = list(tomme.pos)    
                posicao[0] += mover_tomme
                tomme.pos = tuple(posicao)
            elif (mover_para_esquerda and colisao_tomme['left'] == 0):
                posicao = list(tomme.pos)    
                posicao[2] += mover_tomme
                tomme.pos = tuple(posicao)
            elif (mover_para_direita and colisao_tomme['right'] == 0):
                posicao = list(tomme.pos)
                posicao[2] -= mover_tomme
                tomme.pos = tuple(posicao)

            glPopMatrix()
            pygame.display.flip()