import tkinter as tk
from tkinter import ttk

def create_set_repeat(window, hold_or_repeat, value_repeat, variables_entry_time, can_click):
    global config_repeat
    
    local_hold_or_repeat = tk.IntVar(value= hold_or_repeat.get())
    local_value_repeat = tk.IntVar(value= value_repeat.get())
    local_variables_entry_time = [tk.IntVar(value= variables_entry_time[0].get()), tk.IntVar(value= variables_entry_time[1].get()), tk.IntVar(value= variables_entry_time[2].get()), tk.IntVar(value= variables_entry_time[3].get())]
   
    config_repeat = tk.Toplevel()

    # desabilita o auto click e a janela principal
    can_click.set(False)
    window.attributes('-disable', True)
    # configura essa janela
    
    config_repeat.title('Clicking repeat')
    pos_x = window.winfo_x()
    pos_y = window.winfo_y()
    config_repeat.geometry(f'402x265+{pos_x + 150}+{pos_y + 20}')
    config_repeat.minsize(402,265)
    config_repeat.maxsize(402,265)
    config_repeat.resizable(width=False, height=False)
    config_repeat.attributes('-topmost', True)
    
    # cria os widgets
    widgets(config_repeat, window, local_hold_or_repeat, local_value_repeat, local_variables_entry_time, hold_or_repeat, value_repeat, variables_entry_time, can_click)
    # fecha a janela
    config_repeat.protocol('WM_DELETE_WINDOW', lambda: fechar_janela(window, can_click))

# fecha a janela quando apertado o X sem salvar as modificaçoes
def fechar_janela(window, can_click):
    # reabilita o auto click e janela pricipal
    can_click.set(True)
    window.attributes('-disable', False)
    config_repeat.destroy()

# cria os widgets e os posiciona
def widgets(config_repeat, window, local_hold_or_repeat, local_value_repeat, local_variables_entry_time, hold_or_repeat, value_repeat, variables_entry_time, can_click):
    # cria frames
    frame_top = ttk.Frame(config_repeat, borderwidth=2, relief="groove")
    frame_top_1 = ttk.Frame(frame_top)
    frame_top_2 = ttk.Frame(frame_top)
    frame_top_3 = ttk.Frame(frame_top)
    frame_botton = ttk.Frame(config_repeat, borderwidth=2, relief="groove")
    frame_botton_1 = ttk.Frame(frame_botton)
    frame_botton_2 = ttk.Frame(frame_botton)
    # posiciona frames
    frame_top.place(x= 6, y= 6, relwidth= 0.97, relheight= 0.5)
    frame_top_1.pack(fill='x', padx= 10, pady= 15)
    frame_top_2.pack(fill='x', padx= 10)
    frame_top_3.pack(fill='x', padx= 10, pady= 15)
    frame_botton.place(x= 6, rely= 0.5, relwidth= 0.97, relheight= 0.47)
    frame_botton_1.pack(expand=True, fill='x', pady= 15)
    frame_botton_2.pack(expand=True, fill='x')

    # cria widgets e posiciona
    # parte de cima 1 linha
    ttk.Radiobutton(frame_top_1, text='Repeat  ', variable=local_hold_or_repeat, value= 0).pack(side='left', anchor='w')
    spinbox_repeat = ttk.Spinbox(frame_top_1, width=6, from_=1, to=999999, textvariable=local_value_repeat, justify='center', font=('Ariel', 9), validate="key", validatecommand=(window.register(validate_repeat), "%P"))
    spinbox_repeat.pack(side='left', anchor='w')
    ttk.Label(frame_top_1, text='  Times').pack(side='left', anchor='w')
    # 2 linha
    ttk.Radiobutton(frame_top_2, text='Repeat until stopped', variable=local_hold_or_repeat, value= 1).pack(fill='x', anchor='w')
    # 3 linha
    ttk.Radiobutton(frame_top_3, text='Hold button', variable=local_hold_or_repeat, value= 2).pack(fill='x', anchor='w')
    
    # parte de baixo 4 linha
    ttk.Label(frame_botton_1, text='Interval:      ').pack(side='left', anchor='w')
    text_label_time = ['hours   ', 'mins   ', 'secs   ', 'miliseconds   ']
    dict_entry= []
    for tt, vv in zip(text_label_time, local_variables_entry_time):
        entry = ttk.Entry(frame_botton_1, width=4, justify='right', font=('Ariel', 9), textvariable=vv, validate="key", validatecommand=(window.register(validate_time), "%P"))
        entry.pack(side='left', anchor='w')
        dict_entry.append(entry)
        ttk.Label(frame_botton_1, text= tt).pack(side='left', anchor='w')
    # 5 linha essa variavel local_value_repeat n precisa ser passada mas ela está de bira e local_variables_entry_time tambem
    ttk.Button(frame_botton_2, text='Ok', command= lambda: ok_selected(local_hold_or_repeat, local_value_repeat, local_variables_entry_time, hold_or_repeat, value_repeat, variables_entry_time, window, can_click, spinbox_repeat, dict_entry)).pack(side='left', expand=True, anchor='e', padx= 20, ipady= 2)
    ttk.Button(frame_botton_2, text='Cancel', command= lambda: fechar_janela(window, can_click)).pack(side='left', expand=True, anchor='w', padx= 20, ipady= 2)

# valida o entry do repeat
def validate_repeat(text):
    if len(text) >= 7:
        return False
    if text.isnumeric() and (int(text) == 0 or int(text) <= 999999):
        return True
    else:
        return False

# valida o entry time
def validate_time(text):
    if len(text) >= 5:
        return False
    if text.isnumeric() and (int(text) == 0 or int(text) <= 999):
        return True
    else:
        return False

def ok_selected(local_hold_or_repeat, local_value_repeat, local_variables_entry_time, hold_or_repeat, value_repeat, variables_entry_time, window, can_click, spinbox_repeat, dict_entry):
    hold_or_repeat.set(local_hold_or_repeat.get())
    value_repeat.set(value= validar_numero(spinbox_repeat.get()))
    variables_entry_time[0].set(value= validar_numero(dict_entry[0].get()))
    variables_entry_time[1].set(value= validar_numero(dict_entry[1].get()))
    variables_entry_time[2].set(value= validar_numero(dict_entry[2].get()))
    variables_entry_time[3].set(value= validar_numero(dict_entry[3].get()))
    # reabilita o auto click e janela pricipal
    can_click.set(True)
    window.attributes('-disable', False)
    config_repeat.destroy()

def validar_numero(nume):
    numero = int(nume)
    if numero == 0:
        return 0
    numero = int(nume.lstrip('0'))
    return numero