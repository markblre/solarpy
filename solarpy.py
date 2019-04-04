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

showPaths = 0

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
    global showPaths
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

    showPaths = varShowPaths.get()

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
                 showJupiter, showSaturn, showUranus, showNeptune, showPaths,
                 years, month, day, hour, minute, second, realTime, speed)

def lauchSimulationInRealTime():
    global SCREEN_SIZE_W, SCREEN_SIZE_H
    incrementerVar()

    realTime = True

    if(fullScreen):
        SCREEN_SIZE_W = int(fenetre.winfo_screenwidth())*2
        SCREEN_SIZE_H = int(fenetre.winfo_screenheight())*2
    
    goSimulation((SCREEN_SIZE_W, SCREEN_SIZE_H), fullScreen, showSun, showMercury, showVenus, showEarth, showMars,
                 showJupiter, showSaturn, showUranus, showNeptune, showPaths,
                 years, month, day, hour, minute, second, realTime, speed)

#tkinter
fenetre = Tk()
m = fenetre.maxsize()
fenetre.geometry('{}x{}+0+0'.format(*m))
fenetre.title("Solarpy")
image = PhotoImage(file='img/spaceBackground.gif', master=fenetre)
canvas = Canvas(fenetre, width=m[0], height=m[1])
canvas.pack()
canvas.create_image((m[0]//2, m[1]//2), image=image)
fenetre.filename = ""

def saveFile(ev=None):
    incrementerVar()
    
    if fenetre.filename == "":
        saveFileAs()
    else:
        fichier = open(fenetre.filename, "w")
        fichier.write(str(fullScreen) + "\n" + str(SCREEN_SIZE_W) + "\n" + str(SCREEN_SIZE_H) + "\n" + str(showSun) + "\n" + str(showMercury) + "\n" + str(showVenus) + "\n" + str(showEarth) + "\n" + str(showMars) + "\n" + str(showJupiter)
                      + "\n" + str(showSaturn) + "\n" + str(showUranus) + "\n" + str(showNeptune) + "\n" + str(showPaths) + "\n" + str(years) + "\n" + str(month) + "\n" + str(day)
                      + "\n" + str(hour) + "\n" + str(minute) + "\n" + str(second) + "\n" + str(speed))
        fichier.close()

def saveFileAs(ev=None):
    incrementerVar()
    
    fenetre.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
    fichier = open(fenetre.filename, "w")
    fichier.write(str(fullScreen) + "\n" + str(SCREEN_SIZE_W) + "\n" + str(SCREEN_SIZE_H) + "\n" + str(showSun) + "\n" + str(showMercury) + "\n" + str(showVenus) + "\n" + str(showEarth) + "\n" + str(showMars) + "\n" + str(showJupiter)
                  + "\n" + str(showSaturn) + "\n" + str(showUranus) + "\n" + str(showNeptune) + "\n" + str(showPaths) + "\n" + str(years) + "\n" + str(month) + "\n" + str(day)
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

    if fichierSplit[12] == "0":
        boutonShowPaths.deselect()
    else:
        boutonShowPaths.select()

    varsAnnee.set(fichierSplit[13])
    varsMois.set(fichierSplit[14])
    varsJour.set(fichierSplit[15])
    varsHeure.set(fichierSplit[16])
    varsMinute.set(fichierSplit[17])
    varsSeconde.set(fichierSplit[18])

    varsVitesse.set(fichierSplit[19])

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
    boutonShowPaths.deselect()
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
policeSize = 16
#barre de menu
menubar = Menu(fenetre)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Open...             Ctrl+o", command=openFile)
fenetre.bind_all("<Command-o>", openFile)
menu1.add_command(label="Save           Ctrl+s", command=saveFile)
fenetre.bind_all("<Command-s>", saveFile)
menu1.add_command(label="Save as...   Ctrl+Shift+s", command=saveFileAs)
fenetre.bind_all("<Command-S>", saveFileAs)
menu1.add_separator()
menu1.add_command(label="Reset", command=reset)
menu1.add_separator()
menu1.add_command(label="Quit", command=quitte)
menubar.add_cascade(label="File", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="About") #ouvrir une page de crédit
menubar.add_cascade(label="Help", menu=menu2)

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
varShowPaths = IntVar()
varsAnnee = StringVar()
varsMois = StringVar()
varsJour = StringVar()
varsHeure = StringVar()
varsMinute = StringVar()
varsSeconde = StringVar()
varsVitesse = StringVar()

#LabelFrame
screenLabelFrame = LabelFrame(fenetre, text="Screen parameters", padx=20, pady=20, bg="white", font=(None,policeSize))
screenLabelFrame.place(x=(m[0]/2)-225, y=(m[1]/2)-225, width=300, height=400, anchor=CENTER)
starsLabelFrame = LabelFrame(fenetre, text="Stars parameters", padx=20, pady=20, bg="white", font=(None,policeSize))
starsLabelFrame.place(x=(m[0]/2)-225, y=(m[1]/2)+225, width=300, height=400, anchor=CENTER)
dateLabelFrame = LabelFrame(fenetre, text="Date parameters", padx=20, pady=20, bg="white", font=(None,policeSize))
dateLabelFrame.place(x=(m[0]/2)+225, y=(m[1]/2)-225, width=300, height=400, anchor=CENTER)
startLabelFrame = LabelFrame(fenetre, text="Start parameters", padx=20, pady=20, bg="white", font=(None,policeSize))
startLabelFrame.place(x=(m[0]/2)+225, y=(m[1]/2)+225, width=300, height=400, anchor=CENTER)

#buttons
#display parameters
boutonFullScreen = Checkbutton(screenLabelFrame, text="Full Screen", variable=varFullScreen, font=(None,policeSize))
boutonFullScreen.pack()
labelSCREEN_SIZE_W = Label(screenLabelFrame, text="Screen size width", font=(None,policeSize))
labelSCREEN_SIZE_W.pack()
sSCREEN_SIZE_W = Spinbox(screenLabelFrame, from_=0, textvariable=varsSCREEN_SIZE_W)
sSCREEN_SIZE_W.pack()
labelSCREEN_SIZE_H = Label(screenLabelFrame, text="Screen size height", font=(None,policeSize))
labelSCREEN_SIZE_H.pack()
sSCREEN_SIZE_H = Spinbox(screenLabelFrame, from_=0, textvariable=varsSCREEN_SIZE_H)
sSCREEN_SIZE_H.pack()

#show planets
boutonSelectAll = Button(starsLabelFrame, text="Select/Deselect all", command=SelectDeselectAll, font=(None,policeSize))
boutonSelectAll.pack()
boutonShowSun = Checkbutton(starsLabelFrame, text="Show Sun", variable=varShowSun, font=(None,policeSize))
boutonShowSun.pack()
boutonShowMercury = Checkbutton(starsLabelFrame, text="Show Mercury", variable=varShowMercury, font=(None,policeSize))
boutonShowMercury.pack()
boutonShowVenus = Checkbutton(starsLabelFrame, text="Show Venus", variable=varShowVenus, font=(None,policeSize))
boutonShowVenus.pack()
boutonShowEarth = Checkbutton(starsLabelFrame, text="Show Earth", variable=varShowEarth, font=(None,policeSize))
boutonShowEarth.pack()
boutonShowMars = Checkbutton(starsLabelFrame, text="Show Mars", variable=varShowMars, font=(None,policeSize))
boutonShowMars.pack()
boutonShowJupiter = Checkbutton(starsLabelFrame, text="Show Jupiter", variable=varShowJupiter, font=(None,policeSize))
boutonShowJupiter.pack()
boutonShowSaturn = Checkbutton(starsLabelFrame, text="Show Saturn", variable=varShowSaturn, font=(None,policeSize))
boutonShowSaturn.pack()
boutonShowUranus = Checkbutton(starsLabelFrame, text="Show Uranus", variable=varShowUranus, font=(None,policeSize))
boutonShowUranus.pack()
boutonShowNeptune = Checkbutton(starsLabelFrame, text="Show Neptune", variable=varShowNeptune, font=(None,policeSize))
boutonShowNeptune.pack()
labelBlank = Label(starsLabelFrame, text="", font=(None,policeSize))
labelBlank.pack()
boutonShowPaths = Checkbutton(starsLabelFrame, text="Show paths", variable=varShowPaths, font=(None,policeSize))
boutonShowPaths.pack()

#date
labelAnnee = Label(dateLabelFrame, text="Years", font=(None,policeSize))
labelAnnee.pack()
sAnnee = Spinbox(dateLabelFrame, from_=1970, to=10000, textvariable=varsAnnee)
sAnnee.pack()
labelMois = Label(dateLabelFrame, text="Month", font=(None,policeSize))
labelMois.pack()
sMois = Spinbox(dateLabelFrame, from_=1, to=12, textvariable=varsMois)
sMois.pack()
labelJour = Label(dateLabelFrame, text="Day", font=(None,policeSize))
labelJour.pack()
sJour = Spinbox(dateLabelFrame, from_=1, to=31, textvariable=varsJour)
sJour.pack()
labelHeure = Label(dateLabelFrame, text="Hour", font=(None,policeSize))
labelHeure.pack()
sHeure = Spinbox(dateLabelFrame, from_=0, to=23, textvariable=varsHeure)
sHeure.pack()
labelMinute = Label(dateLabelFrame, text="Minute", font=(None,policeSize))
labelMinute.pack()
sMinute = Spinbox(dateLabelFrame, from_=0, to=60, textvariable=varsMinute)
sMinute.pack()
labelSeconde = Label(dateLabelFrame, text="Second", font=(None,policeSize))
labelSeconde.pack()
sSeconde = Spinbox(dateLabelFrame, from_=0, to=60, textvariable=varsSeconde)
sSeconde.pack()

#vitesse
labelVitesse = Label(startLabelFrame, text="Simulation speed", font=(None,policeSize))
labelVitesse.pack()
sVitesse = Spinbox(startLabelFrame, from_=1.0, to=100000, textvariable=varsVitesse)
sVitesse.pack()

#boutons start
boutonStart = Button(fenetre, text="Launch", command=lauchSimulation, font=(None,policeSize))
boutonStart.place(x=m[0]-300-10, y=(m[1]/2)-12.5-50, width=250, height=50)
boutonStartRealTime = Button(fenetre, text="Launch with actual time", command=lauchSimulationInRealTime, font=(None,policeSize))
boutonStartRealTime.place(x=m[0]-300-10, y=(m[1]/2)-12.5+50, width=250, height=50)

reset()
fenetre.mainloop()
