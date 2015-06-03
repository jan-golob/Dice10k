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
        for a in self.kocke:
            if a.cup.get():
                a.roll()


root=tk.Tk()
root.title("10k")
pregled = tabela(root)
root.mainloop
