import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageOps
# meu
from menu_configure import Menu_config

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # configura a janela
        self.width = 266
        self.height = 55
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)
        self.attributes('-topmost', True)
        self.title('TinyTask')
        try:
            self.iconbitmap('tinytask/data_img/camera.ico')
        except:
            pass


        # data
        self.creat_data()

        # cria o menu de configuraçao do app
        self.menu_config = Menu_config(self)

        # menu
        self.menu_buttons()



    def creat_data(self):
        # var que contrala se a janela principal está ativa ou nao
        self.janela_aberta = tk.BooleanVar(value=False)

        # speed
        self.speed = tk.IntVar(value=2)
        self.custom_speed = tk.IntVar(value=20)

        # repeat
        self.infinite_repeat = tk.BooleanVar(value= False)
        self.repeat = tk.IntVar(value= 1)

        # rec/play hotkey config
        self.rec_key = tk.IntVar(value=1)
        self.play_key = tk.IntVar(value=1)

        # topmost , ficar em cima dos outros apps
        self.topmost_bool = tk.BooleanVar(value= False)

        # mostrar texto
        self.show_text_bool = tk.BooleanVar(value= True)

    def menu_buttons(self):
        # cria o canvas pra armazenar os botoes
        self.canvas = tk.Canvas(self)
        self.canvas.pack(expand=True, fill='both')
        # salva as imagens e os textos dos botoes
        self.imagens_ids = []
        self.textos_ids = []

        # importa todas as imagens
        imagem_list = [
            (Image.open('tinytask/data_img/open.png'), "Open", 'gray'),
            (Image.open('tinytask/data_img/save.png'), "Save", 'gray'),
            (Image.open('tinytask/data_img/rec.png'), "Rec", 'blue'),
            (Image.open('tinytask/data_img/play.png'), "Play", 'green'),
            (Image.open('tinytask/data_img/exe.png'), ".exe", 'gray'),
            (Image.open('tinytask/data_img/prefs.png'), "Prefs", 'gray'),
        ]

        # define o tamanho de cada imagem, margem e pos
        tamanho = int(min((self.width - 100) / 6, self.height - 20))
        margem = int(100 / 12)
        y = self.height / 2 - 8
        x = int(-margem / 2)

        for index, img in enumerate(imagem_list):
            # formata a imagem e converte para uma imagem do tkinter
            imagem = ImageTk.PhotoImage(ImageOps.contain(img[0], size=(tamanho, tamanho)))
            self.imagens_ids.append(imagem)

            # posiciona a imagem e o texto
            x += tamanho + margem * 2
            self.canvas.create_image(x, y, anchor=tk.E, image=self.imagens_ids[index])
            texto_id = self.canvas.create_text(x - tamanho / 2, int(y + 11 + tamanho / 2), anchor=tk.CENTER, text=f'{img[1]}', font=('Arial', 10), fill=img[2])

            # armazena o id do texto
            self.textos_ids.append(texto_id)


        # cria a bind
        self.canvas.bind('<Button-1>', self.button_click)

        # muda o formato do cursor pra "mao"
        self.canvas.configure(cursor="hand2")

    def button_click(self, event):
        valor = self.width / 6
        if event.x < valor:
            print("open")
        elif event.x < valor * 2:
            print("save")
        elif event.x < valor * 3:
            print("rec")
        elif event.x < valor * 4:
            print("play")
        elif event.x < valor * 5:
            print("exe")
        elif event.x < valor * 6:
            x, y = self.winfo_pointerxy()
            self.menu_config.show_submenu(x, y)


if __name__ == '__main__':
    app = App()
    app.mainloop()
