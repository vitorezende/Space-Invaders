"""
Universidade Federal de Mato Grosso - Campus Universitario do Araguaia
Dicente: Vitor Rezende Campos
Docente: Rafael Teixeira
Disciplina: Computacao Grafica

Game Space Invaders - Python  OpenGL
    
"""
import numpy
import sys
import Image
import math
import OpenGL
import random
from OpenGL.GLUT import *
from OpenGL.GL import *
from sys import argv


#Variaveis globais
T = -6
viewangle = 0
moverx = 0
localTiro = 0
disparo = False
reverse = False
numParticulas = 250 
tempExplosao = 25 
particulas = []


img = Image.open("textura.png") 
img_data = numpy.array(list(img.getdata()), numpy.int8)
   

#Classes
class particulaClass(object): #classe para as particulas
    def __init__(self, x, y, z, vx, vy, vz, cor = []):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz
        self.cor = cor

#Coordenadas dos ETs
cord2 = [ [-4, 6.5, 0], [-3, 6.5, 0], [-2, 6.5, 0], [-1, 6.5, 0], [0, 6.5, 0], [1, 6.5, 0], [2, 6.5, 0], [3, 6.5, 0], [4, 6.5, 0], [-4, 6, 0], [-3, 6, 0], [-2, 6, 0], [-1, 6, 0], [0, 6, 0], [1, 6, 0], [2, 6, 0], [3, 6, 0], [4, 6, 0] ]
cord1 = [ [-4, 5.5, 0], [-3, 5.5, 0], [-2, 5.5, 0], [-1, 5.5, 0], [0, 5.5, 0], [1, 5.5, 0], [2, 5.5, 0], [3, 5.5, 0], [4, 5.5, 0], [-4, 5, 0], [-3, 5, 0], [-2, 5, 0], [-1, 5, 0], [0, 5, 0], [1, 5, 0], [2, 5, 0], [3, 5, 0], [4, 5, 0], [-4, 4.5, 0], [-3, 4.5, 0], [-2, 4.5, 0], [-1, 4.5, 0], [0, 4.5, 0], [1, 4.5, 0], [2, 4.5, 0], [3, 4.5, 0], [4, 4.5, 0] ]
orienta = [ [4, 4.5, 0], [-3, 5.5, 0] ]


#Funcao de Inicializacao
def init ():

  # Camera
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  glOrtho (-1.5, 1.5, -1.5, 1.5, -1.5, 1.5)
  # Iluminacao
  glEnable(GL_LIGHTING)
  glEnable(GL_LIGHT0)
  glEnable(GL_LIGHT1)
  glEnable(GL_DEPTH_TEST)
     
  lightpos = [2.0, 2.0, 1.0, 1.0]
  lightcol = [.8, .0, .0, 1.0]
  lightamb = [.5, .5, .5, 1.0]
     
  glLightfv(GL_LIGHT0, GL_POSITION, lightpos)
  glLightfv(GL_LIGHT0, GL_DIFFUSE, lightcol)
  glLightfv(GL_LIGHT1, GL_AMBIENT, lightamb)
  glEnable(GL_COLOR_MATERIAL)
  glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
  
  
  
  
 
 
#Funcao para controle de teclas
def teclado (key, x, y):
  global disparo, localTiro
  if (key == ' '):
    if disparo == False:
      localTiro = moverx
      disparo = True
  glutPostRedisplay()
  
def specialKeys( key, x, y ):
  global viewangle, moverx, localTiro, disparo
  if (key == GLUT_KEY_RIGHT):
    moverx += 0.2
    if (viewangle <= 30):
      viewangle += 10
  else:
    if (key == GLUT_KEY_LEFT):
      moverx -= 0.2
      if (viewangle >= -30):
	viewangle -= 10
  glutPostRedisplay()
  
#Funcao de explosao
def explosao(x,y, z, cor):
   global particulas, tempExplosao
   particulas = []
   while(len(particulas) < numParticulas):
      vx = 0.0
      vy = 0.0
      vz = 0.0
      vx = (random.uniform(-1,1))
      vy = (random.uniform(-1,1))
      vz = (random.uniform(-1,1))
      p = particulaClass(x,y,z,vx,vy,vz,cor)
      particulas.append(p)
      
   tempExplosao = 25
  
#Funcao para desenho do ET
def desenhaET1 ():
  #Cara
  glPushMatrix()
  glColor3f (.0, .8, .0)
  glScalef (7, 1.0, 1.0)
  glutSolidCube (0.05)
  glPopMatrix()
  
  glPushMatrix()
  glColor3f (.0, .8, .0)
  glScalef (2, 1.0, 1.0)
  glTranslatef (-0.0875, -0.05, 0)
  glutSolidCube (0.05)
  glPopMatrix()
  
  glPushMatrix()
  glColor3f (.0, .8, .0)
  glScalef (2, 1.0, 1.0)
  glTranslatef (0.0875, -0.05, 0)
  glutSolidCube (0.05)
  glPopMatrix()
  
  glPushMatrix()
  glColor3f (.0, .8, .0)
  glScalef (3, 1.0, 1.0)
  glTranslatef (0, -0.05, 0)
  glutSolidCube (0.05)
  glPopMatrix()
  
  glPushMatrix()
  glColor3f (.0, .8, .0)
  glScalef (11, 1.0, 1.0)
  glTranslatef (0, -0.10, 0)
  glutSolidCube (0.05)
  glPopMatrix()
  
  glPushMatrix()
  glColor3f (.0, .8, .0)
  glTranslatef (-0.2, -0.15, 0)
  glutSolidCube (0.05)
  glPopMatrix()
  
  glPushMatrix()
  glColor3f (.0, .8, .0)
  glTranslatef (0.2, -0.15, 0)
  glutSolidCube (0.05)
  glPopMatrix()
  
  glPushMatrix()
  glColor3f (.0, .8, .0)
  glScalef (7, 1.0, 1.0)
  glTranslatef (0.0, -0.15, 0)
  glutSolidCube (0.05)
  glPopMatrix()
  
  glPushMatrix()
  glColor3f (.0, .8, .0)
  glScalef (5, 1.0, 1.0)
  glTranslatef (0.0, -0.20, 0)
  glutSolidCube (0.05)
  glPopMatrix()
  
  glPushMatrix()
  glColor3f (.0, .8, .0)
  glTranslatef (-0.15, -0.25, 0)
  glutSolidCube (0.05)
  glPopMatrix()
  
  glPushMatrix()
  glColor3f (.0, .8, .0)
  glTranslatef (0.15, -0.25, 0)
  glutSolidCube (0.05)
  glPopMatrix()
  
  glPushMatrix()
  glColor3f (.0, .8, .0)
  glTranslatef (0, -0.25, 0)
  glScalef (2, 1.0, 1.0)
  glutSolidCube (0.05)
  glPopMatrix()
 
  #Antenas
  glPushMatrix()
  glColor3f (.0, .8, .0)
  glTranslatef (-0.10, .05, 0)
  glutSolidCube (.05)
  glTranslatef (0, .05, 0)
  glutSolidCube (.05)
  glPopMatrix()
  
  glPushMatrix()
  glColor3f (.0, .8, .0)
  glTranslatef (0.10, .05, 0)
  glutSolidCube (.05)
  glTranslatef (0, .05, 0)
  glutSolidCube (.05)
  glPopMatrix()
  
#Funcao para desenha desenhaET2
def desenhaET2 ():
  #Cara
  glPushMatrix()
  glColor3f (.0, .0, .7)
  glScalef (7, 1.0, 1.0)
  glutSolidCube (0.05)
  glPopMatrix()
  
  glPushMatrix()
  glColor3f (.0, .0, .7)
  glScalef (2, 1.0, 1.0)
  glTranslatef (-0.0875, -0.05, 0)
  glutSolidCube (0.05)
  glPopMatrix()
  
  glPushMatrix()
  glColor3f (.0, .0, .7)
  glScalef (2, 1.0, 1.0)
  glTranslatef (0.0875, -0.05, 0)
  glutSolidCube (0.05)
  glPopMatrix()
  
  glPushMatrix()
  glColor3f (.0, .0, .7)
  glScalef (3, 1.0, 1.0)
  glTranslatef (0, -0.05, 0)
  glutSolidCube (0.05)
  glPopMatrix()
  
  glPushMatrix()
  glColor3f (.0, .0, .7)
  glScalef (11, 1.0, 1.0)
  glTranslatef (0, -0.10, 0)
  glutSolidCube (0.05)
  glPopMatrix()
  
  glPushMatrix()
  glColor3f (.0, .0, .7)
  glTranslatef (-0.3, -0.15, 0)
  glutSolidCube (0.05)
  glPopMatrix()
  
  glPushMatrix()
  glColor3f (.0, .0, .7)
  glTranslatef (0.3, -0.15, 0)
  glutSolidCube (0.05)
  glPopMatrix()
  
  glPushMatrix()
  glColor3f (.0, .0, .7)
  glScalef (9, 1.0, 1.0)
  glTranslatef (0.0, -0.15, 0)
  glutSolidCube (0.05)
  glPopMatrix()
  
  glPushMatrix()
  glColor3f (.0, .0, .7)
  glTranslatef (0.3, -0.20, 0)
  glutSolidCube (0.05)
  glPopMatrix()
  
  glPushMatrix()
  glColor3f (.0, .0, .7)
  glTranslatef (-0.3, -0.20, 0)
  glutSolidCube (0.05)
  glPopMatrix()
  
  glPushMatrix()
  glColor3f (.0, .0, .7)
  glTranslatef (-0.20, -0.20, 0)
  glutSolidCube (0.05)
  glPopMatrix()
  
  glPushMatrix()
  glColor3f (.0, .0, .7)
  glTranslatef (0.20, -0.20, 0)
  glutSolidCube (0.05)
  glPopMatrix()
  
  glPushMatrix()
  glColor3f (.0, .0, .7)
  glTranslatef (0.15, -0.25, 0)
  glutSolidCube (0.05)
  glTranslatef (0.05, 0, 0)
  glutSolidCube (0.05)
  glPopMatrix()
  
  glPushMatrix()
  glColor3f (.0, .0, .7)
  glTranslatef (-0.15, -0.25, 0)
  glutSolidCube (0.05)
  glTranslatef (-0.05, 0, 0)
  glutSolidCube (0.05)
  glPopMatrix()
 
  #Antenas
  glPushMatrix()
  glColor3f (.0, .0, .7)
  glTranslatef (-0.10, .05, 0)
  glutSolidCube (.05)
  glTranslatef (-0.05, .05, 0)
  glutSolidCube (.05)
  glPopMatrix()
  
  glPushMatrix()
  glColor3f (.0, .0, .7)
  glTranslatef (0.10, .05, 0)
  glutSolidCube (.05)
  glTranslatef (0.05, .05, 0)
  glutSolidCube (.05)
  glPopMatrix()
  
#Funcao para desenho da nave
def desenhaNave ():
  global img_data, img
  
  
  #Desenhando as asas
  glPushMatrix()
  id = glGenTextures(1)
  glPixelStorei(GL_UNPACK_ALIGNMENT,1)
  glBindTexture (GL_TEXTURE_2D, id)
  glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_NEAREST)
  glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
  glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
  glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
  glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
  glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.size[0], img.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
  glGenerateMipmap(GL_TEXTURE_2D)
  
  
  glEnable(GL_TEXTURE_2D)
  glBindTexture (GL_TEXTURE_2D, id)
  glColor3f (.6, .8, .8)
  
  glBegin(GL_TRIANGLES)   
  glTexCoord2f(0, 0)
  glVertex3f( 0,  -0.4, 0 )
  glTexCoord2f(1, 0)
  glVertex3f(  1,  -0.5, 0 )
  glTexCoord2f(0, 1)
  glVertex3f( 0,  0.4, 0 )
  
  glTexCoord2f(0, 0)
  glVertex3f( 0,  -0.4, 0 )
  glTexCoord2f(1, 0)
  glVertex3f(  -1,  -0.5, 0 )
  glTexCoord2f(0, 1)
  glVertex3f( 0,  0.4, 0 )
  
  
  glEnd()
  
  glDisable(GL_TEXTURE_2D)
  
  glPopMatrix()
  
  #Desenhando a base
  glPushMatrix()
  glColor3f (0.8, 0.3, 0.0)
  glScalef ( 0.3, 1.0, 0.25 )
  glutSolidSphere ( 0.5, 50, 50 )
  glPopMatrix()
  
  glPushMatrix()
  glColor3f (.9, .9, .9)
  glScalef ( 0.5, 1.0, 0.5 )
  glutSolidSphere ( 0.35, 50, 50 )
  glPopMatrix()
  
  #Bunda
  glPushMatrix()
  glColor3f (.3, .3, .3)
  glScalef ( 0.25, 0.3, 0.3 )
  glTranslatef ( 0.0, -0.30, 0.0 )
  glutSolidTorus(0.35, 0.7, 50, 50)
  glPopMatrix()
  
  #Canhao
  glPushMatrix()
  glColor3f (.8, .0, .0)
  glScalef ( 0.15, 0.15, 0.1 )
  glTranslatef ( 0.0, 2.3 , 0 )
  glRotatef(240, 1.0, 1.0, 1.0)
  glutSolidCylinder( 0.1, 1.5, 6, 6)
  glPopMatrix()

# Funcao para desenhar o projetil  
def desenhaBala():
  glPushMatrix()
  glColor3f (.8, .0, .0)
  glScalef ( 0.15, 0.15, 0.1 )
  glTranslatef ( 0.0, 2.3 , 0 )
  glRotatef(240, 1.0, 1.0, 1.0)
  glutSolidCylinder( 0.1, 1.5, 6, 6)
  glPopMatrix()
  
# Funcao do tiro
def tiro( local ):
  global T, disparo
  glPushMatrix()
  glScalef (.2, .2, .2)
  glTranslatef (local, T, 0.0)
  desenhaBala()
  glPopMatrix()
  if (T > 7):
    T = -6
    disparo = False
  
# Movendo os ETs
def atualizaCordX (cords):
  global reverse
  if ( reverse == False ):
    cords[0] = cords[0] + 0.05
  else:
    cords[0] = cords[0] - 0.05
    
def atualizaCordY (cords):
  cords[1] = cords[1] - 0.1
    
# Temporizador para animacao
def timer( valor ):
  global T, disparo, cord1, cord2, reverse
  if disparo == True:
    T += 0.1
    
  # Movimentacao dos ETs
  if (orienta[0][0] <= 7):
    map (atualizaCordX, cord1)
    map (atualizaCordX, cord2)
    map (atualizaCordX, orienta)
    if (orienta[0][0] > 7):
      map (atualizaCordY, cord1)
      map (atualizaCordY, cord2)
      map (atualizaCordY, orienta)
      if (orienta[1][0] > -7):
	reverse = True
	map (atualizaCordX, cord1)
	map (atualizaCordX, cord2)
	map (atualizaCordX, orienta)
  if (orienta[1][0] < -6):
    map (atualizaCordY, cord1)
    map (atualizaCordY, cord2)
    map (atualizaCordY, orienta)
    reverse = False
      
  trataColisao()
  
  glutPostRedisplay();			#Redesenhar
  glutTimerFunc(30, timer, 1 );
 
# Funcao que trata as colisoes
def trataColisao ():
  global cord1, cord2, T, disparo, x1, y1
  buffAlien = []
  for i in range (0, len(cord1)):
    if ( localTiro >= cord1[i][0] - 0.25 and  localTiro <= cord1[i][0] + 0.25 and T >= cord1[i][1] - 0.25 and T <= cord1[i][1] + 0.25):
      if cord1[i] not in buffAlien:
	buffAlien.append (cord1[i])
	
  for i in range (0, len(cord2)):
    if ( localTiro >= cord2[i][0] - 0.25 and  localTiro <= cord2[i][0] + 0.25 and T >= cord2[i][1] - 0.25 and T <= cord2[i][1] + 0.25):
      if cord2[i] not in buffAlien:
	buffAlien.append (cord2[i])
	
  for x in buffAlien:
    if x in cord1:
      cord1.remove (x)
      disparo = False
      T = -6
      cor = [.0, .8, .0]
    else:
      cord2.remove (x)
      disparo = False
      T = -6
      cor = [.0, .0, .7]
    explosao (x[0], x[1], x[2], cor)
    
  	
#Funcao de Desenho
def display ():
  global disparo, cord1, cord2, x1, y1, particulas, tempExplosao
  
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
  glMatrixMode(GL_MODELVIEW)
  
  glPushMatrix()
  #Chamando ET2
  for x in cord2:
    glPushMatrix()
    glScalef (.2, .2, .2)
    glTranslatef (x[0], x[1], x[2])
    desenhaET2()
    glPopMatrix()  
    
  #Chamando ET1
  for x in cord1:
    glPushMatrix()
    glScalef (.2, .2, .2)
    glTranslatef (x[0], x[1], x[2])
    desenhaET1()
    glPopMatrix()

  #Chamando nave
  glPushMatrix()
  glScalef (.2, .2, .2)
  glTranslatef (moverx, -6, 0.0)
  glRotatef(viewangle, 0.0, 1.0, 0.0)
  desenhaNave()
  glPopMatrix()
  
  #Chamando explosoes
  if tempExplosao > 0 and len(particulas) > 0:
    for i in particulas:
      glPushMatrix()
      i.x += i.vx * 0.2
      i.y += i.vy * 0.2
      i.z += i.vz * 0.2
      glColor3fv(i.cor)
      glScalef(.2, .2, .2)
      glTranslatef(i.x,i.y,i.z)
      glutSolidSphere(0.05,10,10);
      glPopMatrix()
    tempExplosao -= 2
  
  # Chamando o Tiro
  if (disparo == True): 
    tiro (localTiro)
  
  glPopMatrix()
  glEnable(GL_NORMALIZE)
  glutSwapBuffers()
  
#Funcao MAIN
glutInit(argv)
glutInitDisplayMode ( GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA)
glutInitWindowSize (600, 600)
glutCreateWindow ("Space Invaders - by Vitor R. Campos")
glutSpecialFunc(specialKeys)
glutKeyboardFunc (teclado)
glutDisplayFunc (display)
glutTimerFunc(30, timer, 1)
init()
glutMainLoop()