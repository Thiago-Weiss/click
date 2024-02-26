import tkinter as tk
from tkinter import ttk
from random import randrange
from PIL import Image, ImageTk, ImageOps







class Top_level_master(tk.Toplevel):
    def __init__(self, parent, janela_aberta, windows_name, largura, altura):
        super().__init__(master=parent)

        # se tentar fechar a jenala de outra forma
        self.protocol("WM_DELETE_WINDOW", self.interna_close_window)

        # desabilita a main window
        self.janela_aberta = janela_aberta
        self.janela_aberta.set(True)

        # salva o objeto da janela pricipal e desativa a bind do macro e a janela
        self.main_window = parent
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

        # cria o botao de fechar
        self.close_button = tk.Button(self.frame_window_bar, text='✕', width= 5, font=('Arial', 10), command= self.interna_close_window, relief='raised', borderwidth=0, background='white', activebackground= '#F1707A', activeforeground= 'white')
        self.close_button.pack(side= 'right')

        # configura o botao de fechar
        self.close_button.bind("<Enter>", self.close_button_enter)
        self.close_button.bind("<Leave>", self.close_button_leave)

        self.close_button.pack()

        # cria o frame pra usar no filhos
        self.frame_widgets = tk.Frame(self)
        self.frame_widgets.pack(expand=True, fill='both')

        # ativa a movimentação da janela
        self.frame_window_bar.bind("<ButtonPress-1>", self.start_move)
        self.frame_window_bar.bind("<B1-Motion>", self.on_move)
        self.label_windows_name.bind("<ButtonPress-1>", self.start_move)
        self.label_windows_name.bind("<B1-Motion>", self.on_move)

        # muda a cor
        self.bind("<FocusIn>", self.on_focus_in)
        self.bind("<FocusOut>", self.on_focus_out)



    def close_button_enter(self, event):
        self.close_button.config(background='red')
        self.close_button.config(foreground='white')

    def close_button_leave(self, event):
        self.close_button.config(background='white')
        self.close_button.config(foreground='black')


    def on_focus_in(self, event = None):
        self.frame_window_bar.config(background=self.cor_windows)
        self.label_windows_name.config(fg='black')
        self.label_windows_name.config(bg=self.cor_windows)
        self.close_button.config(foreground='black')

    def on_focus_out(self, event):
        self.frame_window_bar.config(background="white")
        self.label_windows_name.config(fg='gray')
        self.label_windows_name.config(bg='white')
        self.close_button.config(foreground='gray')

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
        self.destroy()



class MensagemBox_entry(Top_level_master):
    def __init__(self, parent, janela_aberta, windows_name, label_text, largura, altura, var):
        super().__init__(parent, janela_aberta, windows_name, largura, altura)
        
        imagem = Image.open('tinytask/data_img/ask.png')
        self.imagem = ImageTk.PhotoImage(ImageOps.contain(imagem, size=(55, 55)))

        frame_top = tk.Frame(self.frame_widgets, background='white')
        frame_bottom = tk.Frame(self.frame_widgets)
        frame_top.pack(expand=True, fill='both')
        frame_bottom.pack(fill='x', side='bottom')



        tk.Label(frame_top, image=self.imagem, background='white', font=('Arial', 10)).place(x=34, y=47, anchor='center')
        ttk.Label(frame_top, text= label_text, background='white').place(x=75, y=15)
        ttk.Entry(frame_top, background='white', width= 22).place(x=75, y=60)

        # estilo do botao só pra mudar a fonte
        style = ttk.Style()
        style.configure('Custom.TButton', font=('Arial', 8))
        # os dois botoes de baixo
        ttk.Button(frame_bottom, text='Cancelar', command=self.interna_close_window,  style='Custom.TButton',).pack(side='right', padx=10, pady=10)
        ttk.Button(frame_bottom, text='Ok',style='Custom.TButton').pack(side='right')


