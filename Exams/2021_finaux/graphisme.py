import tkinter as tk
import random as rd
class AppliCanevas(tk.Tk):
    def __init__(self):
        self.__nb_cercles = 0
        self.__nb_lignes = 0
        tk.Tk.__init__(self)
        self.size = 500
        geometrie = f"{600}x{700}"
        self.geometry(geometrie)
        self.creer_widgets()


    def creer_widgets(self):
        self.canv = tk.Canvas(self, bg="light blue", width=self.size, height=self.size)
        self.canv.grid(row=0, rowspan=2, columnspan = 2, column=0)
        self.bouton_cercles = tk.Button(self, text="Cercles", command=self.dessine_cercles)
        self.bouton_cercles.grid(row=0, column=2)
        self.bouton_lignes = tk.Button(self, text="Lignes", command=self.dessine_lignes)
        self.bouton_lignes.grid(row=1, column=2)

        self.label_cercles = tk.Label(self, text=f"{self.__nb_cercles} cercles", bg="light blue")
        self.label_cercles.grid(row=2, column=0)
        self.label_lignes = tk.Label(self, text=f"{self.__nb_lignes} lignes", bg="light blue")
        self.label_lignes.grid(row=2, column=1)
        self.bouton_quitter = tk.Button(self, text = "Quitter", command = self.quit)
        self.bouton_quitter.grid(row=2, column=2)

    def rd_couleurs(self):
        return rd.choice(["black","yellow",'magenta','cyan','white','purple', "red", "green", "blue"])



    def dessine_cercles(self):
        n = rd.randint(1,10)
        self.__nb_cercles += n
        self.label_cercles.config(text=f"{self.__nb_cercles} cercles")
        for i in range(n):
            x,y  = (rd.randint(1,self.size) for j in range (2))
            diameter = rd.randint(1,50)
            self.canv.create_oval(x,y,x+diameter, y+diameter, fill=self.rd_couleurs())


    def dessine_lignes(self):
        n = rd.randint(1,10)
        self.__nb_lignes += n
        self.label_lignes.config(text=f"{self.__nb_lignes} lignes")
        for i in range(n):
            x,y,x2,y2 = (rd.randint(1,self.size) for j in range (4))
            self.canv.create_line(x,y,x2,y2,fill=self.rd_couleurs())


if __name__ == "__main__":
    app = AppliCanevas()
    app.title("Finalm INF2 2021")
    app.mainloop()