import tkinter as tk
from tkinter import ttk
import webbrowser
# meu
from master_top_level import MensagemBox_entry




class Menu_config():
    def __init__(self, app):
        self.app = app



    def create_menu(self):
        # cria o menu principal
        self.prefs_menu = tk.Menu(self.app, tearoff=False)


        # ///// PRIMEIRA SESAO /////
        # lista de labels
        text_list = ["Play Speed: ½",
                    "Play Speed: 1x",
                    "Play Speed: 2x",
                    "Play Speed: 100x",
                    f"Play Custom Speed:  {self.app.custom_speed.get()}x"]

        # cria os botoes usando uma funçao
        for index, text in enumerate(text_list):
            self.multi_checkbutton(self.prefs_menu, text, self.app.speed, index + 1)

        # adiciona o ultimo botao da primeira sesao o botao que cria outra janela de config
        self.prefs_menu.add_command(label="Set Custom Speed", command=set_speed)

        # linha que separa as seçoes
        self.prefs_menu.add_separator()

        # ///// SEGUNDA SESAO /////
        self.checkbutton(self.prefs_menu, "Continuous Playback", self.app.infinite_repeat, True)
        self.prefs_menu.add_command(label="Set Playback Loops... (XXXX)", command=set_repeat)

        # linha que separa as seçoes
        self.prefs_menu.add_separator()

        # ///// TERCEIRA SESAO /////
        # cria o submenu e adiciona ele ao menu pricipal
        rec_menu = tk.Menu(self.prefs_menu, tearoff=False)
        self.prefs_menu.add_cascade(label="Recording Hotkey", menu=rec_menu)

        # lista de labels
        text_list = ["Control + Shift + Alt + R",
                    "Print Screen",
                    "F8",
                    "F12"]
        # cria os botoes usando uma funçao
        for index, text in enumerate(text_list):
            self.multi_checkbutton(rec_menu, text, self.app.rec_key, index + 1)



        # cria o submenu e adiciona ele ao menu pricipal
        play_menu = tk.Menu(self.prefs_menu, tearoff=False)
        self.prefs_menu.add_cascade(label="Recording Hotkey", menu=play_menu)

        # lista de labels
        text_list = ["Control + Shift + Alt + P",
                    "Print Screen",
                    "F8",
                    "F12"]
        # cria os botoes usando uma funçao
        for index, text in enumerate(text_list):
            self.multi_checkbutton(play_menu, text, self.app.play_key, index + 1)

        play_menu.add_separator()
        play_menu.add_command(label="• Hint: Press {PAUSE} or {ScrollLock} to stop playbacks", state='disabled', activebackground='#d3d3d3')


        # linha que separa as seçoes
        self.prefs_menu.add_separator()

        # ///// TERCEIRA SESAO /////

        self.checkbutton(self.prefs_menu, "Always on Top", self.app.topmost_bool, True)
        self.checkbutton(self.prefs_menu, "Show Captions", self.app.show_text_bool, True)

        self.prefs_menu.add_command(label="Use Custom Toolbar...")
        
        self.multi_checkbutton(self.prefs_menu, "Use Default Toolbar", tk.BooleanVar(value= True), True)


        self.prefs_menu.add_separator()



        self.prefs_menu.add_command(label="TinyTask Website", command= lambda: webbrowser.open("https://www.youtube.com/@TimelapseCoderYT/videos"))
        self.prefs_menu.add_command(label="About TinyTask 1.77")



    def teste (self, var, on_value, func):
        var.set(value = on_value)
        if func:
            func()

    def multi_checkbutton(self, master, label, variable, on_value, func = None):
        master.add_checkbutton(label=label, variable=variable, command = lambda: self.teste(variable, on_value, func), onvalue=on_value, selectcolor='blue', activebackground='#91C9F7', activeforeground="black")

    def checkbutton(self, master, label, variable, on_value, func = None):
        master.add_checkbutton(label=label, variable=variable, command= func, onvalue=on_value, selectcolor='blue', activebackground='#91C9F7', activeforeground="black")



def show_submenu(self):
    # mostra o submenu
    self.prefs_menu.tk_popup(1000, 500)


def set_speed(self):
    MensagemBox_entry(self.app, self.app.janel_aberta, 'Set Custom Speed', "Playback speed multiplier (1-100):", 284, 155, False)


def set_repeat(self):
    MensagemBox_entry(self.app, self.app.janel_aberta, 'Set Playback Loops', 'Set the number of playback loops:', 284, 155, False)
