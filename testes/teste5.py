import tkinter as tk
from tkinter import ttk
import webbrowser
# meu
from master_top_level import MensagemBox_entry


def show_submenu():
    # mostra o submenu
    prefs_menu.tk_popup(file_button.winfo_rootx() + file_button.winfo_width(), file_button.winfo_rooty())


def set_speed():
    window_speed = MensagemBox_entry(root, janela_aberta, 'Set Custom Speed', "Playback speed multiplier (1-100):", 284, 155, False)


def set_repeat():
    window_speed = MensagemBox_entry(root, janela_aberta, 'Set Playback Loops', 'Set the number of playback loops:', 284, 155, False)


root = tk.Tk()




root.geometry("500x100+1000+400")


# ///// DATA /////
janela_aberta = tk.BooleanVar(value=False)

# speed
speed = tk.IntVar(value=2)
custom_speed = tk.IntVar(value=20)

# repeat
infinite_repeat = tk.BooleanVar(value= False)
repeat = tk.IntVar(value= 1)

# rec/play hotkey config
rec_key = tk.IntVar(value=1)
play_key = tk.IntVar(value=1)

# topmost , ficar em cima dos outros apps
topmost_bool = tk.BooleanVar(value= False)

# mostrar texto
show_text_bool = tk.BooleanVar(value= True)


# variavel que está sempre ativa
var_bool_treu = tk.BooleanVar(value= True)




def teste (var, on_value, func):
    var.set(value = on_value)
    if func:
        func()

def multi_checkbutton(master, label, variable, on_value, func = None):
    master.add_checkbutton(label=label, variable=variable, command = lambda: teste(variable, on_value, func), onvalue=on_value, selectcolor='blue', activebackground='#91C9F7', activeforeground="black")

def checkbutton(master, label, variable, on_value, func = None):
    master.add_checkbutton(label=label, variable=variable, command= func, onvalue=on_value, selectcolor='blue', activebackground='#91C9F7', activeforeground="black")

# cria o menu principal
prefs_menu = tk.Menu(root, tearoff=False)



# Cria um botão que mostra o submenu quando clicado
file_button = ttk.Button(root, text="New", command=show_submenu)
file_button.pack()


root.mainloop()
