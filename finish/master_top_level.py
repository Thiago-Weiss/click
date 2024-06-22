import tkinter as tk
from random import randrange
# meu
from widgets_tools import get_color_hex_windows





class Top_level_master(tk.Toplevel):
    def __init__(self, parent, janela_aberta, windows_name, largura, altura):
        super().__init__(master=parent)

        # se tentar fechar a jenala de outra forma
        self.protocol("WM_DELETE_WINDOW", self.on_alternative_close)

        # desabilita a main window
        self.janela_aberta = janela_aberta
        self.janela_aberta.set(True)

        # salva o objeto da janela pricipal e desativa a bind do macro e a janela
        self.main_window = parent
        self.main_window.macro_off()
        parent.attributes('-disable', True)

        # fazer ela aparecer perto da pricipal
        pos_x = parent.winfo_x()
        pos_y = parent.winfo_y()
        self.geometry(f'228x108+{pos_x + randrange(10,40)}+{pos_y + randrange(10,40)}')
        self.geometry(f'{largura}x{altura + 25}')


        # tira a barra original
        self.overrideredirect(True)
        self.attributes('-topmost', True)
        
        # acresenta outra no lugar da cor do tema do windows e coloca o texto nela
        #self.cor_windows = get_color_hex_windows()
        # subistitui a cor do widows por uma cor padaro a branca para evitar problemas
        self.cor_windows = '#fff'
        
        self.frame_window_bar = tk.Frame(self, background=self.cor_windows, height=25)
        self.frame_window_bar.pack(fill='x')
        self.label_windows_name = tk.Label(self.frame_window_bar, text=windows_name, fg='black', bg=self.cor_windows)
        self.label_windows_name.pack(side='left', ipady=2)

        # ativa a movimentação da janela
        self.frame_window_bar.bind("<ButtonPress-1>", self.start_move)
        self.frame_window_bar.bind("<B1-Motion>", self.on_move)
        self.label_windows_name.bind("<ButtonPress-1>", self.start_move)
        self.label_windows_name.bind("<B1-Motion>", self.on_move)

        # muda a cor
        self.bind("<FocusIn>", self.on_focus_in)
        self.bind("<FocusOut>", self.on_focus_out)


    def on_alternative_close(self):
        # impede que feche a jenala de outra forma
        pass


    def on_focus_in(self, event = None):
        self.frame_window_bar.config(background=self.cor_windows)
        self.label_windows_name.config(fg='black')
        self.label_windows_name.config(bg=self.cor_windows)

    def on_focus_out(self, event):
        self.frame_window_bar.config(background="white")
        self.label_windows_name.config(fg='gray')
        self.label_windows_name.config(bg='white')

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def on_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.winfo_x() + deltax
        y = self.winfo_y() + deltay
        self.geometry(f"+{x}+{y}")
        

    def interna_close_window(self):
        # reabilita a bind do macro
        self.janela_aberta.set(False)
        self.main_window.attributes('-disable', False)
        self.main_window.macro_on()
        self.destroy()

