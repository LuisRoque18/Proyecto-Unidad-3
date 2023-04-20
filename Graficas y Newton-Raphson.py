import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
from tkinter import *
import tkinter as tk
import numpy as np
import sympy as sp

root = Tk()
root.title("Newton-Raphson")
root.geometry("800x750")
fig, ax = plt.subplots()

frame = Frame(root)
titulo = Label(frame, text="Localización de raíz mediante Newton-Raphson")
titulo.config(font=("Roboto",22))
titulo.pack(padx=10, pady=10, side=TOP)

izq = Frame(frame)
izq.pack(side=LEFT)

def graficar():
    ax.clear()
    ax.grid(True)
    funcion_e = funcion.get()
    funcionE = eval('lambda x: ' + funcion_e)
    x = np.linspace(int(funcionI.get()), int(funcionF.get()))
    y = funcionE(x)
    ax.plot(x, y)
    canvas.draw()    

def raiz():
    x = sp.Symbol('x')
    f_str = funcion.get()
    f = sp.sympify(f_str)
    df = sp.diff(f, x)
    derivada_text = str(df)

    tolerancia = 1e-6
    max_iter = 100
    x0 = float(VI.get())

    for i in range(max_iter):
        derivada = df
        derivada_value = derivada.subs(x, x0)
       
        x1 = float(x0) - float(f.subs(x, x0)) / float(derivada_value)
    
        if abs(x1 - x0) < tolerancia:
            mostrar_raiz.config(text=x1)
            break
    
        x0 = x1
    plt.scatter(x1,0)

etiqueta_funcion = Label(izq, text="Función", font=("Roboto",12, "bold"))
etiqueta_funcion.pack(padx=4, pady=4)
funcion = StringVar()
entrada_funcion = Entry(izq, textvariable=funcion)
entrada_funcion.pack(padx=4, pady=4)

etiqueta_valorInicial = Label(izq, text="Valor inicial", font=("Roboto",12, "bold"))
etiqueta_valorInicial.pack(padx=4, pady=4)
funcionI = StringVar()
entrada_funcionInicial = Entry(izq, textvariable=funcionI)
entrada_funcionInicial.pack(padx=4, pady=5)

etiqueta_valorFinal = Label(izq, text="Valor final", font=("Roboto",12, "bold"))
etiqueta_valorFinal.pack(padx=4, pady=5)
funcionF = StringVar()
entrada_valorFinal = Entry(izq, textvariable=funcionF)
entrada_valorFinal.pack(padx=4, pady=6)

etiqueta_VI = Label(izq, text="Valor inicial para obtener la raíz", font=("Roboto",12, "bold"))
etiqueta_VI.pack(padx=4, pady=6)
VI = StringVar()
entrada_VI = Entry(izq, textvariable=VI)
entrada_VI.pack(padx=4, pady=7)

boton_calcular = Button(izq, text="Graficar", command=graficar)
boton_calcular.pack(padx=4, pady=8)

boton_raiz = Button(izq, text="Calcular raiz", command=raiz)
boton_raiz.pack(padx=4, pady=8)

mostrar_raiz = Label(izq, text="")
mostrar_raiz.pack(padx=4, pady=4)

ax.grid(True)
canvas = FigureCanvasTkAgg(fig, master=izq)
canvas.get_tk_widget().pack()

frame.pack()
root.mainloop()