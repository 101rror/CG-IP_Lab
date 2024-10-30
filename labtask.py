import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math as mt

def draw_axes():
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINES)
    glVertex2f(-10, 0)
    glVertex2f(10, 0)
    glVertex2f(0, -10)
    glVertex2f(0, 10)
    glEnd()




def rotated_triangle(x1, y1, x2, y2, x3, y3, angle):
    # Rotate a Triangle 80 digree
    rad = mt.radians(angle)
    
    x1_rot = x1 * mt.cos(rad) - y1 * mt.sin(rad)
    y1_rot = x1 * mt.sin(rad) + y1 * mt.cos(rad)
    
    x2_rot = x2 * mt.cos(rad) - y2 * mt.sin(rad)
    y2_rot = x2 * mt.sin(rad) + y2 * mt.cos(rad)
    
    x3_rot = x3 * mt.cos(rad) - y3 * mt.sin(rad)
    y3_rot = x3 * mt.sin(rad) + y3 * mt.cos(rad)
    

    glColor3f(0.0, 1.0, 1.0)
    glBegin(GL_LINES)
    glVertex2f(x1_rot, y1_rot)
    glVertex2f(x2_rot, y2_rot)
    
    glVertex2f(x2_rot, y2_rot)
    glVertex2f(x3_rot, y3_rot)
    
    glVertex2f(x3_rot, y3_rot)
    glVertex2f(x1_rot, y1_rot)
    glEnd()




def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    draw_axes()
    
    basic_triangle(0, 0, 3, 3, 5, 2)
    
    rotated_triangle(0, 0, 3, 3, 5, 2, 80)
    
    glFlush()
    glutSwapBuffers()

def reshape(width, height): 
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-10, 10, -10, 10, -1, 1)
    glMatrixMode(GL_MODELVIEW)

def basic_triangle(x1, y1, x2, y2, x3, y3):
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glVertex2f(x3, y3)
    glVertex2f(x1, y1)
    glEnd()

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(500, 500)
glutCreateWindow(b"Rotated Triangle with PyOpenGL")
glEnable(GL_DEPTH_TEST)
glClearColor(0.0, 0.0, 0.0, 1.0)
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutMainLoop()