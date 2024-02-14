import tkinter as tk
from tkinter import ttk
import keyboard
from threading import Thread


def create_set_key(window, can_click, Hot_key_selected):
    global config_key
    preview_key = tk.StringVar(value= Hot_key_selected.get())
    config_key = tk.Toplevel()

    # desabilita o auto click e a janela principal
    can_click.set(False)
    window.attributes('-disable', True)
    # configura essa janela
    config_key.title('Hotkey')
    pos_x = window.winfo_x()
    pos_y = window.winfo_y()
    config_key.geometry(f'230x110+{pos_x + 150}+{pos_y + 20}')
    config_key.minsize(230, 110)
    config_key.maxsize(230, 110)
    config_key.resizable(width=False, height=False)
    config_key.attributes('-topmost', True)

    # cria os widgets
    widgets(config_key, window, can_click, preview_key, Hot_key_selected)
    # fecha a janela
    config_key.protocol('WM_DELETE_WINDOW', lambda: fechar_janela(window, can_click, preview_key, Hot_key_selected))

# fecha a janela quando apertado o X sem salvar as modificaçoes
def fechar_janela(window, can_click, preview_key, Hot_key_selected):
    config_key.button_setar.config(state='normal')
    config_key.button_ok.config(state='normal')
    config_key.button_cancel.config(state='normal')
    preview_key.set(Hot_key_selected.get())
    # reabilita o auto click e janela pricipal
    can_click.set(True)
    window.attributes('-disable', False)
    config_key.destroy()

# cria os widgets e os posiciona
def widgets(root, window, can_click, preview_key, Hot_key_selected):
    config_key.button_setar = ttk.Button(
        root, text='Click / Stop', command=lambda: setar_botao(preview_key))
    config_key.entry_key = ttk.Entry(
        root, textvariable=preview_key, state='readonly', justify='center', font=('Ariel', 15))
    config_key.button_ok = ttk.Button(root, text='Ok', command=lambda: ok_selected(
        window, can_click, preview_key, Hot_key_selected))
    config_key.button_cancel = ttk.Button(
        root, text='Cancel', command=lambda: cancel_selected(can_click, window, preview_key, Hot_key_selected))

    config_key.button_setar.place(
        relx=0.05, rely=0.15, relwidth=0.425, relheight=0.3)
    config_key.entry_key.place(
        relx=0.55, rely=0.16, relwidth=0.42, relheight=0.28)
    config_key.button_ok.place(
        relx=0.15, rely=0.55, relwidth=0.325, relheight=0.25)
    config_key.button_cancel.place(
        relx=0.55, rely=0.55, relwidth=0.3, relheight=0.25)

# configura a hotkey part 1
def setar_botao(preview_key):
    preview_key.set(value='Press Key')
    config_key.button_setar.config(state='disabled')
    config_key.button_ok.config(state='disabled')
    config_key.button_cancel.config(state='disabled')
    hotkey_thread = Thread(target=lambda: hot_key(preview_key))
    hotkey_thread.daemon = True
    hotkey_thread.start()

# configura a hotkey part 2
def hot_key(preview_key):
    hotkey = keyboard.read_key()
    preview_key.set(hotkey)
    config_key.button_setar.config(state='normal')
    config_key.button_ok.config(state='normal')
    config_key.button_cancel.config(state='normal')

# fecha a janela e salvas as modificaçoes
def ok_selected(window, can_click, preview_key, Hot_key_selected):
    Hot_key_selected.set(preview_key.get())
    window.button1.config(text=f'Press {Hot_key_selected.get().upper()} to Click')
    # reabilita o auto click e a janela pricipal
    can_click.set(True)
    window.attributes('-disable', False)
    config_key.destroy()

# fecha a janela sem salvar as modificaçoes
def cancel_selected(can_click, window, preview_key, Hot_key_selected):
    # reabilita o auto click e a janela pricipal
    preview_key.set(Hot_key_selected.get())
    can_click.set(True)
    window.attributes('-disable', False)
    config_key.destroy()

