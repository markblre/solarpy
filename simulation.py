from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GLE import *

from PIL import Image
import numpy

import pygame
from pygame.locals import *
from numpy import array

from skyfield.api import load
import time

ts = load.timescale()

localSeconde = 0

def goSimulation(SCREEN_SIZE, fullScreen, showSun, showMercury, showVenus, showEarth,
                 showMars, showJupiter, showSaturn, showUranus, showNeptune, showPaths,
                 years, month, day, hour, minute, seconde, realTime, speed):

    localSeconde = seconde
    
    planets = load('de421.bsp')
    sun = planets['sun']
    mercury = planets['mercury barycenter']
    venus = planets['venus barycenter']
    earth = planets['earth barycenter']
    mars = planets['mars barycenter']
    jupiter = planets['jupiter barycenter']
    saturn = planets['saturn barycenter']
    uranus = planets['uranus barycenter']
    neptune = planets['neptune barycenter']
    

    pointAxes = (
        (0, 0, 0),
        (100, 0, 0),
        (0, 100, 0),
        (0, 0, 100)
        )

    edges = (
        (0,1),
        (0,2),
        (0,3)
        )

    def Axes():
        glBegin(GL_LINES)
        for edge in edges:
            for vertex in edge:
                glVertex3fv(pointAxes[vertex])
        glEnd()
        
    def resize(width, height):
        
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, float(width)/height, .1, 1000.)
        gluLookAt(0, 0, 100, # endroit où la camera est
                  0, 0, 0, # endroit où la camera regarde
                  0, 1, 0) # 
        glMatrixMode(GL_MODELVIEW)
            
        glLoadIdentity()


    def init():
        
        glEnable(GL_DEPTH_TEST)
        
        glShadeModel(GL_FLAT)
        glClearColor(0, 0, 0, 0.0)

        glEnable(GL_COLOR_MATERIAL)
        
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)        
        glLight(GL_LIGHT0, GL_POSITION,  (0, 0, 0, 1))

    def read_texture(filename):
        img = Image.open(filename)
        img_data = numpy.array(list(img.getdata()), numpy.int8)
        texture_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture_id)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.size[0], img.size[1], 0,
                     GL_RGB, GL_UNSIGNED_BYTE, img_data)
        return texture_id

    class Ball(object):
        
        def __init__(self, position, texture, size):
            
            self.position = array (position)
            self.texture = texture
            self.size = size
            self.display_list = None
            self.trace = []

        def render(self):
            glPushMatrix()
            global sunTexture
            global mercuryTexture
            global venusTexture
            global earthTexture
            global marsTexture
            global jupiterTexture
            global saturnTexture
            global uranusTexture
            global neptuneTexture
            if self.texture == "sunTexture":
                texture_id = sunTexture
            elif self.texture == "mercuryTexture":
                texture_id = mercuryTexture
            elif self.texture == "venusTexture":
                texture_id = venusTexture
            elif self.texture == "earthTexture":
                texture_id = earthTexture
            elif self.texture == "marsTexture":
                texture_id = marsTexture
            elif self.texture == "jupiterTexture":
                texture_id = jupiterTexture
            elif self.texture == "saturnTexture":
                texture_id = saturnTexture
            elif self.texture == "uranusTexture":
                texture_id = uranusTexture
            elif self.texture == "neptuneTexture":
                texture_id = neptuneTexture
                
            glEnable(GL_TEXTURE_2D)
            glBindTexture(GL_TEXTURE_2D, texture_id)
            glEnable(GL_TEXTURE_GEN_S)
            glEnable(GL_TEXTURE_GEN_T)
            glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
            glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
            glTranslatef(self.position[0],self.position[1],self.position[2])
            glutSolidSphere(self.size,50,50)
            glDisable(GL_TEXTURE_2D)
            glPopMatrix()
            glutSwapBuffers()

    def resetRotate():
        for i in saveChangeRotate:
            if i == "a":
                glRotatef(-1, 1, 0, 0)
            elif i == "z":
                glRotatef(1, 1, 0, 0)
            elif i == "e":
                glRotatef(-1, 0, 1, 0)
            elif i == "r":
                glRotatef(1, 0, 1, 0)
            elif i == "t":
                glRotatef(-1, 0, 0, 1)
            elif i == "y":
                glRotatef(1, 0, 0, 1)

    def backRotate():
        for i in saveChangeRotate:
            if i == "a":
                glRotatef(-1, 1, 0, 0)
            elif i == "z":
                glRotatef(1, 1, 0, 0)
            elif i == "e":
                glRotatef(-1, 0, 1, 0)
            elif i == "r":
                glRotatef(1, 0, 1, 0)
            elif i == "t":
                glRotatef(-1, 0, 0, 1)
            elif i == "y":
                glRotatef(1, 0, 0, 1)

    def run():
        pygame.init()

        if(fullScreen):
            infoObject = pygame.display.Info()
            screen = pygame.display.set_mode(SCREEN_SIZE, HWSURFACE|OPENGL|DOUBLEBUF|FULLSCREEN)
        else:
            screen = pygame.display.set_mode(SCREEN_SIZE, HWSURFACE|OPENGL|DOUBLEBUF)
            
        pygame.display.set_caption("Solarpy")
        
        resize(*SCREEN_SIZE)
        init()

        print("10%")

        #loading textures + storage
        global sunTexture
        global mercuryTexture
        global venusTexture
        global earthTexture
        global marsTexture
        global jupiterTexture
        global saturnTexture
        global uranusTexture
        global neptuneTexture
        sunTexture = read_texture('img/sun.jpg')
        print("20%")
        mercuryTexture = read_texture('img/mercury.jpg')
        print("30%")
        venusTexture = read_texture('img/venus.jpg')
        print("40%")
        earthTexture = read_texture('img/earth.jpg')
        print("50%")
        marsTexture = read_texture('img/mars.jpg')
        print("60%")
        jupiterTexture = read_texture('img/jupiter.jpg')
        print("70%")
        saturnTexture = read_texture('img/saturn.jpg')
        print("80%")
        uranusTexture = read_texture('img/uranus.jpg')
        print("90%")
        neptuneTexture = read_texture('img/neptune.jpg')
        print("99%")
             
        glMaterial(GL_FRONT, GL_AMBIENT, (0.1, 0.1, 0.1, 1.0))    
        glMaterial(GL_FRONT, GL_DIFFUSE, (1.0, 1.0, 1.0, 1.0))

        #tailles planètes
        sizeBall = 1
        sunSize = 2
        mercurySize = 0.05
        venusSize = 0.12
        earthSize = 0.13
        marsSize = 0.07
        jupiterSize = 1.43
        saturnSize = 1.21
        uranusSize = 0.51
        neptuneSize = 0.5

        #for zoom
        saveChangeRotate = ""
        saveChangeRotateReturn = ""
        #a  X+1
        #z  X-1
        #e  Y+1
        #r  Y-1
        #t  Z+1
        #y  Z-1

        pygame.key.set_repeat(1,20) #for smooth movement

        #path save:
        pos_hist_mercury = []
        pos_hist_venus = []
        pos_hist_earth = []
        pos_hist_mars = []
        pos_hist_jupiter = []
        pos_hist_saturn = []
        pos_hist_uranus = []
        pos_hist_neptune = []

        calculTime = 0
        
        while True:
            startTime = time.time()
            for event in pygame.event.get():          
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    pygame.quit()
                    quit()
                
                if event.type == KEYDOWN and event.key == K_UP:
                    for i in saveChangeRotate:
                        if i == "a":
                            glRotatef(-1, 1, 0, 0)
                        elif i == "z":
                            glRotatef(1, 1, 0, 0)
                        elif i == "e":
                            glRotatef(-1, 0, 1, 0)
                        elif i == "r":
                            glRotatef(1, 0, 1, 0)
                        elif i == "t":
                            glRotatef(-1, 0, 0, 1)
                        elif i == "y":
                            glRotatef(1, 0, 0, 1)
                    glTranslatef(0,0,0.5)
                    sunSize -= 0.01
                    sizeBall -= 0.001
                    for i in saveChangeRotateReturn:
                        if i == "a":
                            glRotatef(1, 1, 0, 0)
                        elif i == "z":
                            glRotatef(-1, 1, 0, 0)
                        elif i == "e":
                            glRotatef(1, 0, 1, 0)
                        elif i == "r":
                            glRotatef(-1, 0, 1, 0)
                        elif i == "t":
                            glRotatef(1, 0, 0, 1)
                        elif i == "y":
                            glRotatef(-1, 0, 0, 1)
                            
                if event.type == KEYDOWN and event.key == K_DOWN:
                    for i in saveChangeRotate:
                        if i == "a":
                            glRotatef(-1, 1, 0, 0)
                        elif i == "z":
                            glRotatef(1, 1, 0, 0)
                        elif i == "e":
                            glRotatef(-1, 0, 1, 0)
                        elif i == "r":
                            glRotatef(1, 0, 1, 0)
                        elif i == "t":
                            glRotatef(-1, 0, 0, 1)
                        elif i == "y":
                            glRotatef(1, 0, 0, 1)
                    glTranslatef(0,0,-0.5)
                    sunSize += 0.01
                    sizeBall += 0.001
                    for i in saveChangeRotateReturn:
                        if i == "a":
                            glRotatef(1, 1, 0, 0)
                        elif i == "z":
                            glRotatef(-1, 1, 0, 0)
                        elif i == "e":
                            glRotatef(1, 0, 1, 0)
                        elif i == "r":
                            glRotatef(-1, 0, 1, 0)
                        elif i == "t":
                            glRotatef(1, 0, 0, 1)
                        elif i == "y":
                            glRotatef(-1, 0, 0, 1)


                if event.type == KEYDOWN and event.key == K_a:
                    glRotatef(1, 1, 0, 0) #(degres, x, y, z)
                    saveChangeRotate = "a" + saveChangeRotate
                    saveChangeRotateReturn += "a"
                if event.type == KEYDOWN and event.key == K_z:
                    glRotatef(-1, 1, 0, 0)
                    saveChangeRotate = "z" + saveChangeRotate
                    saveChangeRotateReturn += "z"

                if event.type == KEYDOWN and event.key == K_LEFT:
                    glRotatef(1, 0, 1, 0)
                    saveChangeRotate = "e" + saveChangeRotate
                    saveChangeRotateReturn += "e"
                if event.type == KEYDOWN and event.key == K_RIGHT:
                    glRotatef(-1, 0, 1, 0)
                    saveChangeRotate = "r" + saveChangeRotate
                    saveChangeRotateReturn += "r"

                if event.type == KEYDOWN and event.key == K_q:
                    glRotatef(1, 0, 0, 1)
                    saveChangeRotate = "t" + saveChangeRotate
                    saveChangeRotateReturn += "t"
                if event.type == KEYDOWN and event.key == K_s:
                    glRotatef(-1, 0, 0, 1)
                    saveChangeRotate = "y" + saveChangeRotate
                    saveChangeRotateReturn += "y"
                    


            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
            glLight(GL_LIGHT0, GL_POSITION,  (0, 0, 0, 1))
            

            Sun = Ball([0,0,0], "sunTexture", sunSize)
            if(showSun == 1):
                Sun.render()
                
            Axes() #shows the axes
            
            #Update date
            if realTime:
                t = ts.now()
            else:
                global localSeconde
                localSeconde += calculTime*speed
                t = ts.utc(years, month, day, hour, minute, localSeconde)

            print(t.utc) #show the date used on the console

            #update planets positions
            if(showMercury == 1):
                posMercury = sun.at(t).observe(mercury).position.au
                MercuryX = posMercury[0] * 1.3
                MercuryY = posMercury[1] * 1.3
                MercuryZ = posMercury[2] * 1.3
                Mercury = Ball([MercuryX,MercuryY,MercuryZ], "mercuryTexture", mercurySize * sizeBall)
                Mercury.render()
                if (showPaths):
                    pos_hist_mercury.append((MercuryX,MercuryY,MercuryZ))
                    #render the path
                    glColor3f(255,255,255)
                    glLineWidth(10)
                    glBegin(GL_LINE_STRIP)
                    for xMercury, yMercury, zMercury in pos_hist_mercury:
                        glVertex3f(xMercury, yMercury, zMercury)
                    glEnd()

            if(showVenus == 1):
                posVenus = sun.at(t).observe(venus).position.au
                VenusX = posVenus[0] * 1.3
                VenusY = posVenus[1] * 1.3
                VenusZ = posVenus[2] * 1.3
                Venus = Ball([VenusX,VenusY,VenusZ], "venusTexture", venusSize * sizeBall)
                Venus.render()
                if (showPaths):
                    pos_hist_venus.append((VenusX,VenusY,VenusZ))
                    #render the path
                    glColor3f(255,255,255)
                    glLineWidth(10)
                    glBegin(GL_LINE_STRIP)
                    for xVenus, yVenus, zVenus in pos_hist_venus:
                        glVertex3f(xVenus, yVenus, zVenus)
                    glEnd()

            if(showEarth == 1):
                posEarth = sun.at(t).observe(earth).position.au
                EarthX = posEarth[0] * 1.3
                EarthY = posEarth[1] * 1.3
                EarthZ = posEarth[2] * 1.3
                Earth = Ball([EarthX,EarthY,EarthZ], "earthTexture", earthSize * sizeBall)
                Earth.render()
                if (showPaths):
                    pos_hist_earth.append((EarthX,EarthY,EarthZ))
                    #render the path
                    glColor3f(255,255,255)
                    glLineWidth(10)
                    glBegin(GL_LINE_STRIP)
                    for xEarth, yEarth, zEarth in pos_hist_earth:
                        glVertex3f(xEarth, yEarth, zEarth)
                    glEnd()

            if(showMars == 1):
                posMars = sun.at(t).observe(mars).position.au
                MarsX = posMars[0] * 1.3
                MarsY = posMars[1] * 1.3
                MarsZ = posMars[2] * 1.3
                Mars = Ball([MarsX,MarsY,MarsZ], "marsTexture", marsSize * sizeBall)
                Mars.render()
                if (showPaths):
                    pos_hist_mars.append((MarsX,MarsY,MarsZ))
                    #render the path
                    glColor3f(255,255,255)
                    glLineWidth(10)
                    glBegin(GL_LINE_STRIP)
                    for xMars, yMars, zMars in pos_hist_mars:
                        glVertex3f(xMars, yMars, zMars)
                    glEnd()

            if(showJupiter == 1):
                posJupiter = sun.at(t).observe(jupiter).position.au
                JupiterX = posJupiter[0] * 1.3
                JupiterY = posJupiter[1] * 1.3
                JupiterZ = posJupiter[2] * 1.3
                Jupiter = Ball([JupiterX,JupiterY,JupiterZ], "jupiterTexture", jupiterSize * sizeBall)
                Jupiter.render()
                if (showPaths):
                    pos_hist_jupiter.append((JupiterX,JupiterY,JupiterZ))
                    #render the path
                    glColor3f(255,255,255)
                    glLineWidth(10)
                    glBegin(GL_LINE_STRIP)
                    for xJupiter, yJupiter, zJupiter in pos_hist_jupiter:
                        glVertex3f(xJupiter, yJupiter, zJupiter)
                    glEnd()

            if(showSaturn == 1):
                posSaturn = sun.at(t).observe(saturn).position.au
                SaturnX = posSaturn[0] * 1.3
                SaturnY = posSaturn[1] * 1.3
                SaturnZ = posSaturn[2] * 1.3
                Saturn = Ball([SaturnX,SaturnY,SaturnZ], "saturnTexture", saturnSize * sizeBall)
                Saturn.render()
                if (showPaths):
                    pos_hist_saturn.append((SaturnX,SaturnY,SaturnZ))
                    #render the path
                    glColor3f(255,255,255)
                    glLineWidth(10)
                    glBegin(GL_LINE_STRIP)
                    for xSaturn, ySaturn, zSaturn in pos_hist_saturn:
                        glVertex3f(xSaturn, ySaturn, zSaturn)
                    glEnd()

            if(showUranus == 1):
                posUranus = sun.at(t).observe(uranus).position.au
                UranusX = posUranus[0] * 1.3
                UranusY = posUranus[1] * 1.3
                UranusZ = posUranus[2] * 1.3
                Uranus = Ball([UranusX,UranusY,UranusZ], "uranusTexture", uranusSize * sizeBall)
                Uranus.render()
                if (showPaths):
                    pos_hist_uranus.append((UranusX,UranusY,UranusZ))
                    #render the path
                    glColor3f(255,255,255)
                    glLineWidth(10)
                    glBegin(GL_LINE_STRIP)
                    for xUranus, yUranus, zUranus in pos_hist_uranus:
                        glVertex3f(xUranus, yUranus, zUranus)
                    glEnd()

            if(showNeptune == 1):
                posNeptune = sun.at(t).observe(neptune).position.au
                NeptuneX = posNeptune[0] * 1.3
                NeptuneY = posNeptune[1] * 1.3
                NeptuneZ = posNeptune[2] * 1.3
                Neptune = Ball([NeptuneX,NeptuneY,NeptuneZ], "neptuneTexture", neptuneSize * sizeBall)
                Neptune.render()
                if (showPaths):
                    pos_hist_neptune.append((NeptuneX,NeptuneY,NeptuneZ))
                    #render the path
                    glColor3f(255,255,255)
                    glLineWidth(1)
                    glBegin(GL_LINE_STRIP)
                    for xNeptune, yNeptune, zNeptune in pos_hist_neptune:
                        glVertex3f(xNeptune, yNeptune, zNeptune)
                    glEnd()
                    
            
            #Display
            pygame.display.flip()

            calculTime = (time.time()-startTime)
            
    run() #launches the pygame window
