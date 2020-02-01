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
        pygame.mixer.music.load("sons/fundo.mp2")
        pygame.mixer.music.play(-1)

        glLightfv(GL_LIGHT0, GL_POSITION,  (-40, 200, 100, 0.0))
        glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
        glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
        glEnable(GL_LIGHT0)
        glEnable(GL_LIGHTING)
        glEnable(GL_COLOR_MATERIAL)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH) # shaders

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
            OBJ('parede_13.obj')
        ]

        acabamento_1 = OBJ('acabamento_1.obj')
        acabamento_2 = OBJ('acabamento_2.obj')

        porta_1 = OBJ('porta_1.obj')
        porta_2 = OBJ('porta_2.obj')
        porta_3 = OBJ('porta_3.obj')

        piso_1 = OBJ('piso_1.obj')
        piso_2 = OBJ('piso_2.obj')
        piso_3 = OBJ('piso_3.obj')

        colisoes = [acabamento_1, acabamento_2]
        for i in range(len(paredes)):
            # if i not in [15, 18, 21]:
            colisoes.append(paredes[i])

        tomme = OBJ('tomme.obj', pos=[0, 0, 0])

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        width, height = viewport
        gluPerspective(70.0, width/float(height), 1, 100.0)
        glEnable(GL_DEPTH_TEST)
        glMatrixMode(GL_MODELVIEW)

        rx, ry = (-90,88)
        tx, ty = (4, -1)
        zpos = 9

        rotacao_tomme = 0
        rotacao_mouse = False
        move = False

        move_forward = False
        move_back    = False
        move_left    = False
        move_right   = False
        move_speed   = 0.1

        estadoluz0 = 1
        estadoluz1 = 0
        estadoluz2 = 0

        while True:
            tempo.tick(30)

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glLoadIdentity()

            # renderizar objetos ================
            glPushMatrix()
            glTranslate(tx/20., ty/20., - zpos)
            glRotate(ry, 1, 0, 0)
            glRotate(rx, 0, 1, 0)
            
            for parede in paredes:
                parede.render()
            acabamento_1.render()
            acabamento_2.render()
            porta_1.render()
            porta_2.render()
            porta_3.render()
            piso_1.render()
            piso_2.render()
            piso_3.render()
            tomme.render()

            for e in pygame.event.get():
                if e.type == QUIT:
                    menu.iniciar()
                elif e.type == KEYDOWN:
                    if e.key == K_w:
                        move_forward = True
                    elif e.key == K_s:
                        move_back    = True
                    elif e.key == K_a:
                        move_left    = True
                    elif e.key == K_d:
                        move_right   = True
                    elif e.key == K_RIGHT:
                        tomme
                        glRotate(90, 0, 1, 0)
                        rotacao_tomme += 90
                        if rotacao_tomme == 360:
                            rotacao_tomme = 0
                    elif e.key == K_LEFT:
                        tomme
                        glRotate(-90, 0, 1, 0)
                        rotacao_tomme -= 90
                        if rotacao_tomme == -360:
                            rotacao_tomme = 0  

                    if e.key == K_0: # 0
                        if estadoluz0 == 0:
                            estadoluz0 = 1
                            #glEnable(GL_LIGHT0)
                        else:
                            estadoluz0 = 0
                            #glDisable(GL_LIGHT0)
                    if e.key == K_1:
                        if estadoluz1 == 0:
                            estadoluz1 = 1
                            #glEnable(GL_LIGHT1)
                        else:
                            estadoluz1 = 0
                            #glDisable(GL_LIGHT1)
                    if e.key == K_2:
                        if estadoluz2 == 0:
                            estadoluz2 = 1
                            #glEnable(GL_LIGHT2)
                        else:
                            estadoluz2 = 0
                            #glDisable(GL_LIGHT2)

                    elif e.key == K_ESCAPE:
                        menu.iniciar()
                
                elif e.type == KEYUP:
                    if e.key == K_w:
                        move_forward = False
                    elif e.key == K_s:
                        move_back    = False
                    elif e.key == K_a:
                        move_left    = False
                    elif e.key == K_d:
                        move_right   = False

                elif e.type == MOUSEBUTTONDOWN:
                    if e.button == 4:
                        zpos = max(1, zpos-1)
                    elif e.button == 5:
                        zpos += 1
                    elif e.button == 1:
                        rotacao_mouse = True
                    elif e.button == 3:
                        move = True
                elif e.type == MOUSEBUTTONUP:
                    if e.button == 1:
                        rotacao_mouse = False
                    elif e.button == 3:
                        move = False
                elif e.type == MOUSEMOTION:
                    i, j = e.rel
                    if rotacao_mouse:
                        rx += i
                        ry += j
                    if move:
                        tx += i
                        ty -= j

            a = chek_collisions(tomme, colisoes)

            # ===========================================================
            #============== movimentacao =================
            if move_forward:
                posicao = list(tomme.pos)
                if rotacao_tomme == 0 and a['up'] == 0:          
                    posicao[0] -= move_speed
                    tomme.pos = tuple(posicao)
                elif ((rotacao_tomme == 90 or rotacao_tomme == -270) and a['right'] == 0):
                    posicao[2] -= move_speed
                    tomme.pos = tuple(posicao)
                elif ((rotacao_tomme == 180 or rotacao_tomme == -180) and a['down'] == 0):
                    posicao[0] += move_speed
                    tomme.pos = tuple(posicao)
                elif ((rotacao_tomme == 270 or rotacao_tomme == -90) and a['left'] == 0):
                    posicao[2] += move_speed
                    tomme.pos = tuple(posicao)
            elif move_back: 
                posicao = list(tomme.pos)    
                if (rotacao_tomme == 0 and a['down'] == 0):
                    posicao[0] += move_speed
                    tomme.pos = tuple(posicao)
                elif ((rotacao_tomme == 90 or rotacao_tomme == -270) and a['left'] == 0):
                    posicao[2] += move_speed
                    tomme.pos = tuple(posicao)
                elif ((rotacao_tomme == 180 or rotacao_tomme == -180) and a['up'] == 0):
                    posicao[0] -= move_speed
                    tomme.pos = tuple(posicao)
                elif ((rotacao_tomme == 270 or rotacao_tomme == -90) and a['right'] == 0):
                    posicao[2] -= move_speed
                    tomme.pos = tuple(posicao)
            elif move_left:
                posicao = list(tomme.pos)    
                if (rotacao_tomme == 0 and a['left'] == 0):
                    posicao[2] += move_speed
                    tomme.pos = tuple(posicao)
                elif ((rotacao_tomme == 90 or rotacao_tomme == -270) and a['up'] == 0):
                    posicao[0] -= move_speed
                    tomme.pos = tuple(posicao)
                elif ((rotacao_tomme == 180 or rotacao_tomme == -180) and a['right'] == 0):
                    posicao[2] -= move_speed
                    tomme.pos = tuple(posicao)
                elif ((rotacao_tomme == 270 or rotacao_tomme == -90) and a['down'] == 0):
                    posicao[0] += move_speed
                    tomme.pos = tuple(posicao)
            elif move_right:
                posicao = list(tomme.pos)
                if (rotacao_tomme == 0 and a['right'] == 0):
                    posicao[2] -= move_speed
                    tomme.pos = tuple(posicao)
                elif ((rotacao_tomme == 90 or rotacao_tomme == -270) and a['down'] == 0):
                    posicao[0] += move_speed
                    tomme.pos = tuple(posicao)
                elif ((rotacao_tomme == 180 or rotacao_tomme == -180) and a['left'] == 0):
                    posicao[2] += move_speed
                    tomme.pos = tuple(posicao)
                elif ((rotacao_tomme == 270 or rotacao_tomme == -90) and a['up'] == 0):
                    posicao[0] -= move_speed
                    tomme.pos = tuple(posicao)

            glPopMatrix()
            pygame.display.flip()