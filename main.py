import tkinter as tk
import tkinter.font as font

class Fullscreen_Example:
    def __init__(self):
        self.window = tk.Tk()
        self.window.attributes('-fullscreen', True)  
        self.fullScreenState = False
        self.window.bind("<F11>", self.toggleFullScreen)
        self.window.bind("<Escape>", self.quitFullScreen)

        #l = tk.LabelFrame(self.window, text="Titre de la frame", padx=0, pady=0)
        #l.pack(fill="both", expand="yes")

        f = font.Font(family='Calibri', size=35, weight="bold")
        f2 = font.Font(family='Calibri', size=35)

        photo = tk.PhotoImage(file="Logo_Staps.png")
        label = tk.Label(self.window, text="Enregistrement Tennis")
        label["font"]=f

        canvas = tk.Canvas(self.window, width=200, height=200)
        canvas.create_image(0, 0, image=photo, anchor=tk.NW)
        label.pack(anchor=tk.N)
        canvas.pack(side=tk.TOP, anchor=tk.NW)
        canvas.place(x=0,y=0)



        quitter = tk.Button(self.window, text="Fermer", command=self.window.quit, bg="lightgrey")
        quitter['font']= f
        quitter.pack(padx=5, pady=5)

        enregistrer = tk.Button(self.window, text="Commencer l'enregistrement", padx=20, pady=20, bg="lightgrey")
        enregistrer["font"]= f2
        enregistrer.pack(padx=20, pady=20)

        liste = tk.Listbox(self.window)
        liste.insert(1, "USB 1")
        liste.insert(2, "USB 2")
        liste.pack(side=tk.RIGHT)

        print(tk.font.families())

        #court1 = tk.Button(self.window, text="Court 1", padx=20, pady=20, bg="lightgrey").place(x=150,y=500)
        #court2 = tk.Button(self.window, text="Court 2", padx=20, pady=20, bg="lightgrey").place(x=300,y=500)
        #court3 = tk.Button(self.window, text="Court 3", padx=20, pady=20, bg="lightgrey").place(x=450,y=500)

        value = tk.StringVar()
        court1 = tk.Radiobutton(self.window, text="Court 1", variable=value, value=1, indicatoron=0, bg="lightgrey",padx=20, pady=20)
        court2 = tk.Radiobutton(self.window, text="Court 2", variable=value, value=2, indicatoron=0, bg="lightgrey",padx=20, pady=20)
        court3 = tk.Radiobutton(self.window, text="Court 3", variable=value, value=3, indicatoron=0, bg="lightgrey",padx=20, pady=20)

        court1.invoke()

        court1.place(x=150,y=500)
        court2.place(x=300, y=500)
        court3.place(x=450, y=500)

        #bouton1.pack()
        #bouton2.pack()
        #bouton3.pack()

        #court1.grid(column=0, row=0)
        #court2.grid(column=1, row=0)
        #court3.grid(column=2, row=0)

        ##court1.pack(side=tk.LEFT,padx=20, pady=20)
        ##court2.pack(side=tk.LEFT,padx=20, pady=20)
        ##court3.pack(side=tk.LEFT,padx=20, pady=20)



        self.window.mainloop()

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.window.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)

if __name__ == '__main__':
    app = Fullscreen_Example()  
