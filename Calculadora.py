import tkinter as tk
from tkinter import messagebox
import winsound

def atualizar_resposta(resultado):
    label= tk.Label(text= f"RESPOSTA: {resultado}", font=("Arial",12))
    label.grid(row=6, column=1,columnspan=2, pady=10)

def Soma():
    a= float(entry_1.get())
    b=float(entry_2.get())
    resultado= a+b
    atualizar_resposta(resultado)

def Subtracao():
    a= float(entry_1.get())
    b=float(entry_2.get())
    resultado= a-b
    atualizar_resposta(resultado)

def Multiplicacao():
    a= float(entry_1.get())
    b=float(entry_2.get())
    resultado= a*b
    atualizar_resposta(resultado)

def Divisao():
    a= float(entry_1.get())
    b=float(entry_2.get())
    if b==0:
        winsound.MessageBeep(winsound.MB_ICONHAND)
        messagebox.showinfo("ERRO","VALOR INDIVISÍVEL!")
    else:
        resultado= a/b
        atualizar_resposta(resultado)

def Sair():
    return exit()

root= tk.Tk()
root.geometry("270x260")
root.configure(bg= "lightGray")
root.title("CALCULADORA")
root.resizable(False, False)

label= tk.Label(root, text="VALOR 1:")
label.grid(row=0, column=1, padx=10, pady=10)
entry_1= tk.Entry(root)
entry_1.grid(row=0, column=2, padx=10, pady=10)

label= tk.Label(root, text="VALOR 2:")
label.grid(row=1, column=1, padx=10, pady=10)
entry_2= tk.Entry(root)
entry_2.grid(row=1, column=2, padx=10, pady=10)

btn=tk.Button(root, text="SOMA", command=lambda: Soma(),font=("Arial",8), width=14)
btn.grid(row=3, column=1, padx=10, pady=10)

btn=tk.Button(root, text="SUBTRAÇÃO", command=lambda: Subtracao(),font=("Arial",8), width=14)
btn.grid(row=4, column=1, padx=10, pady=10)

btn=tk.Button(root, text="MULTIPLICAÇÃO", command=lambda: Multiplicacao(),font=("Arial",8), width=14)
btn.grid(row=3, column=2, padx=10, pady=10)

btn=tk.Button(root, text="DIVISÃO", command=lambda: Divisao(),font=("Arial",8), width=14)
btn.grid(row=4, column=2, padx=10, pady=10)

btn=tk.Button(root, text="Sair", command=lambda: Sair(),font=("Arial",8), width=14)
btn.grid(row=5, column=1,columnspan=2, pady=10)

root.mainloop()