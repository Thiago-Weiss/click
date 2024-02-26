import tkinter as tk
from tkinter import ttk


root = tk.Tk()

# Função chamada quando o botão é clicado


def button_click():
    print("Botão clicado!")


# Configuração do botão sem contorno
button = tk.Button(root, text="Botão sem contorno",
                   borderwidth=0, command=button_click, height=0)
button.pack()


# Configuração do botão sem animação de clique
button = tk.Button(root, text="Botão sem animação",
                   relief=tk.FLAT, command=button_click)
button.pack()
tk.Button(root, text="Botão sem animação", relief='raised',
          command=button_click,  borderwidth=0).pack()


# esse
ttk.Checkbutton(root, text="Botão sem animação", command=button_click).pack()

root.mainloop()
