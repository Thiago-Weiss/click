import tkinter as tk
from tkinter import ttk
# meu
from master_top_level import Top_level_master
from widgets_tools import Alerta_entry


class Window_repeat_config(Top_level_master):
    def __init__(self, parent, janela_aberta,  infinite_repeat, quant_repeat, timer_list):
        super().__init__(parent=parent, janela_aberta= janela_aberta, windows_name='Clicking repeat', largura=402, altura=191)

        # salva as variaveis pricipais
        self.infinite_repeat = infinite_repeat
        self.quant_repeat = quant_repeat
        self.timer_list = timer_list

        # cria uma outra hot key pra ser usado somente dentro dessa class
        self.interna_infinite_repeat = tk.BooleanVar(value=self.infinite_repeat.get())
        self.interna_quant_repeat = tk.StringVar(value=self.quant_repeat.get())
        self.interna_timer_list = {
            'hours': tk.StringVar(value=self.timer_list['hours'].get()),
            'mins':  tk.StringVar(value=self.timer_list['mins'].get()),
            'secs':  tk.StringVar(value=self.timer_list['secs'].get()),
            'mili':  tk.StringVar(value=self.timer_list['mili'].get()), }

        self.digitou_errado = tk.BooleanVar(value=False)
        self.mensagem_erro = None
        self.bind("<FocusOut>", self.tirar_alerta_digitacao)

        self.widgets()




    def widgets(self):
        # frame pai de todos os widgets
        self.frame_widgets = tk.Frame(self)
        self.frame_widgets.pack(expand=True, fill='both')
        # layout
        self.frame_widgets.rowconfigure((1, 2, 3, 4), weight=1, uniform='a')
        self.frame_widgets.columnconfigure((1, 2), weight=1, uniform='a')

        # frame do top layout
        frame_top = ttk.Frame(self.frame_widgets, border=1, relief='solid')
        frame_top.grid(row=1, rowspan=2, column=1, columnspan=2,sticky='nswe', padx=5, pady=6)
        frame_top.rowconfigure((1, 2), weight=1, uniform='b')
        frame_top_top = ttk.Frame(frame_top)
        frame_top_top.grid(row=1, sticky='nswe')

        # widgets top top
        ttk.Radiobutton(frame_top_top, text='Repeat',variable=self.interna_infinite_repeat, value=False).pack(side='left', padx=12)
        ttk.Spinbox(frame_top_top, width=6, from_=1, to=999999, justify='center', validate='key', validatecommand=(self.register(self.validar_repeat), '%P'), textvariable=self.interna_quant_repeat).pack(side='left')
        ttk.Label(frame_top_top, text='  times').pack(side='left')
        # botao top bot
        ttk.Radiobutton(frame_top, text='Repeat until stopped',variable=self.interna_infinite_repeat, value=True).grid(row=2, sticky='w', padx=12)

        # mid
        frame_bot = ttk.Frame(self.frame_widgets)
        frame_bot.grid(row=3, column=1, columnspan=2)

        ttk.Label(frame_bot, text='Interval:          ').pack(side='left')
        # hours
        ttk.Entry(frame_bot, width=4, validate='key', justify='right', validatecommand=(self.register(self.validar_time), '%P'), textvariable=self.interna_timer_list['hours']).pack(side='left')
        ttk.Label(frame_bot, text='hours').pack(side='left')
        # mins
        ttk.Entry(frame_bot, width=4, validate='key', justify='right', validatecommand=(self.register(self.validar_time), '%P'), textvariable=self.interna_timer_list['mins']).pack(side='left')
        ttk.Label(frame_bot, text='mins').pack(side='left')
        # secs
        ttk.Entry(frame_bot, width=4, validate='key', justify='right', validatecommand=(self.register(self.validar_time), '%P'), textvariable=self.interna_timer_list['secs']).pack(side='left')
        ttk.Label(frame_bot, text='secs').pack(side='left')
        # mins
        ttk.Entry(frame_bot, width=4, validate='key', justify='right', validatecommand=(self.register(self.validar_time), '%P'), textvariable=self.interna_timer_list['mili']).pack(side='left')
        ttk.Label(frame_bot, text='milliseconds').pack(side='left')

        # parte de baixo com os botoes de cancel e ok que fecha essa janela
        ttk.Button(self.frame_widgets, text='Ok', command=lambda: self.fechar_janela(True), width=8).grid(row=4, column=1,  sticky='e', padx=16, ipady=3)
        ttk.Button(self.frame_widgets, text='Cancel', command=self.fechar_janela, width=8).grid(row=4, column=2,  sticky='w', padx=16, ipady=3)



    def validar_time(self, value):
        # faz a validaçao do entry
        validade = (value.isdigit() and len(value) <= 4) or value == ''
        if validade:
            # tira o alerta de erro se digiti certo
            self.digitou_errado.set(False)
            return True
        else:
            self.bell()
            if len(value) <= 4:
                self.after(10, self.alerta_digitou_errado)
            return False

    def validar_repeat(self, value):
        # faz a validaçao do entry
        validade = (value.isdigit() and len(value) <= 6) or value == ''
        if validade:
            # tira o alerta de erro se digiti certo
            self.digitou_errado.set(False)
            return True
        else:
            self.bell()
            if len(value) <= 6:
                self.after(10, self.alerta_digitou_errado)
            return False
        
    def alerta_digitou_errado(self):
        # coloca o alerta de erro
        if self.digitou_errado.get() == False:
            self.digitou_errado.set(True)
            x = self.winfo_rootx()
            y = self.winfo_rooty()
            self.mensagem_erro = Alerta_entry(self, x+210, y+50, self.digitou_errado)

    def tirar_alerta_digitacao(self, *args):
        # tira o alerta de erro depois de um tempo
        self.on_focus_out(())
        self.digitou_errado.set(False)
        
    def start_move(self, event):
        # chama a funçao original e chama a funcao de tirar o alerta de erro
        super().start_move(event)
        self.tirar_alerta_digitacao()

    def fechar_janela(self, salvar=False):
        # salva a nova hot key
        if salvar:
            self.infinite_repeat.set(self.interna_infinite_repeat.get())
            self.quant_repeat.set(1 if self.interna_quant_repeat.get() == '' else int(self.interna_quant_repeat.get()))
            self.timer_list['hours'].set(0 if self.interna_timer_list['hours'].get() == '' else int(self.interna_timer_list['hours'].get()))
            self.timer_list['mins'].set(0 if self.interna_timer_list['mins'].get() == '' else int(self.interna_timer_list['mins'].get()))
            self.timer_list['secs'].set(0 if self.interna_timer_list['secs'].get() == '' else int(self.interna_timer_list['secs'].get()))
            self.timer_list['mili'].set(0 if self.interna_timer_list['mili'].get() == '' else int(self.interna_timer_list['mili'].get()))

        # reativa a janela principal
        self.interna_close_window()





if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('228x105+1172+217')

    # vars
    janela_aberta = tk.BooleanVar(value=False)
    infinite_repeat = tk.BooleanVar(value=True)
    quant_repeat = tk.IntVar(value=1)
    timer_list = {
        'hours': tk.IntVar(value=0),
        'mins': tk.IntVar(value=0),
        'secs': tk.IntVar(value=0),
        'mili': tk.IntVar(value=0), }

    ttk.Button(root, text='press', command=lambda: Window_repeat_config(root, janela_aberta, infinite_repeat, quant_repeat, timer_list)).pack()

    root.mainloop()
