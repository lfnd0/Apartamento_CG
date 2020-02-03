from OpenGL.GL import *
from OpenGL.GLU import *

def iluminacao_da_cena(luz_ligada):
    
    luz_ambiente=[0.2,0.2,0.2,1.0]
    posicao_luz=[0.0, 10.0, 10.0, 1.0]

    # Especifica que a cor de fundo da janela será branca
    glClearColor(0, 0, 0, 0)

    # Habilita o modelo de colorização
    glShadeModel(GL_SMOOTH)   # GL_SMOOTH ou GL_FLAT

    # Ativa o uso da luz ambiente
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, luz_ambiente)

    # Define os parametros da luz de número 0
    glLightfv(GL_LIGHT0, GL_AMBIENT, luz_ambiente)
    glLightfv(GL_LIGHT0, GL_POSITION, posicao_luz)

    # Habilita a definição da cor do material a partir da cor corrente
    glEnable(GL_COLOR_MATERIAL)
    # Habilita o uso de iluminação
    glEnable(GL_LIGHTING)
    
    # Habilita a luz de número 0
    if luz_ligada:
        glEnable(GL_LIGHT0)
    else:
        glDisable(GL_LIGHT0)
    
    # Habilita o depth-buffering
    glEnable(GL_DEPTH_TEST)