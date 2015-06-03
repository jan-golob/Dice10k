import tkinter as tk
import random

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
##        self.pikice = tk.Canvas(self.frame, width=300, height=300)
##        self.pikice.grid(row = 0, column = 0)
        self.roller = tk.Button(self.frame, text="MEČI?", command = self.loncek)
        self.roller.grid(row = 1, column = 0)

        self.da = tk.Label(self.frame, textvariable = str(self.cup))
        self.da.grid(row=2, column=0)
      
        
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
            dice.frame.grid(row=0,column=a)
            self.kocke.append(dice)

        self.gump = tk.Button(master, text="Vrzi vse", command = self.spusti)
        self.gump.grid(row = 0, column =6)
##        dice1 = kocka(master)
##        dice1.frame.grid(row = 0, column = 0)

    def spusti(self):
        for a in self.kocke:
            if a.cup.get():
                a.roll()


root=tk.Tk()
pregled = tabela(root)
root.mainloop
