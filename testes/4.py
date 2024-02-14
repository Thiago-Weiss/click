import tkinter as tk
from tkinter import ttk

def mudar_texto():
    label['text'] = 'Texto Alterado'

root = tk.Tk()
root.geometry('400x300')
root.title('Exemplo de Botões e Texto')

style = ttk.Style()

# Criação do tema
style.theme_create("tema_padrao", parent="alt", settings={
    "vermelho.TButton": {
        "configure": {"foreground": "red", "background": "yellow"},
        "map": {"foreground": [("pressed", "green"), ("active", "blue")]}
    },
    "azul.TButton": {
        "configure": {"foreground": "#964BA0", "background": "#fabaa9"},
        "map": {"foreground": [("pressed", "green"), ("active", "blue")]}
    },
    "TLabel": {
        "configure": {"foreground": "green", "background": "black"},
        "map": {"foreground": [("pressed", "white"), ("active", "white")]}
    }
})

style.theme_use("tema_padrao")

# Botão 1 com o estilo 1
btn1 = ttk.Button(root, text='Botão 1', style= 'vermelho.TButton')
btn1.pack(pady=10)

# Botão 2 com o estilo 2
btn2 = ttk.Button(root, text='Botão 2', command=mudar_texto, style='azul.TButton')
btn2.pack(pady=10)

# Texto com estilo
label = ttk.Label(root, text='Texto Original')
label.pack(pady=20)

root.mainloop()
