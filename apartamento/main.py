# botao esquerdo: girar objeto
# botao direito: mover objeto
# scroll: zoom

# from sys import argv
import sys, pygame
from pygame.locals import *
from pygame.constants import *
from OpenGL.GL import *
from OpenGL.GLU import *
# modulo para carregar obj
from objloader import *
from util import *
# from luz import *
# from abajur import *





from camera import Camera




# glutInit(argv)
# glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH)
# glutInitWindowSize(0,0)
# glutCreateWindow(b"Casa")

pygame.init()
viewport = (1280, 720)
# hx = viewport[0]/2
# hy = viewport[1]/2
srf = pygame.display.set_mode(viewport, OPENGL | DOUBLEBUF)

glLightfv(GL_LIGHT0, GL_POSITION,  (-40, 200, 100, 0.0))
glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
glEnable(GL_LIGHT0)
glEnable(GL_LIGHTING)
glEnable(GL_COLOR_MATERIAL)
glEnable(GL_DEPTH_TEST)
glShadeModel(GL_SMOOTH) # shader

# carrega o obj
# gabriel ===============================
# walls = [
# 		OBJ("wall_01.obj"),
# 		OBJ("wall_02.obj"),
# 		OBJ("wall_03.obj"),
# 		OBJ("wall_04.obj"),
# 		OBJ("wall_05.obj"),
# 		OBJ("wall_06.obj"),
# 		OBJ("wall_07.obj"),
# 		OBJ("wall_08.obj"),
# 		OBJ("wall_09.obj"),
# 		OBJ("wall_10.obj"),
# 		OBJ("wall_11.obj"),
# 		OBJ("wall_12.obj"),
# 		OBJ("wall_13.obj"),
# 		OBJ("wall_14.obj"),
# 		OBJ("wall_15.obj"),
# 		OBJ("wall_16.obj"),
# 		OBJ("wall_17.obj"),
# 		OBJ("wall_18.obj"),
# 		OBJ("wall_19.obj"),
# 		OBJ("wall_20.obj"),
# 		OBJ("wall_21.obj"),
# 		OBJ("wall_22.obj"),
# 		OBJ("wall_23.obj"),
# 		OBJ("wall_24.obj"),
# 		]

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

# walls  = OBJ("walls.obj", swapyz=True)
# door   = OBJ("door.obj",scale=[.8,.8,.9],pos=[7,0,-3.35],rot=[0,90,0])
# door2  = OBJ("door.obj",scale=[.8,.8,.9],pos=[6.84,0,6.9],rot=[0,0,0])
# door3  = OBJ("door.obj",scale=[.8,.8,.9],pos=[0,0,-6.8],rot=[0,0,0])

acabamento_1 = OBJ('acabamento_1.obj')
acabamento_2 = OBJ('acabamento_2.obj')

porta_1 = OBJ('porta_1.obj')
porta_2 = OBJ('porta_2.obj')
porta_3 = OBJ('porta_3.obj')

# porta_banheiro  = OBJ("door.obj",scale=[.8,.8,.9],pos=[0,0,1.2], rot=[0,0,0])
# porta_quarto    = OBJ("door.obj",scale=[.8,.8,.9],pos=[-5,0,-.9],rot=[0,90,0])
# porta_quarto2   = OBJ("door.obj",scale=[.8,.8,.9],pos=[-2.7,0,-1.2],rot=[0,0,0])

# clock_     = OBJ("clock.obj", pos=[-2,3,-4])
# clock_p1   = OBJ("clock_p1.obj",pos=[-2,3,-4],rot=[0,0,0])
# clock_p2   = OBJ("clock_p2.obj",pos=[-2,3,-4],rot=[0,0,0])

piso_1 = OBJ('piso_1.obj')
piso_2 = OBJ('piso_2.obj')
piso_3 = OBJ('piso_3.obj')

# window = OBJ("window.obj")
# floor  = OBJ("floor.obj" )
# couch  = OBJ("couch.obj", pos=[0,0,0] )
# table  = OBJ("table.obj" )
# scream = OBJ("ogrito.obj")
# carpet = OBJ("carpet.obj")
# # artur =================================
# pia     = OBJ("pia.obj")
# fogao   = OBJ("fogao.obj",   pos=[3.20, 0.90, 1.30] )
# estante = OBJ("estante.obj", pos=[3.85, -0.39, 5.6])
# tapete  = OBJ("tapete.obj")
# # nao confie no pae ====================
# cama1     = OBJ("bed.obj")
# wardrobe1 = OBJ("wardrobe.obj")
# cama2     = OBJ("bed.obj", pos=[0,0,-10])
# wardrobe2 = OBJ("wardrobe.obj", pos=[0,0,-10])
# # paulo ===============================
# bathtub = OBJ("bathtub.obj")
# sink    = OBJ("sink.obj")
# toilet  = OBJ("toilet.obj")

# trigger_banheiro = OBJ("trigger_banheiro.obj",isTrigger=True)
# trigger_quarto   = OBJ("trigger_quarto.obj", isTrigger=True)
# trigger_quarto2  = OBJ("trigger_quarto2.obj", isTrigger=True)
# trigger_quarto3  = OBJ("trigger_quarto3.obj", isTrigger=True)

# collision_mask = [couch,table,pia,fogao,estante,cama1,cama2,wardrobe1,wardrobe2,bathtub,sink,toilet]
# for x in range (len(walls)):
# 	if x not in [15,18,21]: #3,6,10   sao as de fora
# 		collision_mask.append(walls[x])

colisoes = [acabamento_1, acabamento_2]
for i in range(len(paredes)):
    if i not in [15, 18, 21]:
        colisoes.append(paredes[i])

tomme = OBJ('tomme.obj', pos=[0, 0, 0])
camera = Camera((0, 1, 0), (10, 2 , 0), (0, 1, 0), tomme)
# personagem = OBJ("cubo.obj", pos=[0,0,0])
# mesinha = OBJ("cubo.obj",pos=[-3,0,3])

clock = pygame.time.Clock()

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
width, height = viewport
gluPerspective(70.0, width/float(height), 1, 100.0)
glEnable(GL_DEPTH_TEST)
glMatrixMode(GL_MODELVIEW)



# rx, ry = (0,0)
# tx, ty = (0,0)
# zpos = 5

rx, ry = (-90, 90)
tx, ty = (20, 20)
zpos = 20

rotate = move = False

move_forward = False
move_back    = False
move_left    = False
move_right   = False
move_speed   = 0.1
cam_move_speed = 0

# animacao das portas
# open_speed = 6
# abrir_banheiro = False
# abrir_quarto   = False
# abrir_quarto2  = False

# Luz
estadoluz0 = 1
estadoluz1 = 0
estadoluz2 = 0

while True:
    clock.tick(30)
    
    for e in pygame.event.get():
        if e.type == QUIT:
            sys.exit()
        elif e.type == KEYDOWN:
            if e.key == K_w:
                move_forward = True
            elif e.key == K_s:
                move_back    = True
            elif e.key == K_a:
                move_left    = True
            elif e.key == K_d:
                move_right   = True
            elif e.key == K_ESCAPE: sys.exit()
            
            # iluminação
            # if e.key == K_0: # 0
            #     if estadoluz0 == 0:
            #         estadoluz0 = 1
            #         #glEnable(GL_LIGHT0)
            #     else:
            #         estadoluz0 = 0
            #         #glDisable(GL_LIGHT0)
            # if e.key == K_1:
            #     if estadoluz1 == 0:
            #         estadoluz1 = 1
            #         #glEnable(GL_LIGHT1)
            #     else:
            #         estadoluz1 = 0
            #         #glDisable(GL_LIGHT1)
            # if e.key == K_2:
            #     if estadoluz2 == 0:
            #         estadoluz2 = 1
            #         #glEnable(GL_LIGHT2)
            #     else:
            #         estadoluz2 = 0
            #         #glDisable(GL_LIGHT2)
        
        elif e.type == KEYUP:
            if e.key == K_w:
                move_forward = False
            elif e.key == K_s:
                move_back    = False
            elif e.key == K_a:
                move_left    = False
            elif e.key == K_d:
                move_right   = False
            elif e.key == K_RIGHT:
                camera.rotate(1, 0, 1, 0)
            elif e.key == K_LEFT:
                camera.rotate(-1, 0, 1, 0)

        elif e.type == MOUSEBUTTONDOWN:
            if e.button == 4: zpos = max(1, zpos-1)
            elif e.button == 5: zpos += 1
            elif e.button == 1: rotate = True
            elif e.button == 3: move = True
        elif e.type == MOUSEBUTTONUP:
            if e.button == 1: rotate = False
            elif e.button == 3: move = False
        elif e.type == MOUSEMOTION:
            i, j = e.rel
            if rotate:
                rx += i
                ry += j
            if move:
                tx += i
                ty -= j
    # colisao geral =========================================
    # a = chek_collisions(personagem,collision_mask)
    # colisao com triggers =====================================
    # t_banheiro = chek_collisions(personagem,[trigger_banheiro])
    # t_quarto   = chek_collisions(personagem,[trigger_quarto2])
    # t_quarto_2 = chek_collisions(personagem,[trigger_quarto3])
    # t_quarto2  = chek_collisions(personagem,[trigger_quarto])
    #===========================================================
    a = chek_collisions(tomme, colisoes)

    # condicao do trigger para animar portas =====================
    # if t_banheiro['left'] != 0:
    # 	abrir_banheiro = True
    # else: abrir_banheiro = False

    # if t_quarto['right'] != 0 or t_quarto_2['up'] != 0:
    # 	abrir_quarto = True
    # else: abrir_quarto = False

    # if t_quarto2['right'] != 0:
    # 	abrir_quarto2 = True
    # else: abrir_quarto2 = False
    # ===========================================================
    #============== movimentacao =================
    if move_forward and a['up'] == 0:
        camera.move(-move_speed, 0, 0)
        #tomme.pos[0] -= move_speed
        #ty -= cam_move_speed

    elif move_back and a['down'] == 0:
        camera.move(move_speed, 0, 0)
        #tomme.pos[0] += move_speed
        #ty += cam_move_speed

    elif move_left and a['left'] == 0:
        camera.move(0, 0, move_speed)
        #tomme.pos[2] += move_speed
        #tx += cam_move_speed

    elif move_right and a['right'] == 0:
        camera.move(0, 0, -move_speed)
        #tomme.pos[2] -= move_speed
        #tx -= cam_move_speed
    #=============================================

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # renderizar objetos ================
    glPushMatrix()
    """glTranslate(tx/20., ty/20., - zpos)
    glRotate(ry, 1, 0, 0)
    glRotate(rx, 0, 1, 0)"""

    camera.view()

    # iluminação ================
    # iluminacao_da_cena(estadoluz0, estadoluz1, estadoluz2)

    # ============ estrutura =============
    # for wall in walls:
    #     wall.render()

    for parede in paredes:
        parede.render()

    acabamento_1.render()
    acabamento_2.render()

    porta_1.render()
    porta_2.render()
    porta_3.render()

    # door.render()
    # door2.render()
    # door3.render()

    # portas animadas ==================================
    # ######## banheiro
    # porta_banheiro.render()
    # if(abrir_banheiro):
    # 	if (porta_banheiro.rot[1] < 150): porta_banheiro.rot[1] += 1 * open_speed
    # 	else: abrir_banheiro = False
    # else:
    # 	if (porta_banheiro.rot[1] > 0): porta_banheiro.rot[1] -= 1 * open_speed
    # # ######## quarto
    # porta_quarto.render()
    # if(abrir_quarto):
    # 	if (porta_quarto.rot[1] > 0): porta_quarto.rot[1] -= 1 * open_speed
    # 	else: abrir_quarto = False
    # else:
    # 	if (porta_quarto.rot[1] < 90): porta_quarto.rot[1] += 1 * open_speed
    # # ######## quarto 2
    # porta_quarto2.render()
    # if(abrir_quarto2):
    # 	if (porta_quarto2.rot[1] > -100): porta_quarto2.rot[1] -= 1 * open_speed
    # 	else: abrir_quarto2 = False
    # else:
    # 	if (porta_quarto2.rot[1] < 0): porta_quarto2.rot[1] += 1 * open_speed
    # # ===================================================

    render(piso_1)
    render(piso_2)
    render(piso_3)

    # render(floor)
    # render(window)
    # render(window, pos=[2.8,0,8])
    # render(window, pos=[-1.3,0,0], rot=[0,90,0])
    # render(window, pos=[-1.3,0,13.9], rot=[0,90,0])
    # ====================================

    # ============ sala ===================
    #render(couch)
    #render(table , table.pos, table.rot, table.scale )
    #render(scream, scream.pos, scream.scale          )
    #render(carpet, carpet.pos, carpet.scale)
    # couch.render()
    # table.render()
    # scream.render()
    # carpet.render()

    # clock_.render()
    # clock_p1.render()
    # clock_p2.render()

    # clock_p1.rot[0] -= 1
    # clock_p2.rot[0] -= 2
    # ======================================

    # ============ cozinha ===================
    #render(pia , pia.pos, pia.rot)
    #render(fogao , fogao.pos)
    #render(estante , estante.pos)
    #render(tapete , tapete.pos, tapete.rot)
    # pia.render()
    # fogao.render()
    # estante.render()
    # tapete.render()
    # ======================================
    
    #============= quarto 1 ===================
    #render(cama1)
    #render(wardrobe1)
    # cama1.render()
    # wardrobe1.render()
    #==========================================
    #============= quarto 2 ===================
    #render(cama2 ,    cama2.pos    )
    #render(wardrobe2, wardrobe2.pos)
    # cama2.render()
    # wardrobe2.render()
    #==========================================
    
    # ============ Banheiro ================
    #render(bathtub,bathtub.pos,bathtub.rot,bathtub.scale)
    #render(toilet,toilet.pos,toilet.rot,toilet.scale)
    #render(sink,sink.pos,sink.rot,sink.scale)
    # bathtub.render()
    # toilet.render()
    # sink.render()
    # ======================================
    # personagem.render()
    # mesinha.render()
    
    
    #tomme.render()
    
    # Abajur().draw(0.7,{"x":-3,"y":-3,"z":1.45})
    # glColor3f(0, 0, 0)

    glPopMatrix()
    # ==================================

    pygame.display.set_caption('Apartamento')
    pygame.display.flip()

    #collision = check_box_collision(get_vertices(table), get_vertices(walls[0]))
    #collision = check_mesh_collision(table, couch)