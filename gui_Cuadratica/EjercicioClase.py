
from tkinter import *
import math


def sumar():
    b2= int(b.get()) * (-1)

    d  = ((int(b.get())) ** 2) - 4 * int(a.get()) * int(c.get())

    if d < 0:
            print("Raices imaginarias o complejas")
            t_resultados.insert(INSERT," RAICES IMAGINARIAS O COMPLEJAS")

    else:
        x1 =  (b2 + math.sqrt(d))  / (2 * int(a.get()))
        x2 =  (b2 - math.sqrt(d))  / (2 * int(a.get()))

        print("El resultado de X1 es",x1)
        print("El resultado de X2 es",x2)
        print("Dos raices Reales Diferentes")

        t_resultados.insert(INSERT," EL RESULTADO DE X1 ES" + str(x1) +  "\n EL RESULTADO DE X2 ES" + str(x2) + "\n DOS RAICES REALES DIFERENTES" + "\n") 

        if x1 == x2:
            t_resultados.insert(INSERT,"DOS RAICES REALES IGUALES" )
            print("Dos Raices Reales iguales")


def borrar():
    a.set("")
    b.set("")
    c.set("")
    t_resultados.delete("1.0","end")

def salir():
    ventana_principal.destroy()





# ------------------
# ventana principal
# ------------------

# se declara una variable llamada ventana_principal y que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Jhonatan Steven García Gómez")

# establecer tamaño a la ventana
ventana_principal.geometry("800x500")

# icono de la ventana principal
# ventana_principal.iconbitmap("colegio.ico")

# deshabilitar boton de maximar
#ventana_principal.resizable(0,0)

# color de fondo de la ventana pricipal
ventana_principal.config(bg="black")

# -------------------
# variables globales
# -------------------

a = StringVar()
b = StringVar()
b2 = 0
c = StringVar()
d = StringVar()
x1 =  0
x2 =  0


# ------------------
# frame entrada
# ------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="ivory2", width=500, height=300)
frame_entrada.place(x=10,y=60)

#
# etiqueta para valor a
etiq_a = Label(frame_entrada, text="a = ")
etiq_a.config(bg="black", fg="blue", font=("Arial", 20), anchor=CENTER)
etiq_a.place(x=40, y= 120)

# entry para el valor a
entry_a = Entry(frame_entrada, width=4, textvariable=a)
entry_a.config(font=("Arial", 20), justify=CENTER)
entry_a.focus_set()
entry_a.place(x=90,y=120)

# etiqueta para valor b
etiq_b = Label(frame_entrada, text="b = ")
etiq_b.config(bg="black", fg="blue", font=("Arial", 20), anchor=CENTER)
etiq_b.place(x=210, y= 120)

# entry para el valor b
entry_b = Entry(frame_entrada, width=4, textvariable=b)
entry_b.config(font=("Arial", 20))
entry_b.place(x=260,y=120)


# etiqueta para el valor c

etiq_a = Label(frame_entrada, text=" c =")
etiq_a.config(bg="black", fg="blue", font=("Arial", 20), anchor=CENTER)
etiq_a.place(x=375, y= 120)


# entry para el valor c

entry_a = Entry(frame_entrada, width=4, textvariable=c)
entry_a.config(font=("Arial", 20), justify=CENTER)
entry_a.focus_set()
entry_a.place(x=430,y=120)





# ------------------
# frame operaciones
# ------------------
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="ivory2", width=780, height=122)
frame_operaciones.place(x=10,y=350)

# boton para sumar los números - texto
bt_sum = PhotoImage(file="gui_1/img/boton_sumar.png")
# bt_sumar = Button(frame_operaciones, text= "Sumar", width=10)
bt_sumar = Button(frame_operaciones, image=bt_sum, width=105, height=105, command=sumar)
bt_sumar.place(x=116, y=7)

# boton para borrar entradas y resultado
bt_bor = PhotoImage(file="gui_1/img/boton_borrar.png")
# bt_borrar = Button(frame_operaciones, text="Borrar", width=10)
bt_borrar = Button(frame_operaciones, image=bt_bor, width=105, height=105, command=borrar)
bt_borrar.place(x=337, y=7)

# boton para salir - cerrar la app
bt_sal = PhotoImage(file="gui_1/img/boton_salir.png")
# bt_salir = Button(frame_operaciones, text="Salir", width=10)
bt_salir = Button(frame_operaciones, image=bt_sal, width=105, height=105, command=salir)
bt_salir.place(x=558, y=7)










# -----------------
# frame resultados
# ------------------
frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="ivory2", width=100, height=400)
frame_resultados.place(x=10,y=10)


# area de texto para resultados
t_resultados = Text(frame_resultados, width=97 , height=6)
t_resultados.config(bg="green", fg="white", font=("Courier", 10))
t_resultados.pack()



# se ejecuta el metodo mainloop() de la clase Tk() a través de la instancia ventana_principal.  Este metodo despliega una ventana simple en pantalla y queda a la espera de lo que el usuario haga (click en boton, escribir, etc).  Cada accion del usuario se conoce como un evento.  El metodo mainloop() es un bucle infinito.
ventana_principal.mainloop()


