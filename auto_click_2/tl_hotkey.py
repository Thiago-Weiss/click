import tkinter as tk
from tkinter import ttk, messagebox
import keyboard
# meu
from master_top_level import Top_level_master



class Window_hot_key_config(Top_level_master):
    def __init__(self, parent, janela_aberta, hot_key, att_text):
        super().__init__(parent=parent, janela_aberta= janela_aberta, windows_name='Hotkey Setting', largura=232, altura=111)

        # salva a hot key pricipal
        self.hot_key = hot_key
        self.att_text = att_text
        # cria uma outra hot key pra ser usado somente dentro dessa class
        self.interna_hot_key = tk.StringVar(value=self.hot_key.get())

        self.widgets()

    def widgets(self):
        # frame pai de todos os widgets
        self.frame_widgets = tk.Frame(self)
        self.frame_widgets.pack(expand=True, fill='both')
        # layout
        self.frame_widgets.rowconfigure((1, 2), weight=1, uniform='a')
        self.frame_widgets.columnconfigure((1, 2), weight=1, uniform='a')

        # parte de cima botao de configuraçao da hot key e entry que mostar o texto
        self.hot_key_display = ttk.Entry(self.frame_widgets, textvariable=self.interna_hot_key, font=10, width=10, justify='center', state='readonly')
        self.hot_key_display.grid(row=1, column=2,  sticky='w', padx=5, ipadx=3, ipady=3)
        self.configure_key = ttk.Button(self.frame_widgets, text='Click / Stop', command=self.trocar_hot_key, width=15)
        self.configure_key.grid(row=1, column=1,  sticky='e', padx=5, ipady=5)

        # parte de baixo com os botoes de calcel e ok que fecha essa janela
        self.cancel = ttk.Button(self.frame_widgets, text='Cancel', command=self.fechar_janela, width=8)
        self.cancel.grid(row=2, column=2,  sticky='w', padx=16, ipady=3)
        self.ok = ttk.Button(self.frame_widgets, text='Ok',command=lambda: self.fechar_janela(True), width=8)
        self.ok.grid(row=2, column=1,  sticky='e', padx=16, ipady=3)

    def trocar_hot_key(self):
        # deastiva os botoes
        self.configure_key.configure(state='disabled')
        self.ok.configure(state='disabled')

        # troca o texto do entry
        self.interna_hot_key.set(value='Please key')

        # teclas proibidas com alt
        alt_block_key = ['f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11','f12']


        # funçao pra configura a hot key
        combo_keys_list = ['alt', 'ctrl', 'shift']
        white_list_keys = combo_keys_list + [
            'caps lock',
            'tab',
            'f1',
            'f2',
            'f3',
            'f4',
            'f5',
            'f6',
            'f7',
            'f8',
            'f9',
            'f10',
            'f11',
            'f12',]
        mapeamento_numeros = {
            'alt gr': 'alt',
            'right shift': 'shift',
            'right ctrl': 'ctrl',
            '"': "'",
            '!': '0',
            '@': '1',
            '#': '2',
            '$': '3',
            '%': '4',
            '¨': '5',
            '&': '6',
            '*': '7',
            '(': '8',
            ')': '9',
        }

        def hot_key_config(key):
            # validaçao da key
            key_validade = False
            # valida se é um numero
            if key.name in mapeamento_numeros:
                key.name = mapeamento_numeros[key.name]
                key_validade = True

            # valida se é uma das teclas permitidas
            if key.name in white_list_keys and key_validade == False:
                key_validade = True
            else:
                # valida se é uma letra
                if len(key.name) == 1:
                    if ord('A') <= ord(key.name) <= ord('Z') or ord('a') <= ord(key.name) <= ord('z') or ord('1') <= ord(key.name) <= ord('9'):
                        key_validade = True

            # se a key foi validada
            if key_validade:
                # verifica se vai ser combo key e se é a primeira da combo
                if key.name in combo_keys_list and self.interna_hot_key.get() == 'Please key':
                    self.interna_hot_key.set(value=key.name.title())
                else:
                    # se for um single key
                    if self.interna_hot_key.get() == 'Please key':
                        self.interna_hot_key.set(value=key.name.title())
                        keyboard.unhook_all()
                        self.configure_key.configure(state='enabled')
                        self.ok.configure(state='enabled')


                    # se for a segunda da combo key
                    else:
                        # se a primeira tecla foi alt e a segunda for um dos f1,2,3,4...
                        # exibe um alerta que n pode e coloca uma combo key padrao
                        if key.name in alt_block_key and self.interna_hot_key.get() == 'Alt':
                            # desativa a jenela
                            self.attributes('-disable', True)
                            # alerta informando que n pode usar alt + f1,2,3,4...
                            messagebox.showinfo('info', f'ALT + {key.name.upper()} already using!')
                            # reativa a janela depois de fechar o alerta
                            self.attributes('-disable', False)
                            # coloca ela na frente das outras janelas
                            self.attributes('-topmost', True)
                            # chama a funcao pra colocar o foco nessa janela dnv
                            self.on_focus_in()
                            # seta uma nova combo key padrao e desativa a config da hot key
                            self.interna_hot_key.set('Shift + E')
                            keyboard.unhook_all()
                            self.configure_key.configure(state='enabled')
                            self.ok.configure(state='enabled')

                        # verica se é uma tecla permitida
                        elif key.name not in combo_keys_list + ['caps lock', 'tab']:
                            self.interna_hot_key.set(self.interna_hot_key.get() + ' + ' + key.name.title())
                            keyboard.unhook_all()
                            self.configure_key.configure(state='enabled')
                            self.ok.configure(state='enabled')

                        # se n for uma tecla permitida subistitui a primeira tecla da combo key por essa agora precionada
                        else:
                            if not key.name in ['caps lock', 'tab']:
                                self.interna_hot_key.set(value=key.name.title())

        # funçao que chama a funçao de cima para configurar a hot key
        keyboard.on_press(hot_key_config)

    def fechar_janela(self, salvar=False):
        # salva a nova hot key
        if salvar:
            self.hot_key.set(self.hot_key_display.get().title())
            self.att_text()

        # desativa o a detecção do keyboard
        keyboard.unhook_all()
        # reativa a janela principal
        self.interna_close_window()




if __name__ == '__main__':
    def print_hot_key():
        print(hot_key.get())
    root = tk.Tk()
    root.geometry('228x105+1172+217')

    # vars
    janela_aberta = tk.BooleanVar(value=False)
    hot_key = tk.StringVar(value='F8')

    ttk.Button(root, text='press', command=lambda: Window_hot_key_config(root, janela_aberta, hot_key, print_hot_key)).pack()

    root.mainloop()
