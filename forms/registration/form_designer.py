import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
import util.generic as utl

class FormRegisterDesigner:

    def register():
        pass

    def __init__(self):
        self.ventana = tk.Toplevel()
        self.ventana.title('Inicio de sesión')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana,600,450)
        

        logo = utl.leer_imagen("./imagenes/logo.png", (200,200))

        #frame_logo
        frame_logo = tk.Frame(self.ventana, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg='#009900')
        frame_logo.pack(side="left",expand=tk.NO,fill=tk.BOTH)
        label = tk.Label( frame_logo, image=logo,bg="#009900")
        label.place(x=0,y=0,relwidth=1,relheight=1)

        #frame_form
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="left",expand=tk.YES,fill=tk.BOTH)
        #end frame_form

        #frame_form_top
        frame_form_top = tk.Frame(frame_form,height=50, bd=0, relief=tk.SOLID,bg='black')
        frame_form_top.pack(side="top",fill=tk.X)
        title = tk.Label(frame_form_top, text="Registro de Usuario",font=('Arial',30),fg="#666a88",bg="#fcfcfc",pady=50)
        title.pack(expand=tk.YES,fill=tk.BOTH)
        #end frame_form_top

        #frame_form_fill
        frame_form_fill = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID,bg='#fcfcfc')
        frame_form_fill.pack(side='bottom',expand=tk.YES,fill=tk.BOTH)

        etiqueta_usuario = tk.Label(frame_form_fill, text="Usuario", font=('Arial',14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=20, pady=5)
        self.usuario = ttk.Entry(frame_form_fill, font=('Arial',14))
        self.usuario.pack(fill=tk.X, padx=20,pady=10)

        etiqueta_password = tk.Label(frame_form_fill, text="Contraseña", font=('Arial',14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_password.pack(fill=tk.X, padx=20, pady=5)
        self.password = ttk.Entry(frame_form_fill, font=('Arial',14))
        self.password.pack(fill=tk.X, padx=20,pady=10)
        self.password.config(show="*")

        etiqueta_confirmation = tk.Label(frame_form_fill, text="Confirmaciòn", font=('Arial',14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_confirmation.pack(fill=tk.X, padx=20, pady=5)
        self.confirmation = ttk.Entry(frame_form_fill, font=('Arial',14))
        self.confirmation.pack(fill=tk.X, padx=20,pady=10)
        self.confirmation.config(show="*")


        

        register = tk.Button(frame_form_fill, text="Registrar", font=('Arial', 15), bg='#fcfcfc', bd=0, fg="#009900", command=self.register)
        register.pack(fill=tk.X, padx=20, pady=20)
        register.bind("<Return>", (lambda event: self.register()))


        #end frame_form_fill
        self.ventana.mainloop()



