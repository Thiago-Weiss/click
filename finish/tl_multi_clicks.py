import tkinter as tk
from tkinter import ttk, messagebox
import mouse
# meu
from widgets_tools import Tooltip_label, ListVar
from master_top_level import Top_level_master



class Window_multi_clicks_config(Top_level_master):
    def __init__(self, parent, janela_aberta, multiplos_clicks_bool, multi_clicks_pos):
        super().__init__(parent=parent, janela_aberta= janela_aberta, windows_name='Record multiple clicks', largura=286, altura=176)

        # salva as variaveis pricipais
        self.multiplos_clicks_bool = multiplos_clicks_bool
        self.multi_clicks_pos = multi_clicks_pos

        # cria uma outra hot key pra ser usado somente dentro dessa class
        self.interna_multiplos_clicks_bool = tk.BooleanVar(value=multiplos_clicks_bool.get())
        self.interna_lista_pos_clicks = self.multi_clicks_pos.get()[:]
        self.interna_quant_clicks = tk.IntVar(value=len(self.interna_lista_pos_clicks))

        self.widgets()



    def widgets(self):
        # frame pai de todos os widgets
        self.frame_widgets = tk.Frame(self)
        self.frame_widgets.pack(expand=True, fill='both')
        # layout
        self.frame_widgets.rowconfigure((1, 2, 3, 4, 5, 6), weight=1, uniform='d')
        self.frame_widgets.columnconfigure((1, 2, 3, 4, 5, 6), weight=1, uniform='d')

        # 1 linha Record
        ttk.Checkbutton(self.frame_widgets, command=self.ativar_multiple_clicks, onvalue=True, offvalue=False, text='Record and replay multiple clicks',variable=self.interna_multiplos_clicks_bool).grid(row=1, rowspan=2, column=1, columnspan=6, sticky='nw', padx=15, pady=14)
        # 2 linha label Click records
        self.label_click = ttk.Label(self.frame_widgets, text='Click records:')
        self.label_click.grid(row=2, rowspan=2, column=1,columnspan=3, sticky='w', padx=15, pady=35)
        # 2 linha entry
        self.entry_len_pos = ttk.Entry(self.frame_widgets, textvariable=self.interna_quant_clicks, state='readonly', width=11, justify='right')
        self.entry_len_pos.grid(row=2, rowspan=2, column=3, columnspan=2, sticky='e', padx=4, ipadx=1)
        # 3 linha button Clear
        self.button_clear = ttk.Button(self.frame_widgets, text='Clear', command=self.limpar_lista_pos, width=11)
        self.button_clear.grid(row=3, rowspan=2, column=3,columnspan=2, sticky='e', padx=3)
        # 2/3 linha button Pick
        self.button_pick = ttk.Button(self.frame_widgets, text='Pick point', command=self.add_lista_pos)
        self.button_pick.place(x=190, y=43, width=86, height=57)
        # habilita a exibiçao de texto
        Tooltip_label(self.frame_widgets, self.button_pick, 'Pick the place you want to click', verificar_state= True)

        # Cancel/Ok
        ttk.Button(self.frame_widgets, text='Ok', command=lambda: self.fechar_janela(True), width=8).grid(row=5, rowspan=2, column=1, columnspan=3,  sticky='e', padx=22, ipady=3, pady=9)
        ttk.Button(self.frame_widgets, text='Cancel', command=self.fechar_janela, width=8).grid(row=5, rowspan=2, column=4, columnspan=3,  sticky='w', padx=22, ipady=3, pady=9)

        # define os estatod dos botoes de acordo com a checkbox
        self.ativar_multiple_clicks()


    def limpar_lista_pos(self):
        # cria uma janela de confimação antes de excluir as pos
        self.attributes('-disable', True)
        self.attributes('-topmost', False)
        if messagebox.askquestion('info', 'Are you sure to clear all the records?') == 'yes':
            self.interna_lista_pos_clicks.clear()
            self.interna_quant_clicks.set(len(self.interna_lista_pos_clicks))
        self.attributes('-disable', False)
        self.attributes('-topmost', True)


    def add_lista_pos(self):
        # minimiza a tela principal
        self.overrideredirect(False)
        self.main_window.iconify()
        self.iconify()

        # click do mouse, pega a pos e adiciona
        def on_event(*args):
            self.interna_lista_pos_clicks.append(mouse.get_position())
            self.interna_quant_clicks.set(len(self.interna_lista_pos_clicks))
            top_level_text.clicked.set(True)
            mouse.unhook_all()

        # funçao pra atualizar a janela
        def update_position():
            x, y = top_level_text.winfo_pointerxy()
            top_level_text.pos_x_y.set(f'x:{x}, y:{y}')
            top_level_text.geometry(f"+{x}+{y+10}")
            if top_level_text.clicked.get() == False:
                top_level_text.after(10, update_position)
            else:
                top_level_text.after_cancel(update_position)

        # cria a outra janela
        top_level_text = tk.Toplevel(self)
        top_level_text.overrideredirect(True)
        top_level_text.attributes('-topmost', True)
        top_level_text.pos_x_y = tk.StringVar(value=top_level_text.winfo_pointerxy())
        ttk.Label(top_level_text, textvariable=top_level_text.pos_x_y).pack()
        # chama a funçao que fica no loop esperando o click
        top_level_text.clicked = tk.BooleanVar(value= False)

        # ativa o texto e espera o click
        update_position()
        mouse.on_click(on_event)
        self.wait_variable(top_level_text.clicked)

        # abre a janela denovo

        self.main_window.deiconify()
        self.deiconify()
        self.overrideredirect(True)
        self.focus_set()
        self.main_window.attributes('-topmost', True)
        self.attributes('-topmost', True)

        
        top_level_text.destroy()


    def ativar_multiple_clicks(self):
        # define os estatod dos botoes de acordo com a checkbox
        if not self.interna_multiplos_clicks_bool.get():
            self.label_click.configure(state='disabled')
            self.entry_len_pos.configure(state='disabled')
            self.button_clear.configure(state='disabled')
            self.button_pick.configure(state='disabled')
        else:
            self.label_click.configure(state='enabled')
            self.entry_len_pos.configure(state='readonly')
            self.button_clear.configure(state='enabled')
            self.button_pick.configure(state='enabled')


    def fechar_janela(self, salvar=False):
        # salva a nova hot key
        if salvar:
            if self.interna_multiplos_clicks_bool.get() and self.interna_lista_pos_clicks == []:
                messagebox.showinfo('info', 'Please pick a point you wanto to click!')
                return

            self.multiplos_clicks_bool.set(self.interna_multiplos_clicks_bool.get())
            self.multi_clicks_pos.set(self.interna_lista_pos_clicks[:])
            print(self.multi_clicks_pos.get())

        # reativa a janela principal
        self.interna_close_window()






if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('228x105+1172+217')

    # vars
    janela_aberta = tk.BooleanVar(value= False)

    lista_pos_clicks = ListVar([])
    multiplos_clicks_bool = tk.BooleanVar(value= False)

    ttk.Button(root, text= 'press', command= lambda: Window_multi_clicks_config(root, janela_aberta, multiplos_clicks_bool, lista_pos_clicks)).pack()

    root.mainloop()

