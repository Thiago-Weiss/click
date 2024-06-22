import tkinter as tk
from tkinter import ttk

def create_menu_barra(window, set_key, set_repeat, set_mouse):
    menu_criar = tk.Menu(window)
    window.configure(menu=menu_criar)

    # cria o primeiro menu
    file_menu = tk.Menu(menu_criar, tearoff=False)
    menu_criar.add_cascade(label='File', menu=file_menu)
    # adiciona o sub menu do primeiro
    file_menu.add_command(label='Exit', command=lambda: window.destroy())

    # cria o segundo menu
    options_menu = tk.Menu(menu_criar, tearoff=False)
    menu_criar.add_cascade(label='Options', menu=options_menu)

    # cria os submenus do options
    sub_options = tk.Menu(options_menu, tearoff=False)
    sub_recording = tk.Menu(options_menu, tearoff=False)
    sub_settings = tk.Menu(options_menu, tearoff=False)
    # adiciona os submenus ao menu options
    options_menu.add_cascade(label='Clicking', menu=sub_options)
    options_menu.add_cascade(label='Multiple clicks', menu=sub_recording)
    options_menu.add_cascade(label='Settings', menu=sub_settings)

    # funçoes do sub menu 3
    sub_options.add_command(label='Options', command=lambda: set_mouse())
    # cria a configuração de tempo e repeat
    sub_options.add_command(label='Repeat', command=lambda: set_repeat())
    
    # cria ...
    sub_recording.add_command(label='Multiple clicks', command=lambda: print('Multiple clicks'))
    
    # cria a configuração de HotKey
    sub_settings.add_command(label='Hotkey', command=lambda: set_key())
    sub_settings.add_command(label='View', command=lambda: print('View'))
    sub_settings.add_command(label='Other', command=lambda: print('Other'))

    Help_menu = tk.Menu(menu_criar, tearoff=False)
    menu_criar.add_cascade(label='Help', menu=Help_menu)

    Help_menu.add_command(label='How to automate a sequence of mouse clicks and keystrokes')
    Help_menu.add_command(label='About')

    return menu_criar

