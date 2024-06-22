import tkinter as tk
from tkinter import ttk
import json
import keyboard
import webbrowser
import os

# minhas
from tl_click import Window_click_config
from tl_hotkey import Window_hot_key_config
from tl_multi_clicks import Window_multi_clicks_config
from tl_repeat import Window_repeat_config
from widgets_tools import ListVar
from click_core import Click


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # configura a janela
        self.geometry('232x130+1157+442')
        self.resizable(False, False)
        self.attributes('-topmost', True)
        self.title('GS Auto Clicker')
        try:
            current_directory = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(current_directory, 'data_img/star.ico')
            self.iconbitmap(file_path)
        except:
            pass
        # chama todas as funçoes de inicializaçao do app
        # data
        self.create_data()
        # top menu
        self.create_menu_top()
        # main menu
        self.create_menu()

        # atualiza a forma de fechar o app
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    # cria/abre todo o data/variaveis de um arquivo json

    def create_data(self):
        # variavel que controla se o macro está ligado
        self.macro_on_bool = tk.BooleanVar(value=False)

        # varivel que controla o texto do botao da hotkey
        self.hotkey_button_text_str = tk.StringVar(value='Press -- to click')

        # variavel que controla se tem mais de uma janela aberta
        self.janela_secundaria_aberta = tk.BooleanVar(value=False)

        # data inicial se tiver data criado
        data = {
            'hotkey': 'q',
            'multi_clicks': False,
            'multi_clicks_pos': [],
            'mouse_value_str': 'Left',
            'click_value_str': 'Single',
            'freeze': False,
            'infinite_repeat': True,
            'quant_repeat': 1,
            'time': [0, 0, 0, 0]
        }
        try:
            # Obtenha o diretório atual do script
            current_directory = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(current_directory, 'data_img/dados.json')
            print (current_directory)
            # Carregando dados de um arquivo JSON
            with open(file_path, 'r') as file:
                data = json.load(file)
        except:
            pass

            # hot key
        # data hot key
        self.hot_key = tk.StringVar(value=data['hotkey'])

        # multiclics
        # data bool multiplos clicks
        self.multiplos_clicks_bool = tk.BooleanVar(value=data['multi_clicks'])
        # pos dos multiplos clicks
        self.multi_clicks_pos = ListVar(data['multi_clicks_pos'])

        # click config
        # qual o botao esquerdo, meio ou direito
        self.mouse_value_str = tk.StringVar(value=data['mouse_value_str'])
        # qual o tipo de click single ou doble
        self.click_value_str = tk.StringVar(value=data['click_value_str'])
        # mouse travado/freezado no lugar
        self.freeze_pointer_bool = tk.BooleanVar(value=data['freeze'])

        # repeat config
        # se está no modo de repetir infinito = true ou x vezes = false
        self.infinite_repeat = tk.BooleanVar(value=data['infinite_repeat'])
        # quantidade de repetiçoes
        self.quant_repeat = tk.IntVar(value=data['quant_repeat'])
        # tempo entre os clicks/repetiçoes
        self.timer_list = {
            'hours': tk.IntVar(value=data['time'][0]),
            'mins': tk.IntVar(value=data['time'][1]),
            'secs': tk.IntVar(value=data['time'][2]),
            'mili': tk.IntVar(value=data['time'][3]), }

        # cria o objeto de click
        self.macro = Click(self.macro_on_bool, self.att_text_hotkey_button)

    # salva o data/variaveis em um arquivo json
    def on_close(self):
        # Salvando dados em um arquivo JSON
        data = {
            'hotkey': self.hot_key.get(),
            'multi_clicks': self.multiplos_clicks_bool.get(),
            'multi_clicks_pos': self.multi_clicks_pos.get(),
            'mouse_value_str': self.mouse_value_str.get(),
            'click_value_str': self.click_value_str.get(),
            'freeze': self.freeze_pointer_bool.get(),
            'infinite_repeat': self.infinite_repeat.get(),
            'quant_repeat': self.quant_repeat.get(),
            'time': [
                self.timer_list['hours'].get(),
                self.timer_list['mins'].get(),
                self.timer_list['secs'].get(),
                self.timer_list['mili'].get()]
        }
        current_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_directory, 'data_img/dados.json')
        with open(file_path, 'w') as file:
            json.dump(data, file)
        self.destroy()

    # cria o menu superior e conecta com os outros arquivos
    def create_menu_top(self):
        menu_principal = tk.Menu(self)
        self.configure(menu=menu_principal)

        # 1 botao
        # crio o objeto e associo ele a um menu
        file = tk.Menu(menu_principal, tearoff=False)
        # aqui eu adiciono o botao e o comando
        file.add_command(label='Exit', command=lambda: self.on_close())
        # eu ligo os dois o menu principla ao sub menu e seu filhos
        menu_principal.add_cascade(label='File', menu=file)

        # 2 botao
        # crio o sub menu
        options = tk.Menu(menu_principal, tearoff=False)
        # os botoes
        clicking = tk.Menu(options, tearoff=False)
        recording = tk.Menu(options, tearoff=False)
        settings = tk.Menu(options, tearoff=False)
        # conectando eles com o sub menu
        # 2.1, 2.2 e 2.3
        options.add_cascade(label='Clicking', menu=clicking)
        options.add_cascade(label='Recording', menu=recording)
        options.add_cascade(label='Settings', menu=settings)
        # 2.1.1 e 2.1.1
        clicking.add_command(label='Options', command=lambda: Window_click_config(
            self, self.janela_secundaria_aberta, self.mouse_value_str, self.click_value_str, self.freeze_pointer_bool))
        clicking.add_command(label='Repeat', command=lambda: Window_repeat_config(
            self, self.janela_secundaria_aberta, self.infinite_repeat, self.quant_repeat, self.timer_list))
        # 2.2.1
        recording.add_command(label='Multiple clicks', command=lambda: Window_multi_clicks_config(
            self, self.janela_secundaria_aberta, self.multiplos_clicks_bool, self.multi_clicks_pos))
        # 2.3.1, 2.3.2 e 2.3.3
        settings.add_command(label='Hotkey', command=lambda: Window_hot_key_config(
            self, self.janela_secundaria_aberta, self.hot_key, self.att_text_hotkey_button))
        settings.add_command(label='View', command=lambda: print('View'))
        settings.add_command(label='Other', command=lambda: print('Other'))
        # conectando tudo
        menu_principal.add_cascade(label='Options', menu=options)

        # 3
        help = tk.Menu(menu_principal, tearoff=False)
        # 3.1 e 3.2
        help.add_command(label='How to automate a sequence of mouse clicks and keystrokes',
                         command=lambda: print('How to automate a sequence of mouse clicks and keystrokes'))
        help.add_command(label='About', command=lambda: print('About'))
        # conectando tudo
        menu_principal.add_cascade(label='Help', menu=help)

    # cria o menu inicial
    def create_menu(self):
        # cria os dois botoes do menu
        ttk.Button(self, textvariable=self.hotkey_button_text_str, command=lambda: Window_hot_key_config(
            self, self.janela_secundaria_aberta, self.hot_key, self.att_text_hotkey_button)).place(x=15, y=13, width=202, height=35)
        ttk.Button(self, text='Help >>', command=lambda: webbrowser.open(
            "https://www.youtube.com/@TimelapseCoderYT/videos")).place(x=15, y=61, width=202, height=35)
        # atualiza o texto do botao Hot key
        self.att_text_hotkey_button()
        # ativa a bind do macro
        self.macro_on()

    # funçao que atualiza o texto do botao Hot key
    def att_text_hotkey_button(self):
        action = 'Stop' if self.macro_on_bool.get() else 'Click'
        self.hotkey_button_text_str.set(
            f'Press {self.hot_key.get()} to {action}')

    # configura a bind que ativa o macro
    def macro_on(self):
        keyboard.add_hotkey(self.hot_key.get().lower(), self.switch_macro)

    # funçao pra desativar o macro e a bind que ativa ele
    def macro_off(self):
        keyboard.unhook_all()
        self.macro_on_bool.set(False)

    # funçao que chama a funçao de macro do objeto macro
    def switch_macro(self, *args):
        self.macro_on_bool.set(not self.macro_on_bool.get())
        if self.macro_on_bool.get():
            # configura todas os parametros
            # time
            time = (self.timer_list['mili'].get() / 1000) + self.timer_list['secs'].get() + (
                self.timer_list['mins'].get() * 60) + (self.timer_list['hours'].get() * 3600)
            # tipo do click
            double_bool = False if self.click_value_str.get() == 'Single' else True
            # se vai ter repetiçoes
            repeat = self.quant_repeat.get() if self.infinite_repeat.get() == False else False
            # possiçao dos multiclicks
            self.multi_clicks_pos.get()

            # chama a funçao do macro e passa todos os parametros
            self.macro.start_normal_macro(self.freeze_pointer_bool.get(), time, self.mouse_value_str.get(
            ), double_bool, repeat, self.multi_clicks_pos.get(), self.multiplos_clicks_bool.get())

        # atualiza o texto do menu
        self.att_text_hotkey_button()


if __name__ == '__main__':
    app = App()
    app.mainloop()
