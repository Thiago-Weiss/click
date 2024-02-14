import tkinter as tk
from tkinter import ttk

def create_mouse_button(window, can_click, str_value_mouse, str_value_click, freeze_click):
    global config_mouse
    config_mouse = tk.Toplevel()
    local_str_value_click = tk.StringVar(value= str_value_click.get())
    local_str_value_mouse = tk.StringVar(value= str_value_mouse.get())
    local_freeze_click = tk.BooleanVar(value= freeze_click.get())
    
    can_click.set(False)
    window.attributes('-disable', True)
    
    pos_x = window.winfo_x()
    pos_y = window.winfo_y()
    config_mouse.geometry(f'274x184+{pos_x + 150}+{pos_y + 20}')
    
    config_mouse.minsize(274,184)
    config_mouse.maxsize(274,184)
    config_mouse.resizable(width=False, height=False)
    config_mouse.attributes('-topmost', True)

    widgets(config_mouse, window, can_click, local_freeze_click, local_str_value_click, local_str_value_mouse, str_value_mouse, str_value_click, freeze_click)
    # fecha a janela
    config_mouse.protocol('WM_DELETE_WINDOW', lambda: fechar_janela(window, can_click))

# fecha a janela quando apertado o X sem salvar as modificaçoes
def fechar_janela(window, can_click):
    # reabilita o auto click e janela pricipal
    can_click.set(True)
    window.attributes('-disable', False)
    config_mouse.destroy()
      
def widgets(config_mouse, window, can_click, local_freeze_click, local_str_value_click, local_str_value_mouse, str_value_mouse, str_value_click, freeze_click):
    config_mouse.rowconfigure((0,1,2,3,4), weight= 1, uniform= 'a')
    config_mouse.columnconfigure((0,1,2,3), weight = 1, uniform= 'a')

    # 1 linha
    values_mouse = ['Left', 'Right', 'Mid']
    ttk.Label(config_mouse, text='Mouse:').grid(row= 0, column= 0, sticky= 'nswe', padx= 10)
    ttk.Combobox(config_mouse, values= values_mouse, textvariable= local_str_value_mouse, state= 'readonly', width=10, justify= 'left', font=('Ariel', 9)).grid(row= 0, column= 1, columnspan=2, sticky='w')
    # 2 linha
    values_click = ['Single', 'Double']
    ttk.Label(config_mouse, text='Click:').grid(row= 1, column= 0, sticky= 'nswe', padx= 10)
    ttk.Combobox(config_mouse, values= values_click, textvariable= local_str_value_click, state= 'readonly', width= 10, justify= 'left', font=('Ariel', 9)).grid(row= 1, column= 1, columnspan=2, sticky='w')
    # 3 linha
    ttk.Checkbutton(config_mouse, text='Frezze the pointer (only single click)', variable= local_freeze_click).grid(row= 2, column= 0, columnspan= 4, sticky= 'w', padx= 10)
    # 4 linha
    frame = ttk.Frame(config_mouse)
    frame.grid(row=3, column=0, rowspan= 2, columnspan= 4, sticky= 'nswe')
    ttk.Button(frame, text='Ok', command= lambda: ok_selected(config_mouse, window, can_click, local_freeze_click, local_str_value_click, local_str_value_mouse, str_value_mouse, str_value_click, freeze_click)).pack(side='left', expand=True, anchor='e', padx= 20, ipady= 2)
    ttk.Button(frame, text='Cancel', command= lambda: fechar_janela(window, can_click)).pack(side='left', expand=True, anchor='w', padx= 20, ipady= 2)

    
def ok_selected(config_mouse, window, can_click, local_freeze_click, local_str_value_click, local_str_value_mouse, str_value_mouse, str_value_click, freeze_click):
    str_value_mouse.set(local_str_value_mouse.get())
    str_value_click.set(local_str_value_click.get())
    freeze_click.set(local_freeze_click.get())
    can_click.set(True)
    window.attributes('-disable', False)
    config_mouse.destroy()

