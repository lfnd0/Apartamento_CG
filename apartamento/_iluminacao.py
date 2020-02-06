from OpenGL.GL import *
from OpenGL.GLU import *

def iluminacao_da_cena(luz_ligada):
    
    luz_ambiente=[0.2, 0.2, 0.2, 1.0]
    posicao_luz=[0.0, 10.0, 10.0, 1.0]

    glClearColor(0, 0, 0, 0)

    glShadeModel(GL_SMOOTH)

    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, luz_ambiente)

    glLightfv(GL_LIGHT0, GL_AMBIENT, luz_ambiente)
    glLightfv(GL_LIGHT0, GL_POSITION, posicao_luz)

    glEnable(GL_COLOR_MATERIAL)

    glEnable(GL_LIGHTING)
    
    if luz_ligada:
        glEnable(GL_LIGHT0)
    else:
        glDisable(GL_LIGHT0)
    
    glEnable(GL_DEPTH_TEST)