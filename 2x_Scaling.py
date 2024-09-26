import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_axes():
    glColor3f(1.0, 1.0, 1.0)  # White color for axes
    glBegin(GL_LINES)
    glVertex2f(-10, 0)  # x-axis
    glVertex2f(10, 0)
    glVertex2f(0, -10)  # y-axis
    glVertex2f(0, 10)
    glEnd()

def basic_triangle(x1, y1, x2, y2, x3, y3):
    glColor3f(1.0, 0.0, 0.0)  # Red color for points
    glPointSize(5)
    glBegin(GL_LINES)
    glVertex2f(x1, y1)  # (5, 4)
    glVertex2f(x2, y2)
    
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    
    glVertex2f(x3, y3)
    glVertex2f(x1, y1)
    glEnd()

def scaled_triangle(x1, y1, x2, y2, x3, y3, scale):
    #Magnify the triangle with vertices A(1, 1), B(3, 3), C(5, 2) to twice its size while keeping A(1, 1) fixed.
    
    # x1 = x1*scale
    # y1 = y1*scale
    
    x2 = x1 + (x2 - x1) * scale
    y2 = y1 + (y2 - y1) * scale
    
    x3 = x1 + (x3 - x1) * scale
    y3 = y1 + (y3 - y1) * scale


    glColor3f(0.0, 1.0, 0.0)  # Green color for points
    glPointSize(5)
    glBegin(GL_LINES)
    glVertex2f(x1, y1)  # (5, 4)
    glVertex2f(x2, y2)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glVertex2f(x3, y3)
    glVertex2f(x1, y1)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    draw_axes()
    
    basic_triangle(1, 1, 3, 3, 5, 2)
    scaled_triangle(1, 1, 3, 3, 5, 2, 2)
    
    glFlush()
    glutSwapBuffers()

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-10, 10, -10, 10, -1, 1)
    glMatrixMode(GL_MODELVIEW)


glutInit()  # Initialize GLUT
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(500, 500)
glutCreateWindow(b"Plotting with PyOpenGL")
glEnable(GL_DEPTH_TEST)
glClearColor(0.0, 0.0, 0.0, 1.0)
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutMainLoop()