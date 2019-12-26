import random
import tkinter
from tkinter import *

momentanesAuto=None;

rareoltimer=[]
raregold=[]
oldtimer=[]
gold=[]
raresilver=[]
silver=[]
rarebronze=[]
bronze=[]

vorkommen=[1001,501,201,101,51,27,10,1]

# ------------------------ Klasse Spieler    
class Spieler:
    def __init__(self,name):
        self.name=name
        self.autoliste=[]
    def __str__(self):
        return self.name+"("+str(len(self.autoliste))+")"
        
        

    
# ------------------------ Klasse Auto    
class Auto :
    def __init__(self, vorkommen, name, geschwindigkeit=None, beschleunigung=None,preis="unbekannt"):
        self.vorkommen=vorkommen
        self.name = name
        self.geschwindigkeit = geschwindigkeit
        self.beschleunigung = beschleunigung
        self.preis=preis
        self.bestand=1
        
        
    def __str__(self):
        return "Auto: %s,%s,%s,%s,%s,%dx"%(self.vorkommen,self.name, self.geschwindigkeit, self.beschleunigung, self.preis, self.bestand)
        

spielerliste=[Spieler("1"),Spieler("2")]
momentanerSpieler=len(spielerliste)-1

def getMomentanerSpieler():
    global spielerliste
    return spielerliste[momentanerSpieler]

def nextSpieler():
    global momentanerSpieler
    momentanerSpieler+=1
    print("Next Spieler: "+str(momentanerSpieler))
    if momentanerSpieler == len(spielerliste):
        momentanerSpieler = 0
    spielerlabel.config(text=str(getMomentanerSpieler()))

# ------------------ Sammeln -------------------
def button1Click() :
    global momentanesAuto
    spieler=getMomentanerSpieler()
    # sammle altes auto in der liste
    if momentanesAuto!=None:
        autoGefunden=False
        for einAutoInListe in spieler.autoliste:
            if (einAutoInListe.name == momentanesAuto.name):
                # doppelter eintrag
                einAutoInListe.bestand+=1
                autoGefunden=True
        if not autoGefunden:
            spieler.autoliste.append(momentanesAuto)
    # wechsle spieler
    nextSpieler()
    # erzeuge neues auto
    momentanesAuto=zufallsauto()
    Anzeige.config(text=momentanesAuto)
    

# ------------------ Schliessen
def button2Click() :
    Fenster.destroy()

# ------------------ Anzeigen Autoliste
def button3Click() :
    spieler=getMomentanerSpieler()
    text=""
    for auto in spieler.autoliste:
        text+=str(auto)+'\n'
    Anzeige.config(text=text)

# ------------------ Skip Auto
def button4Click() :
    nextSpieler()
    momentanesAuto=zufallsauto()
    Anzeige.config(text=momentanesAuto)
    
    
# ------------------ Alles Schliessen
def buttonHauptmenüClick() :
    Fenster.destroy()
    Hauptmenü.destroy()


        

# ------------------ lade die autos aus dateien
def loadautos(autoklasse):
    AutosAusDatei=[]
    with open(autoklasse, "r") as f:
        lines=f.readlines()
        print(autoklasse ,len(lines))
        for line in lines:
            values=line.split(",")
            AutosAusDatei.append(Auto(autoklasse,*values))
        for auto in AutosAusDatei:
            print(auto)
    return AutosAusDatei

rareoldtimer=loadautos("rareoldtimer")
raregold=loadautos("raregold")
oldtimer=loadautos("oldtimer")
gold=loadautos("gold")
raresilver=loadautos("raresilver")
silver=loadautos("silver")
rarebronze=loadautos("rarebronze")
bronze=loadautos("bronze")


          
def zufallsauto() :
    wahrscheinlichkeit=random.randint(1,5522)
    print(wahrscheinlichkeit)

    if wahrscheinlichkeit%vorkommen[0]==0:
        if len(rareoldtimer)>0:
            auto = rareoldtimer[random.randint(0,(len(rareoldtimer))-1)]
    elif wahrscheinlichkeit%vorkommen[1]==0:
        if len(raregold)>0:
            auto = raregold[random.randint(0,(len(raregold))-1)]
    elif wahrscheinlichkeit%vorkommen[2]==0:
        if len(oldtimer)>0:
            auto = oldtimer[random.randint(0,(len(oldtimer))-1)]
    elif wahrscheinlichkeit%vorkommen[3]==0:
        if len(gold)>0:    
            auto = gold[random.randint(0,(len(gold))-1)]
    elif wahrscheinlichkeit%vorkommen[4]==0:
        if len(raresilver)>0:    
            auto = raresilver[random.randint(0,(len(raresilver))-1)]
    elif wahrscheinlichkeit%vorkommen[5]==0:
        if len(silver)>0:    
            auto = silver[random.randint(0,(len(silver))-1)]
    elif wahrscheinlichkeit%vorkommen[6]==0:
        if len(rarebronze)>0:    
            auto = rarebronze[random.randint(0,(len(rarebronze))-1)]
    else:
        if len(bronze)>0:    
            auto = bronze[random.randint(0, (len(bronze))-1)]
    return auto

Fenster = Tk()
Hauptmenü = Tk()
auto=zufallsauto()
    
Anzeige = tkinter.Label(Fenster, text="AutoSammler v1.0 Klicke zum Sammeln!")
Anzeige.pack()
Hauptmenüanzeige = tkinter.Label(Hauptmenü, text="AutoSammler v1.0!")
Hauptmenüanzeige.pack()
spielerlabel = tkinter.Label(Fenster, text=str(getMomentanerSpieler()))
ButtonHauptmenü = Button(Hauptmenü, text="schließen",
command = buttonHauptmenüClick)
Button1 = Button(Fenster, text="Sammeln!",
command = button1Click)
Button2 = Button(Fenster, text="schließen!",
command = button2Click)
Button3 = Button(Fenster, text="Gesammelte Autos ansehen!",
command = button3Click)
Button4 = Button(Fenster, text="Überspringen und geld einsammeln",
command = button4Click)
spielerlabel.pack()
Button1.pack()
Button2.pack()
Button3.pack()
Button4.pack()
ButtonHauptmenü.pack()

Fenster.mainloop()


