import tkinter as tk
from tkinter import ttk
import webbrowser
# meu
from master_top_level import MensagemBox_entry


class Menu_config(tk.Menu):
    def __init__(self, app):
        super().__init__(master=app,  tearoff=False)
        self.app = app

        self.create_menu()

    def create_menu(self):

        # funçao usanda pra imperdir que o checkbox seja desmarcado
        # e para adicionar a funçao passada para o botao
        def teste(var, on_value, func):
            var.set(value=on_value)
            if func:
                func()

        # funcao para criar muiltiplos checkbox com a mesma varavel e impedir manter sempre um ativo
        def multi_checkbutton(master, label, variable, on_value, func=None):
            master.add_checkbutton(label=label, variable=variable, command=lambda: teste(variable, on_value, func), onvalue=on_value, selectcolor='blue', activebackground='#91C9F7', activeforeground="black")

        # funçao que cria um checkbox e esse pode ficar ativo ou desativado
        def checkbutton(master, label, variable, on_value, func=None):
            master.add_checkbutton(label=label, variable=variable, command=func, onvalue=on_value, selectcolor='blue', activebackground='#91C9F7', activeforeground="black")

        def commandbutton(master, label, func):
            master.add_command(label=label, command=func, activebackground='#91C9F7', activeforeground="black")

        # funçao que cria uma outra janela para configura o speed

        def set_speed():
            MensagemBox_entry(self.app, self.app.janela_aberta, 'Set Custom Speed',"Playback speed multiplier (1-100):", 284, 155, self.app.custom_speed, value_max=1000)

        # funçao que cria uma outra janela para configura o repeat

        def set_repeat():
            MensagemBox_entry(self.app, self.app.janela_aberta, 'Set Playback Loops',
                              'Set the number of playback loops:', 284, 155, self.app.repeat)

        # ////////////////////////////////////////// PRIMEIRA SESAO //////////////////////////////////////////
        # lista de labels
        text_list = ["Play Speed: ½",
                     "Play Speed: 1x",
                     "Play Speed: 2x",
                     "Play Speed: 100x",
                     f"Play Custom Speed:  {self.app.custom_speed.get()}x"]
        # cria os botoes usando a funçao
        for index, text in enumerate(text_list):
            multi_checkbutton(self, text, self.app.speed, index + 1)
        # adiciona o ultimo botao da primeira sesao o botao que cria outra janela de config
        commandbutton(self, f"Set Custom Speed", set_speed)

        # linha que separa as seçoes -------------------------------------
        self.add_separator()
        # ////////////////////////////////////////// SEGUNDA SESAO //////////////////////////////////////////
        checkbutton(self, "Continuous Playback",self.app.infinite_repeat, True)
        commandbutton(self, f"Set Playback Loops... ({self.app.repeat.get()})", set_repeat)



        # linha que separa as seçoes -------------------------------------
        self.add_separator()

        # ////////////////////////////////////////// TERCEIRA SESAO //////////////////////////////////////////
        # cria o submenu e adiciona ele ao menu pricipal
        rec_menu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="Recording Hotkey", menu=rec_menu, activebackground='#91C9F7', activeforeground="black")

        # lista de labels
        text_list = ["Control + Shift + Alt + R",
                     "Print Screen",
                     "F8",
                     "F12"]
        # cria os botoes usando uma funçao
        for index, text in enumerate(text_list):
            multi_checkbutton(rec_menu, text, self.app.rec_key, index + 1, lambda: print("verificar a key"))

        # ////////////////////////////////////////// TERCEIRA SESAO //////////////////////////////////////////
        # cria o submenu e adiciona ele ao menu pricipal
        play_menu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="Recording Hotkey", menu=play_menu, activebackground='#91C9F7', activeforeground="black")

        # lista de labels
        text_list = ["Control + Shift + Alt + P",
                     "Print Screen",
                     "F8",
                     "F12"]
        # cria os botoes usando uma funçao
        for index, text in enumerate(text_list):
            multi_checkbutton(play_menu, text, self.app.play_key, index + 1, lambda: print("verificar a key"))
        # coloca os itens finals desse submenu
        play_menu.add_separator()
        play_menu.add_command(label="• Hint: Press {PAUSE} or {ScrollLock} to stop playbacks", state='disabled', activebackground='#d3d3d3')

        # linha que separa as seçoes -------------------------------------
        self.add_separator()

        # ////////////////////////////////////////// QUARTA SESAO //////////////////////////////////////////
        checkbutton(self, "Always on Top", self.app.topmost_bool, True)
        checkbutton(self, "Show Captions", self.app.show_text_bool, True)
        commandbutton(self, "Use Custom Toolbar...",lambda: print("Use Custom Toolbar..."))
        multi_checkbutton(self, "Use Default Toolbar",tk.BooleanVar(value=True), True)

        # linha que separa as seçoes -------------------------------------
        self.add_separator()

        # ////////////////////////////////////////// QUINTA SESAO //////////////////////////////////////////
        commandbutton(self, "TinyTask Website", lambda: webbrowser.open("https://www.youtube.com/@TimelapseCoderYT/videos"))
        commandbutton(self, "About TinyTask 1.77",lambda: print("fazer a janela ainda"))

    def show_submenu(self, x, y):
        # mostra o submenu
        self.tk_popup(x, y)
