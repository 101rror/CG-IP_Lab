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

def draw_points():
    glColor3f(1.0, 0.0, 0.0)  # Red color for points
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(5, 4)  # (5, 4)
    glVertex2f(6, 2)  # (6, 2)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    draw_axes()
    draw_points()
    
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
