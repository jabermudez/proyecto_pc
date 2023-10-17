import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from forms.form_master import MasterPanel

class App:

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Inicio de sesión')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana,800,500)
        

        logo = utl.leer_imagen("./imagenes/logo.png", (200,200))

        #frame_logo
        frame_logo = tk.Frame(self.ventana, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg='#009900')
        frame_logo.pack(side="left",expand=tk.NO,fill=tk.BOTH)
        label = tk.Label( frame_logo, image=logo,bg="#009900")
        label.place(x=0,y=0,relwidth=1,relheight=1)

        #frame_form
        frame_logo = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_logo.pack(side="left",expand=tk.YES,fill=tk.BOTH)

        self.ventana.mainloop()