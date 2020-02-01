import pygame
from OpenGL.GLU import *
from OpenGL.GL import *

def MTL(filename):
    contents = {}
    mtl = None
    for line in open(filename, "r"):
        if line.startswith('#'): continue
        values = line.split()
        if not values: continue
        if values[0] == 'newmtl':
            mtl = contents[values[1]] = {}
        elif mtl is None:
            raise (ValueError, "mtl file doesn't start with newmtl stmt")
        elif values[0] == 'map_Kd':
            # load the texture referred to by this declaration
            mtl[values[0]] = values[1]
            surf = pygame.image.load(mtl['map_Kd'])
            image = pygame.image.tostring(surf, 'RGBA', 1)
            ix, iy = surf.get_rect().size
            texid = mtl['texture_Kd'] = glGenTextures(1)
            glBindTexture(GL_TEXTURE_2D, texid)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER,
                GL_LINEAR)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER,
                GL_LINEAR)
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, ix, iy, 0, GL_RGBA,
                GL_UNSIGNED_BYTE, image)
        else:
            mtl[values[0]] = map(float, values[1:])
    return contents

def get_vertices(obj):
    vector = []
    for x in obj.vertices:
        vector.append([ x[0]+obj.pos[0], x[1]+obj.pos[1], x[2]+obj.pos[2] ])
    return vector

def get_vert(obj):
    vertices = []
    for v in obj.vertices:
        vertices.append(v)
    return vertices

def check_box_collision(box1, box2):
    """
    Check Collision of 2 box colliders
    """
    #print('\nCollision check:')

    x_max = max([e[0] for e in box1])
    x_min = min([e[0] for e in box1])
    y_max = max([e[1] for e in box1])
    y_min = min([e[1] for e in box1])
    z_max = max([e[2] for e in box1])
    z_min = min([e[2] for e in box1])
    #print('Box1 min %.2f, %.2f, %.2f' % (x_min, y_min, z_min))
    #print('Box1 max %.2f, %.2f, %.2f' % (x_max, y_max, z_max))    
    
    x_max2 = max([e[0] for e in box2])
    x_min2 = min([e[0] for e in box2])
    y_max2 = max([e[1] for e in box2])
    y_min2 = min([e[1] for e in box2])
    z_max2 = max([e[2] for e in box2])
    z_min2 = min([e[2] for e in box2])
    #print('Box2 min %.2f, %.2f, %.2f' % (x_min2, y_min2, z_min2))
    #print('Box2 max %.2f, %.2f, %.2f' % (x_max2, y_max2, z_max2))        
    
    isColliding = []

    if(x_max >= x_min2 and x_max <= x_max2): isColliding.append(True)
    else: isColliding.append(False)

    if(x_min <= x_max2 and x_min >= x_min2): isColliding.append(True)
    else: isColliding.append(False)

    if(y_max >= y_min2 and y_max <= y_max2): isColliding.append(True)
    else: isColliding.append(False)

    if(y_min <= y_max2 and y_min >= y_min2): isColliding.append(True)
    else: isColliding.append(False)

    if(z_max >= z_min2 and z_max <= z_max2): isColliding.append(True)
    else: isColliding.append(False) 

    if(z_min <= z_max2 and z_min >= z_min2): isColliding.append(True)
    else: isColliding.append(False)  

    #if isColliding:
    #    print('Colliding!')
        
    return isColliding

def chek_collisions(player, collisionMask=[]):
    allcolisions = { 'left':0, 'right':0, 'up':0,'down':0 }
    for collider in collisionMask:
        a = check_box_collision(get_vertices(player),get_vertices(collider))
        #colisoes no eixo x
        if a[0] and (a[4] or a[5]): allcolisions['down'] += 1
        if a[1] and (a[4] or a[5]): allcolisions['up']   += 1
        #colisoes no eixo z
        if a[4] and (a[0] or a[1]): allcolisions['left'] += 1
        if a[5] and (a[0] or a[1]): allcolisions['right']   += 1

    return allcolisions

class OBJ:
    def __init__(self, filename, pos=[0,0,0],rot=[0,0,0],scale=[1,1,1], isTrigger=False):
        """Carrega dados do arquivo OBJ. """
        self.vertices = []
        self.normals = []
        self.texcoords = []
        self.faces = []

        self.pos       = pos
        self.rot       = rot
        self.scale     = scale
        self.isTrigger = isTrigger

        material = None
        for line in open(filename, "r"):
            if line.startswith('#'): continue
            values = line.split()
            if not values: continue
            if values[0] == 'v':
                v = list(map(float, values[1:4]))
                self.vertices.append(v)
            elif values[0] == 'vn':
                v = list(map(float, values[1:4]))
                self.normals.append(v)
            elif values[0] == 'vt':
                self.texcoords.append( list(map(float, values[1:3])) )
            elif values[0] in ('usemtl', 'usemat'):
                material = values[1]
            elif values[0] == 'mtllib':
                self.mtl = MTL(values[1])
            elif values[0] == 'f':
                face = []
                texcoords = []
                norms = []
                for v in values[1:]:
                    w = v.split('/')
                    face.append(int(w[0]))
                    if len(w) >= 2 and len(w[1]) > 0:
                        texcoords.append(int(w[1]))
                    else:
                        texcoords.append(0)
                    if len(w) >= 3 and len(w[2]) > 0:
                        norms.append(int(w[2]))
                    else:
                        norms.append(0)
                self.faces.append((face, norms, texcoords, material))

        self.gl_list = glGenLists(1)
        glNewList(self.gl_list, GL_COMPILE)
        glEnable(GL_TEXTURE_2D)
        glFrontFace(GL_CCW)

        for face in self.faces:
            vertices, normals, texture_coords, material = face

            mtl = self.mtl[material]
            
            if 'texture_Kd' in mtl:
                # diffuse texmap
                glBindTexture(GL_TEXTURE_2D, mtl['texture_Kd'])
            else:
                # diffuse color
                #glColor(*mtl['Kd'])
                glColor3f(1,1,1)

            glBegin(GL_POLYGON)
            for i in range(0,len(vertices)):
                if normals[i] > 0:
                    glNormal3fv(self.normals[normals[i] - 1])
                if texture_coords[i] > 0:
                    glTexCoord2fv(self.texcoords[texture_coords[i] - 1])
                glVertex3fv(self.vertices[vertices[i] - 1])
            glEnd()
        
        glDisable(GL_TEXTURE_2D)
        glEndList()

    def render(self):
        glPushMatrix()
        glTranslate(self.pos[0], self.pos[1], self.pos[2])
        glScale(self.scale[0], self.scale[1], self.scale[2])
        glRotate(self.rot[0], 1, 0, 0)
        glRotate(self.rot[1], 0, 1, 0)
        glRotate(self.rot[2], 0, 0, 1)
        glCallList(self.gl_list)
        glPopMatrix()