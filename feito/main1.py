import tkinter as tk
from tkinter import ttk
import time
import win32api
import win32con
import keyboard
import pyautogui
from threading import Thread
from Hot_Key1 import *
from Menu_barra1 import *
from Repeat1 import *
from Mouse_confi1 import *


# cria a janela que configura o botão do click
config_mouse = None
def set_mouse():
    global config_mouse
    if config_mouse is not None and config_mouse.winfo_exists():
        return
    else:
        create_mouse_button(window, can_click, str_value_mouse, str_value_click, freeze_click)
        
# cria a janela que configura a hotkey
config_key = None
def set_key():
    global config_key
    if config_key is not None and config_key.winfo_exists():
        return
    else:
        create_set_key(window, can_click, Hot_key_selected)

# cria a jenala para configurar o tempo e a repetiçao
config_repeat = None
def set_repeat():
    global config_repeat
    if config_repeat is not None and config_repeat.winfo_exists():
        return
    else:
        create_set_repeat(window, hold_or_repeat, value_repeat, variables_entry_time, can_click)

# configura a jenela pricipal e cria o SubMenu
def window_config(window):
    window.title('Auto click')
    #window.iconbitmap('VS-CODE/Py/Biblioteca Tkinter/Apps/Auto click/icons/cursor.ico')
    window.geometry('230x125+800+400')
    window.minsize(230, 125)
    window.maxsize(230, 125)
    window.resizable(width=False, height=False)
    window.attributes('-topmost', True)

    window.button1 = ttk.Button(window, text=f'Press {Hot_key_selected.get().upper()} to Click', command=set_key)
    window.button1.place(relx=0.06, rely=0.1, relwidth=0.88, relheight=0.35)

    button2 = ttk.Button(window, text='Help >>', command= printar_values)
    button2.place(relx=0.06, rely=0.55, relwidth=0.88, relheight=0.35)
    
    # cria o submenu
    create_menu_barra(window, set_key, set_repeat, set_mouse)

def printar_values():
    print(Hot_key_selected.get())
    print(switch.get())
    print(can_click.get())


    # crias as variaveis do tempo e da repetição
    print(hold_or_repeat.get())
    print(value_repeat.get())
    horas = 3600 * variables_entry_time[0].get()
    minutos = 60 * variables_entry_time[1].get()
    segundos = 1 * variables_entry_time[2].get()
    miliseconds = 0.001 * variables_entry_time[3].get()

    time_between_clicks = (horas + minutos + segundos + miliseconds)
    print(time_between_clicks)
    
    # cria as variaveis do mouse
    print(str_value_mouse.get())
    print(str_value_click.get())
    print(freeze_click.get())

# macro part 1
def on_key_press(event):
    if not can_click.get():
        return
    if event.name == Hot_key_selected.get():
        switch.set(not switch.get())
        Thread(target=clicar).start()
# macro part 2
def clicar():
    horas = 3600 * variables_entry_time[0].get()
    minutos = 60 * variables_entry_time[1].get()
    segundos = 1 * variables_entry_time[2].get()
    miliseconds = 0.001 * variables_entry_time[3].get()
    time_between_clicks = (horas + minutos + segundos + miliseconds)

    if str_value_mouse.get() == 'Left':
        botao_descer = win32con.MOUSEEVENTF_LEFTDOWN
        botao_subir = win32con.MOUSEEVENTF_LEFTUP
    elif str_value_mouse.get() == 'Right':
        botao_descer = win32con.MOUSEEVENTF_RIGHTDOWN
        botao_subir = win32con.MOUSEEVENTF_RIGHTUP
    elif str_value_mouse.get() == 'Mid':
        botao_descer = win32con.MOUSEEVENTF_MIDDLEDOWN
        botao_subir = win32con.MOUSEEVENTF_MIDDLEUP

    x, y = pyautogui.position()

    if hold_or_repeat.get() == 0:
        window.button1.config(text=f'Press {Hot_key_selected.get().upper()} to Stop')
        for i in range(value_repeat.get()):
            if not switch.get():
                window.button1.config(text=f'Press {Hot_key_selected.get().upper()} to Click')
                return
            if freeze_click.get():
                win32api.SetCursorPos((x, y))
            click(botao_descer, botao_subir)
            tempo_inicial = time.time()
            while time.time() - tempo_inicial < time_between_clicks:
                pass
        switch.set(False)
        window.button1.config(text=f'Press {Hot_key_selected.get().upper()} to Click')
        return


    if hold_or_repeat.get() == 1:
        window.button1.config(text=f'Press {Hot_key_selected.get().upper()} to Stop')
        while switch.get():
            if freeze_click.get():
                win32api.SetCursorPos((x, y))
            click(botao_descer, botao_subir)
            tempo_inicial = time.time()
            while time.time() - tempo_inicial < time_between_clicks:
                if not switch.get():
                    window.button1.config(text=f'Press {Hot_key_selected.get().upper()} to Click')
                    return
        window.button1.config(text=f'Press {Hot_key_selected.get().upper()} to Click')



    if hold_or_repeat.get() == 2:
        window.button1.config(text=f'Press {Hot_key_selected.get().upper()} to Stop')
        while switch.get():
            win32api.mouse_event(botao_descer, 0, 0)
            if freeze_click.get():
                win32api.SetCursorPos((x, y))
            time.sleep(0.2)
            if not switch.get():
                win32api.mouse_event(botao_subir, 0, 0)
                window.button1.config(text=f'Press {Hot_key_selected.get().upper()} to Click')
                return
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        window.button1.config(text=f'Press {Hot_key_selected.get().upper()} to Click')

def click(botao_descer, botao_subir):
    win32api.mouse_event(botao_descer, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(botao_subir, 0, 0)



window = tk.Tk()

# cria as variaveis da key e auto click
Hot_key_selected = tk.StringVar(value= 'q')
switch = tk.BooleanVar(value= False)
can_click = tk.BooleanVar(value=True)


# crias as variaveis do tempo e da repetição
hold_or_repeat = tk.IntVar(value= 1)
value_repeat = tk.IntVar(value=1)
variables_entry_time = [tk.IntVar(value=0), tk.IntVar(value=0), tk.IntVar(value=0), tk.IntVar(value=0)]

# cria as variaveis do mouse
str_value_mouse = tk.StringVar(value= 'Left')
str_value_click = tk.StringVar(value= 'Single')
freeze_click = tk.BooleanVar(value= True)

# cria a jenela pricipal e o SubMenu
window_config(window)

keyboard.on_press(on_key_press)

window.mainloop()

