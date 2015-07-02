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
    kocke = len(met),
    ##preverimo za mete 6 kock
    if len(met)== 6:
        if met == [1,2,3,4,5,6]:
            return 1500
        elif pari3(met):
            return 1500

    ##preverimo za mete 3 ali več kock
    if len(met) >= 3:
        if met.count(1) >= 3:
            tocke += 1000*(met.count(1) - 2)
        for a in range(2,7):
            if met.count(a) >= 3:
                tocke += a*100*(met.count(a) - 2)
                ##prevermo še za ostalo

    if met.count(1) < 3:
        tocke += 100 * met.count(1)
    if met.count(5) < 3:
        tocke += 50 * met.count(5)
    return tocke


##def roll(k=1):
##    meti = []
##    for a in range(k):
##        a = random.randint(1, 6)
##        meti.append(a)
##    meti.sort()
##    print(meti)
##    return meti

class kocka:
    def __init__(self, master,tabela):
        self.frame = tk.Frame(master)

        self.plat = tk.IntVar(master, value = None)
        self.cup = tk.BooleanVar(master, value = True)
        self.display = tk.Label(self.frame, textvariable = self.plat)
        self.display.grid(row=0, column = 0)        
        self.display = tk.Checkbutton(self.frame, variable = self.cup, command=tabela.refresh)
        #self.display.bind("<Button-1>", tabela.tockuj)
        self.display.grid(row=1, column=0)
     ##   self.display.config(state=tk.DISABLED)
      
        
##        self.photo = tk.PhotoImage(file = './six.png')
##        self.pikice.create_image(0,0, image=self.photo)
        

    def roll(self):
        self.plat.set(random.randint(1, 6))

    def loncek(self):
        x = self.cup.get()
        self.cup.set(not (x))


    

class tabela:
    def __init__(self, master):
        self.igralec = tk.StringVar(master, value="Igralec")
        self.tocke = tk.IntVar(master, value=None)
        self.rezultat=tk.IntVar(master, value=0)
        self.kocke = []
        for a in range(6):
            dice=kocka(master, self)
            dice.frame.grid(row=1,column=a+1)
            self.kocke.append(dice)

        self.ime0= tk.Label(master, text="Tvoje ime:")
        self.ime0.grid(row=0, column=0, columnspan=2)
        self.ime1= tk.Entry(master, textvariable=self.igralec)
        self.ime1.grid(row=0, column=2, columnspan=5)
        self.gump = tk.Button(master, text="Vrzi", command = self.spusti)
        self.gump.grid(row = 1, column =0)
        self.dosezek0 = tk.Label(master, text="tvoje točke:")
        self.dosezek0.grid(row =2, column =1, columnspan=2)
        self.dosezek1 = tk.Label(master, textvariable=self.tocke)
        self.dosezek1.grid(row =2, column =3)
        self.dosezek2 = tk.Label(master, text="to rundo")
        self.dosezek2.grid(row =2, column =4, columnspan=2)
        self.dosezek3 = tk.Label(master, textvariable=self.rezultat)
        self.dosezek3.grid(row =2, column =6)
        self.pravila = tk.Label(master, text="PRAVILA: https://en.wikipedia.org/wiki/Dice_10000")
        self.pravila.grid(row =3, column =0, columnspan=7)
        
        
        self.koncaj= tk.Button(master, text="končaj", command = self.nova_igra_z)
        self.koncaj.grid(row =2, column =0)
##        dice1 = kocka(master)
##        dice1.frame.grid(row = 0, column = 0)
        
    def refresh(self):
        self.tockuj()
        if self.vseh6():
            self.nova_igra()

    def vseh6(self):
        for k in self.kocke:
            if k.plat.get() != 0:
                return False
        return True
        

    def tockuj(self):
        pike=[]
        for a in self.kocke:
            if a.cup.get()== False:
                pike.append(a.plat.get())
        a=oceni(pike)
        
        if a == 0:
            self.gump.config(state=tk.DISABLED)
        else:
            self.gump.config(state=tk.NORMAL)
        self.tocke.set(a)

    def spusti(self):
        pike=[]
        dajs=[]
        for a in self.kocke:
            if a.cup.get()== False and a.plat.get()!=0:
                pike.append(a.plat.get())
                dajs.append(a)
        p=oceni(pike)
        for k in range(len(dajs)):
            if oceni(pike[:k]+pike[k+1:]) == p:
                dajs[k].display.select()
                
        
        self.rezultat.set(self.rezultat.get() + p)
        self.tocke.set(0)
        for a in self.kocke:
            if a.cup.get():
                a.roll()
            else:
                a.plat.set(0)
                a.display.config(state=tk.DISABLED)
        self.gump.config(state=tk.DISABLED)
        if self.vseh6():
            self.nova_igra()
            self.spusti()

    def nova_igra(self):
        for a in self.kocke:
            a.display.config(state=tk.NORMAL)
            a.plat.set(0)
            a.display.select()
        self.gump.config(state=tk.NORMAL)
        

    def nova_igra_z(self):
        zadnja = []
        for a in self.kocke:
            zadnja.append(a.plat.get())
        x = oceni(zadnja)
        with open ("{0}_dice10k.txt".format(self.igralec.get()), "a",encoding="utf8") as outp:
            if x == 0:
                print("{0}! To je katastrofa!".format(self.igralec.get()),file = outp)
            else:
                print("{0} je dosegel {1} točk".format(self.igralec.get(), self.rezultat.get()+x),file=outp)
        self.rezultat.set(0)
        self.nova_igra()



    


root=tk.Tk()
root.title("10k")
igra = tabela(root)
root.mainloop
