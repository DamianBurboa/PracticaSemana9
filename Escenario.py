from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *

class Escenario:

    xObstaculo = 0.0
    yObstaculo = 0.0

    xCarrito = -0.72
    yCarrito = 0.73

    colisionando = False

    def caminos(self):
        glPushMatrix()
        glTranslate(-0.5, 0.01, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.04, 0.0)
        glVertex3f(0.4, 0.04, 0.0)
        glVertex3f(0.4, 0.0, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(-0.6, -0.1, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.04, 0.0)
        glVertex3f(0.5, 0.04, 0.0)
        glVertex3f(0.5, 0.0, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(-0.5, 0.05, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.04, 0.0, 0.0)
        glVertex3f(0.04, 0.4, 0.0)
        glVertex3f(0.0, 0.4, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(-0.6, -0.1, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.04, 0.0, 0.0)
        glVertex3f(0.04, 0.55, 0.0)
        glVertex3f(0.0, 0.55, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(-0.5, 0.45, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.04, 0.0)
        glVertex3f(0.6, 0.04, 0.0)
        glVertex3f(0.6, 0.0, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(-0.76, 0.45, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.04, 0.0)
        glVertex3f(0.2, 0.04, 0.0)
        glVertex3f(0.2, 0.0, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(-0.85, 0.56, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.04, 0.0)
        glVertex3f(0.95, 0.04, 0.0)
        glVertex3f(0.95, 0.0, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(-0.5, 0.34, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.04, 0.0)
        glVertex3f(0.6, 0.04, 0.0)
        glVertex3f(0.6, 0.0, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(-0.4, 0.15, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.04, 0.0, 0.0)
        glVertex3f(0.04, 0.2, 0.0)
        glVertex3f(0.0, 0.2, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(-0.295, 0.01, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.04, 0.0, 0.0)
        glVertex3f(0.04, 0.2, 0.0)
        glVertex3f(0.0, 0.2, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(-0.298, 0.28, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.04, 0.0, 0.0)
        glVertex3f(0.04, 0.08, 0.0)
        glVertex3f(0.0, 0.08, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(-0.2, 0.2, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.04, 0.0, 0.0)
        glVertex3f(0.04, 0.08, 0.0)
        glVertex3f(0.0, 0.08, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(-0.2, 0.25, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.04, 0.0)
        glVertex3f(0.58, 0.04, 0.0)
        glVertex3f(0.58, 0.0, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(0.17, 0.25, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.04, 0.0, 0.0)
        glVertex3f(0.04, 0.43, 0.0)
        glVertex3f(0.0, 0.43, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(0.27, 0.35, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.04, 0.0, 0.0)
        glVertex3f(0.04, 0.25, 0.0)
        glVertex3f(0.0, 0.25, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(0.3, 0.45, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.04, 0.0)
        glVertex3f(0.2, 0.04, 0.0)
        glVertex3f(0.2, 0.0, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(0.38, 0.14, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.04, 0.0, 0.0)
        glVertex3f(0.04, 0.25, 0.0)
        glVertex3f(0.0, 0.25, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(0.3, 0.56, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.04, 0.0)
        glVertex3f(0.2, 0.04, 0.0)
        glVertex3f(0.2, 0.0, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(0.5, -0.01, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.04, 0.0, 0.0)
        glVertex3f(0.04, 0.5, 0.0)
        glVertex3f(0.0, 0.5, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(0.5, 0.56, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.04, 0.0, 0.0)
        glVertex3f(0.04, 0.24, 0.0)
        glVertex3f(0.0, 0.24, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(0.19, 0.099, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.04, 0.0)
        glVertex3f(0.23, 0.04, 0.0)
        glVertex3f(0.23, 0.0, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(0.22, -0.01, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.04, 0.0)
        glVertex3f(0.3, 0.04, 0.0)
        glVertex3f(0.3, 0.0, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(0.19, -0.5, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.04, 0.0, 0.0)
        glVertex3f(0.04, 0.53, 0.0)
        glVertex3f(0.0, 0.53, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(0.1, -0.4, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.04, 0.0, 0.0)
        glVertex3f(0.04, 0.68, 0.0)
        glVertex3f(0.0, 0.68, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(0.25, 0.2, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.04, 0.0, 0.0)
        glVertex3f(0.04, 0.08, 0.0)
        glVertex3f(0.0, 0.08, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(0.012, -0.5, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.04, 0.0)
        glVertex3f(0.3, 0.04, 0.0)
        glVertex3f(0.3, 0.0, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(0.01, -0.5, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.04, 0.0, 0.0)
        glVertex3f(0.04, 0.23, 0.0)
        glVertex3f(0.0, 0.23, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(-0.76, -0.29, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.04, 0.0)
        glVertex3f(0.81, 0.04, 0.0)
        glVertex3f(0.81, 0.0, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(-0.31, -0.252, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.04, 0.0, 0.0)
        glVertex3f(0.04, 0.08, 0.0)
        glVertex3f(0.0, 0.08, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(-0.41, -0.178, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.04, 0.0, 0.0)
        glVertex3f(0.04, 0.08, 0.0)
        glVertex3f(0.0, 0.08, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(-0.51, -0.252, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.04, 0.0, 0.0)
        glVertex3f(0.04, 0.08, 0.0)
        glVertex3f(0.0, 0.08, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(-0.76, -0.178, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.04, 0.0, 0.0)
        glVertex3f(0.04, 0.65, 0.0)
        glVertex3f(0.0, 0.65, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(-0.66, -0.1, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.04, 0.0)
        glVertex3f(0.08, 0.04, 0.0)
        glVertex3f(0.08, 0.0, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(-0.73, 0.0, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.04, 0.0)
        glVertex3f(0.08, 0.04, 0.0)
        glVertex3f(0.08, 0.0, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(-0.66, 0.1, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.04, 0.0)
        glVertex3f(0.08, 0.04, 0.0)
        glVertex3f(0.08, 0.0, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(-0.73, 0.2, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.04, 0.0)
        glVertex3f(0.08, 0.04, 0.0)
        glVertex3f(0.08, 0.0, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(-0.66, 0.3, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.04, 0.0)
        glVertex3f(0.08, 0.04, 0.0)
        glVertex3f(0.08, 0.0, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(-0.76, -0.19, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.04, 0.0)
        glVertex3f(0.29, 0.04, 0.0)
        glVertex3f(0.29, 0.0, 0.0)
        glEnd()
        glPopMatrix()
        
        glPushMatrix()
        glTranslate(-0.87, -0.29, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.04, 0.0, 0.0)
        glVertex3f(0.04, 0.89, 0.0)
        glVertex3f(0.0, 0.89, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(-0.87, -0.8, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.04, 0.0, 0.0)
        glVertex3f(0.04, 0.6, 0.0)
        glVertex3f(0.0, 0.6, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(-0.76, -0.4, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.04, 0.0)
        glVertex3f(0.81, 0.04, 0.0)
        glVertex3f(0.81, 0.0, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(-0.85, -0.5, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.04, 0.0)
        glVertex3f(0.78, 0.04, 0.0)
        glVertex3f(0.78, 0.0, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(-0.77, -0.7, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.04, 0.0, 0.0)
        glVertex3f(0.04, 0.1, 0.0)
        glVertex3f(0.0, 0.1, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(-0.77, -0.6, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.04, 0.0)
        glVertex3f(1.0, 0.04, 0.0)
        glVertex3f(1.0, 0.0, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(-0.86, -0.8, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.04, 0.0)
        glVertex3f(1.0, 0.04, 0.0)
        glVertex3f(1.0, 0.0, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(-0.77, -0.7, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.04, 0.0)
        glVertex3f(1.0, 0.04, 0.0)
        glVertex3f(1.0, 0.0, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(0.1, -0.8, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.04, 0.0)
        glVertex3f(0.24, 0.04, 0.0)
        glVertex3f(0.24, 0.0, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(0.30, -0.7, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.04, 0.0, 0.0)
        glVertex3f(0.04, 0.62, 0.0)
        glVertex3f(0.0, 0.62, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(0.3, -0.1, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.04, 0.0)
        glVertex3f(0.34, 0.04, 0.0)
        glVertex3f(0.34, 0.0, 0.0)
        glEnd()
        glPopMatrix()
        
        glPushMatrix()
        glTranslate(0.6, -0.01, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.04, 0.0, 0.0)
        glVertex3f(0.04, 0.87, 0.0)
        glVertex3f(0.0, 0.87, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(0.705, -0.29, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.04, 0.0, 0.0)
        glVertex3f(0.04, 0.89, 0.0)
        glVertex3f(0.0, 0.89, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(0.705, -0.8, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.04, 0.0, 0.0)
        glVertex3f(0.04, 0.6, 0.0)
        glVertex3f(0.0, 0.6, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(0.6, -0.8, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.04, 0.0, 0.0)
        glVertex3f(0.04, 0.62, 0.0)
        glVertex3f(0.0, 0.62, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(-0.29, -0.8, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.04, 0.0)
        glVertex3f(1.0, 0.04, 0.0)
        glVertex3f(1.0, 0.0, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(0.3, -0.7, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.04, 0.0)
        glVertex3f(0.24, 0.04, 0.0)
        glVertex3f(0.24, 0.0, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(0.4, -0.6, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.04, 0.0)
        glVertex3f(0.24, 0.04, 0.0)
        glVertex3f(0.24, 0.0, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(0.4, -0.58, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.04, 0.0, 0.0)
        glVertex3f(0.04, 0.42, 0.0)
        glVertex3f(0.0, 0.42, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(0.5, -0.5, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.04, 0.0, 0.0)
        glVertex3f(0.04, 0.32, 0.0)
        glVertex3f(0.0, 0.32, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(0.5, -0.2, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.04, 0.0)
        glVertex3f(0.14, 0.04, 0.0)
        glVertex3f(0.14, 0.0, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(-0.29, 0.86, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.04, 0.0)
        glVertex3f(1.0, 0.04, 0.0)
        glVertex3f(1.0, 0.0, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(-0.87, 0.86, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.04, 0.0)
        glVertex3f(1.0, 0.04, 0.0)
        glVertex3f(1.0, 0.0, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(0.705, 0.1, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.04, 0.0, 0.0)
        glVertex3f(0.04, 0.8, 0.0)
        glVertex3f(0.0, 0.8, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(-0.87, 0.0, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.04, 0.0, 0.0)
        glVertex3f(0.04, 0.89, 0.0)
        glVertex3f(0.0, 0.89, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(-0.60, 0.56, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.04, 0.0, 0.0)
        glVertex3f(0.04, 0.13, 0.0)
        glVertex3f(0.0, 0.13, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(-0.60, 0.76, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.04, 0.0, 0.0)
        glVertex3f(0.04, 0.1, 0.0)
        glVertex3f(0.0, 0.1, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(-0.58, 0.65, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.04, 0.0)
        glVertex3f(0.79, 0.04, 0.0)
        glVertex3f(0.79, 0.0, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(-0.58, 0.76, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.04, 0.0)
        glVertex3f(0.5, 0.04, 0.0)
        glVertex3f(0.5, 0.0, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(0, 0.65, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.04, 0.0, 0.0)
        glVertex3f(0.04, 0.15, 0.0)
        glVertex3f(0.0, 0.15, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(0.12, 0.75, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.04, 0.0, 0.0)
        glVertex3f(0.04, 0.15, 0.0)
        glVertex3f(0.0, 0.15, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(0.2, 0.65, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.04, 0.0)
        glVertex3f(0.23, 0.04, 0.0)
        glVertex3f(0.23, 0.0, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(0.24, 0.65, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.04, 0.0, 0.0)
        glVertex3f(0.04, 0.15, 0.0)
        glVertex3f(0.0, 0.15, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(0.34, 0.76, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.04, 0.0)
        glVertex3f(0.18, 0.04, 0.0)
        glVertex3f(0.18, 0.0, 0.0)
        glEnd()
        glPopMatrix()
    
    def paredes2(self):

        glPushMatrix()
        glTranslate(self.xObstaculo, self.yObstaculo, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0,0.0,0.0)
        glVertex3f(0.05,-0.07,0.0)
        glVertex3f(0.05,-0.20,0.0)
        glVertex3f(-0.2,-0.20,0.0)
        glVertex3f( -0.2,-0.07,0.0) 
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(0.001, -0.1, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.05, 0.0, 0.0)
        glVertex3f(0.05, 0.2, 0.0)
        glVertex3f(0.0, 0.2, 0.0)
        glEnd()
        glPopMatrix()

    def paredes3(self):

        glPushMatrix()
        glTranslate(self.xObstaculo, self.yObstaculo, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.0,.0,0.0)
        glVertex3f(0.05,0.05,0.0)
        glVertex3f(0.05,0.20,0.0)
        glVertex3f(-0.2,0.20,0.0)
        glVertex3f( -0.2,0.05,0.0) 
        glEnd()
        glPopMatrix() 