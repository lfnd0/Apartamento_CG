import glm
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *

class Camera():
    def __init__(self, pos, center, up, tomme):
        self.pos = pos
        self.center = center
        self.up = up
        self.tomme = tomme
        self.tomme.pos = pos
        self.__matrix = None
        self.init_camera()

    def view(self):
       glLoadMatrixf(self.matrix4)

    @property
    def matrix4(self):
        return np.array(self.__matrix)


    def move(self, x, y, z):
        pos_tomme = list(self.tomme.pos)
        pos_tomme[0] += x
        pos_tomme[1] += y
        pos_tomme[2] += z

        self.tomme.pos = tuple(pos_tomme)
        self.__matrix = glm.translate(self.__matrix, glm.vec3(x, y, z))

    def rotate(self, angle, x, y, z):
        self.__matrix = glm.rotate(self.__matrix, glm.radians(angle), glm.vec3(x, y, z))
        
    def init_camera(self):
        self.__matrix =  glm.lookAt(glm.vec3(self.pos), glm.vec3(self.center), glm.vec3(self.up))