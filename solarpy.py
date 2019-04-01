from simulation import *
from tkinter import *
from tkinter.messagebox import *
from tkinter import filedialog

fullScreen = False
SCREEN_SIZE_W = 0
SCREEN_SIZE_H = 0

#afficher les planetes ?
showSun = 0
showMercury = 0
showVenus = 0
showEarth = 0
showMars = 0
showJupiter = 0
showSaturn = 0
showUranus = 0
showNeptune = 0

#date
years = 1979
month = 3
day = 17
hour = 22
minute = 45
second = 0

#vitesse
speed = 1

def incrementerVar():
    global fullScreen
    global SCREEN_SIZE_W
    global SCREEN_SIZE_H
    global showSun
    global showMercury
    global showVenus
    global showEarth
    global showMars
    global showJupiter
    global showSaturn
    global showUranus
    global showNeptune
    global years
    global month
    global day
    global hour 
    global minute
    global second
    global speed

    fullScreen = varFullScreen.get()
    SCREEN_SIZE_W = int(sSCREEN_SIZE_W.get())
    SCREEN_SIZE_H = int(sSCREEN_SIZE_H.get())

    showSun = varShowSun.get()
    showMercury = varShowMercury.get()
    showVenus = varShowVenus.get()
    showEarth = varShowEarth.get()
    showMars = varShowMars.get()
    showJupiter = varShowJupiter.get()
    showSaturn = varShowSaturn.get()
    showUranus = varShowUranus.get()
    showNeptune = varShowNeptune.get()

    years = int(sAnnee.get())
    month = int(sMois.get())
    day = int(sJour.get())
    hour = int(sHeure.get())
    minute = int(sMinute.get())
    second = int(sSeconde.get())

    speed = float(sVitesse.get())
    
def lauchSimulation():
    global SCREEN_SIZE_W, SCREEN_SIZE_H
    incrementerVar()
    
    realTime = False

    if(fullScreen):
        SCREEN_SIZE_W = int(fenetre.winfo_screenwidth())*2
        SCREEN_SIZE_H = int(fenetre.winfo_screenheight())*2
        
    goSimulation((SCREEN_SIZE_W, SCREEN_SIZE_H), fullScreen, showSun, showMercury, showVenus, showEarth, showMars,
                 showJupiter, showSaturn, showUranus, showNeptune,
                 years, month, day, hour, minute, second, realTime, speed)

def lauchSimulationInRealTime():
    global SCREEN_SIZE_W, SCREEN_SIZE_H
    incrementerVar()

    realTime = True

    if(fullScreen):
        SCREEN_SIZE_W = int(fenetre.winfo_screenwidth())*2
        SCREEN_SIZE_H = int(fenetre.winfo_screenheight())*2
    
    goSimulation((SCREEN_SIZE_W, SCREEN_SIZE_H), fullScreen, showSun, showMercury, showVenus, showEarth, showMars,
                 showJupiter, showSaturn, showUranus, showNeptune,
                 years, month, day, hour, minute, second, realTime, speed)

#tkinter
fenetre = Tk()
fenetre.filename = ""

def saveFile(ev=None):
    incrementerVar()
    
    if fenetre.filename == "":
        saveFileAs()
    else:
        fichier = open(fenetre.filename, "w")
        fichier.write(str(fullScreen) + "\n" + str(SCREEN_SIZE_W) + "\n" + str(SCREEN_SIZE_H) + "\n" + str(showSun) + "\n" + str(showMercury) + "\n" + str(showVenus) + "\n" + str(showEarth) + "\n" + str(showMars) + "\n" + str(showJupiter)
                      + "\n" + str(showSaturn) + "\n" + str(showUranus) + "\n" + str(showNeptune) + "\n" + str(years) + "\n" + str(month) + "\n" + str(day)
                      + "\n" + str(hour) + "\n" + str(minute) + "\n" + str(second) + "\n" + str(speed))
        fichier.close()

def saveFileAs(ev=None):
    incrementerVar()
    fenetre.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
    fichier = open(fenetre.filename, "w")
    fichier.write(str(fullScreen) + "\n" + str(SCREEN_SIZE_W) + "\n" + str(SCREEN_SIZE_H) + "\n" + str(showSun) + "\n" + str(showMercury) + "\n" + str(showVenus) + "\n" + str(showEarth) + "\n" + str(showMars) + "\n" + str(showJupiter)
                  + "\n" + str(showSaturn) + "\n" + str(showUranus) + "\n" + str(showNeptune) + "\n" + str(years) + "\n" + str(month) + "\n" + str(day)
                  + "\n" + str(hour) + "\n" + str(minute) + "\n" + str(second) + "\n" + str(speed))
    fichier.close()

def openFile(ev=None):
    fenetre.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
    fichier = open(fenetre.filename, "r")
    fichierSplit = str(fichier.read()).split()

    if fichierSplit[0] == "0":
        boutonFullScreen.deselect()
    else:
        boutonFullScreen.select()

    varsSCREEN_SIZE_W.set(fichierSplit[1])
    varsSCREEN_SIZE_H.set(fichierSplit[2])
        
    if fichierSplit[3] == "0":
        boutonShowSun.deselect()
    else:
        boutonShowSun.select()

    if fichierSplit[4] == "0":
        boutonShowMercury.deselect()
    else:
        boutonShowMercury.select()
    fichier.close()

    if fichierSplit[5] == "0":
        boutonShowVenus.deselect()
    else:
        boutonShowVenus.select()
    fichier.close()

    if fichierSplit[6] == "0":
        boutonShowEarth.deselect()
    else:
        boutonShowEarth.select()
    fichier.close()

    if fichierSplit[7] == "0":
        boutonShowMars.deselect()
    else:
        boutonShowMars.select()
    fichier.close()

    if fichierSplit[8] == "0":
        boutonShowJupiter.deselect()
    else:
        boutonShowJupiter.select()
    fichier.close()

    if fichierSplit[9] == "0":
        boutonShowSaturn.deselect()
    else:
        boutonShowSaturn.select()
    fichier.close()

    if fichierSplit[10] == "0":
        boutonShowUranus.deselect()
    else:
        boutonShowUranus.select()
    fichier.close()

    if fichierSplit[11] == "0":
        boutonShowNeptune.deselect()
    else:
        boutonShowNeptune.select()

    varsAnnee.set(fichierSplit[12])
    varsMois.set(fichierSplit[13])
    varsJour.set(fichierSplit[14])
    varsHeure.set(fichierSplit[15])
    varsMinute.set(fichierSplit[16])
    varsSeconde.set(fichierSplit[17])

    varsVitesse.set(fichierSplit[18])

    fichier.close()

def reset():
    boutonFullScreen.deselect()
    varsSCREEN_SIZE_W.set(fenetre.winfo_screenwidth())
    varsSCREEN_SIZE_H.set(fenetre.winfo_screenheight())
    boutonShowSun.deselect()
    boutonShowMercury.deselect()
    boutonShowVenus.deselect()
    boutonShowEarth.deselect()
    boutonShowMars.deselect()
    boutonShowJupiter.deselect()
    boutonShowSaturn.deselect()
    boutonShowUranus.deselect()
    boutonShowNeptune.deselect()
    varsAnnee.set("1970")
    varsMois.set("1")
    varsJour.set("1")
    varsHeure.set("0")
    varsMinute.set("0")
    varsSeconde.set("0")
    varsVitesse.set("1.0")

selectDeselect = False
def SelectDeselectAll():
    global selectDeselect
    selectDeselect = not selectDeselect
    
    if selectDeselect:
        boutonShowSun.select()
        boutonShowMercury.select()
        boutonShowVenus.select()
        boutonShowEarth.select()
        boutonShowMars.select()
        boutonShowJupiter.select()
        boutonShowSaturn.select()
        boutonShowUranus.select()
        boutonShowNeptune.select()
    else:
        boutonShowSun.deselect()
        boutonShowMercury.deselect()
        boutonShowVenus.deselect()
        boutonShowEarth.deselect()
        boutonShowMars.deselect()
        boutonShowJupiter.deselect()
        boutonShowSaturn.deselect()
        boutonShowUranus.deselect()
        boutonShowNeptune.deselect()
        
def quitte():
    if askyesno('Quitter', 'Êtes-vous sûr de vouloir quitter?'):
        fenetre.destroy()

#affichage
#barre de menu
menubar = Menu(fenetre)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Ouvrir...             Ctrl+o", command=openFile)
fenetre.bind_all("<Command-o>", openFile)
menu1.add_command(label="Enregistrer           Ctrl+s", command=saveFile)
fenetre.bind_all("<Command-s>", saveFile)
menu1.add_command(label="Enregistrer sous...   Ctrl+Shift+s", command=saveFileAs)
fenetre.bind_all("<Command-S>", saveFileAs)
menu1.add_separator()
menu1.add_command(label="Réinitialiser", command=reset)
menu1.add_separator()
menu1.add_command(label="Quitter", command=quitte)
menubar.add_cascade(label="Fichier", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="A propos") #ouvrir une page de crédit
menubar.add_cascade(label="Aide", menu=menu2)

fenetre.config(menu=menubar)

#vars
varFullScreen = IntVar()
varsSCREEN_SIZE_W = StringVar()
varsSCREEN_SIZE_H = StringVar()
varShowSun = IntVar()
varShowMercury = IntVar()
varShowVenus = IntVar()
varShowEarth = IntVar()
varShowMars = IntVar()
varShowJupiter = IntVar()
varShowSaturn = IntVar()
varShowUranus = IntVar()
varShowNeptune = IntVar()
varsAnnee = StringVar()
varsMois = StringVar()
varsJour = StringVar()
varsHeure = StringVar()
varsMinute = StringVar()
varsSeconde = StringVar()
varsVitesse = StringVar()

#buttons
#display
boutonFullScreen = Checkbutton(fenetre, text="Full Screen", variable=varFullScreen)
boutonFullScreen.pack()
labelSCREEN_SIZE_W = Label(fenetre, text="Screen size width")
labelSCREEN_SIZE_W.pack()
sSCREEN_SIZE_W = Spinbox(fenetre, from_=0, textvariable=varsSCREEN_SIZE_W)
sSCREEN_SIZE_W.pack()
labelSCREEN_SIZE_H = Label(fenetre, text="Screen size height")
labelSCREEN_SIZE_H.pack()
sSCREEN_SIZE_H = Spinbox(fenetre, from_=0, textvariable=varsSCREEN_SIZE_H)
sSCREEN_SIZE_H.pack()

#planets
boutonSelectAll = Button(fenetre, text="Select/Deselect all", command=SelectDeselectAll)
boutonSelectAll.pack()
boutonShowSun = Checkbutton(fenetre, text="ShowSun", variable=varShowSun)
boutonShowSun.pack()
boutonShowMercury = Checkbutton(fenetre, text="ShowMercury", variable=varShowMercury)
boutonShowMercury.pack()
boutonShowVenus = Checkbutton(fenetre, text="ShowVenus", variable=varShowVenus)
boutonShowVenus.pack()
boutonShowEarth = Checkbutton(fenetre, text="ShowEarth", variable=varShowEarth)
boutonShowEarth.pack()
boutonShowMars = Checkbutton(fenetre, text="ShowMars", variable=varShowMars)
boutonShowMars.pack()
boutonShowJupiter = Checkbutton(fenetre, text="ShowJupiter", variable=varShowJupiter)
boutonShowJupiter.pack()
boutonShowSaturn = Checkbutton(fenetre, text="ShowSaturn", variable=varShowSaturn)
boutonShowSaturn.pack()
boutonShowUranus = Checkbutton(fenetre, text="ShowUranus", variable=varShowUranus)
boutonShowUranus.pack()
boutonShowNeptune = Checkbutton(fenetre, text="ShowNeptune", variable=varShowNeptune)
boutonShowNeptune.pack()

#date
labelAnnee = Label(fenetre, text="Année")
labelAnnee.pack()
sAnnee = Spinbox(fenetre, from_=1970, to=10000, textvariable=varsAnnee)
sAnnee.pack()
labelMois = Label(fenetre, text="Mois")
labelMois.pack()
sMois = Spinbox(fenetre, from_=1, to=12, textvariable=varsMois)
sMois.pack()
labelJour = Label(fenetre, text="Jour")
labelJour.pack()
sJour = Spinbox(fenetre, from_=1, to=31, textvariable=varsJour)
sJour.pack()
labelHeure = Label(fenetre, text="Heure")
labelHeure.pack()
sHeure = Spinbox(fenetre, from_=0, to=23, textvariable=varsHeure)
sHeure.pack()
labelMinute = Label(fenetre, text="Minute")
labelMinute.pack()
sMinute = Spinbox(fenetre, from_=0, to=60, textvariable=varsMinute)
sMinute.pack()
labelSeconde = Label(fenetre, text="Seconde")
labelSeconde.pack()
sSeconde = Spinbox(fenetre, from_=0, to=60, textvariable=varsSeconde)
sSeconde.pack()

#vitesse
labelVitesse = Label(fenetre, text="Vitesse")
labelVitesse.pack()
sVitesse = Spinbox(fenetre, from_=1.0, to=100000, textvariable=varsVitesse)
sVitesse.pack()

#boutons start
boutonStart = Button(fenetre, text="Launch", command=lauchSimulation)
boutonStart.pack()
boutonStartRealTime = Button(fenetre, text="Launch with real time", command=lauchSimulationInRealTime)
boutonStartRealTime.pack()

reset()
fenetre.mainloop()
