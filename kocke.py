import tkinter as tk
import random

def pari3(met2):
    par = 0
    for a in range(1,7):
        if met2.count(a) == 2:
            par += 1
    if par == 3:
        return True
    else:
        return False

def oceni(met):
    tocke = 0
    kocke = len(met)
    ##preverimo za mete 6 kock
    if len(met)== 6:
        if met == [1,2,3,4,5,6]:
            return (1500, 0)
        elif pari3(met):
            return (1500, 0)

    ##preverimo za mete 3 ali več kock
    if len(met) >= 3:
        if met.count(1) >= 3:
            tocke += 1000*(met.count(1) - 2)
            kocke = kocke - met.count(1)
        for a in range(2,7):
            if met.count(a) >= 3:
                tocke += a*100*(met.count(a) - 2)
                kocke = kocke - (met.count(a))
                ##prevermo še za ostalo

    for a in [1,5]:
        if met.count(a) < 3:
            if a == 1:
                x = 100
            else:
                x = 50
            tocke += met.count(a) * x
            kocke = kocke - met.count(a)
    return (tocke, kocke)


##def roll(k=1):
##    meti = []
##    for a in range(k):
##        a = random.randint(1, 6)
##        meti.append(a)
##    meti.sort()
##    print(meti)
##    return meti

class kocka:
    def __init__(self, master):
        self.frame = tk.Frame(master)

        self.plat = tk.IntVar(master, value = None)
        self.cup = tk.BooleanVar(master, value = True)
        self.display = tk.Label(self.frame, textvariable = self.plat)
        self.display.grid(row=0, column = 0)        
        self.display = tk.Checkbutton(self.frame, variable = self.cup)
        self.display.grid(row=1, column=0)
      
        
##        self.photo = tk.PhotoImage(file = './six.png')
##        self.pikice.create_image(0,0, image=self.photo)
        

    def roll(self):
        self.plat.set(random.randint(1, 6))

    def loncek(self):
        x = self.cup.get()
        self.cup.set(not (x))


    

class tabela:
    def __init__(self, master):
        self.kocke = []
        for a in range(6):
            dice=kocka(master)
            dice.frame.grid(row=0,column=a+1)
            self.kocke.append(dice)

        self.gump = tk.Button(master, text="Vrzi vse", command = self.spusti)
        self.gump.grid(row = 0, column =0)
##        dice1 = kocka(master)
##        dice1.frame.grid(row = 0, column = 0)

    def spusti(self):
        pike = []
        for a in self.kocke:
            if a.cup.get():
                a.roll()
                pike.append(a.plat.get())
        a=oceni(pike)
        print (a)

    


root=tk.Tk()
root.title("10k")
pregled = tabela(root)
root.mainloop
