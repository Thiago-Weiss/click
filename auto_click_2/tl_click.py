import tkinter as tk
from tkinter import ttk
# meu
from master_top_level import Top_level_master
from widgets_tools import Tooltip_label





class Window_click_config(Top_level_master):
    def __init__(self, parent, janela_aberta, mouse_value_str, click_value_str, freeze_pointer_bool):
        super().__init__(parent= parent, janela_aberta= janela_aberta, windows_name='Clicking options', largura=276, altura=184)

        # salva as variaveis pricipais
        self.mouse_value_str = mouse_value_str
        self.click_value_str = click_value_str
        self.freeze_pointer_bool = freeze_pointer_bool

        # cria uma outra hot key pra ser usado somente dentro dessa class
        self.intera_mouse_value_str = tk.StringVar(value= self.mouse_value_str.get())
        self.intera_click_value_str = tk.StringVar(value= self.click_value_str.get())
        self.intera_freeze_pointer_bool = tk.BooleanVar(value= self.freeze_pointer_bool.get())

        self.widgets()


    def widgets(self):
        # frame pai de todos os widgets
        self.frame_widgets = tk.Frame(self)
        self.frame_widgets.pack(expand=True, fill='both')
        # layout
        self.frame_widgets.rowconfigure((1,2,3,4,5,6), weight= 1, uniform= 'c')
        self.frame_widgets.columnconfigure((1,2,3,4), weight= 1, uniform= 'c')

        # 1 linha Mouse
        mouse_values = ['Left', 'Right', 'Middle']
        ttk.Label(self.frame_widgets, text= 'Mouse:').grid(row= 1, rowspan=2, column=1, columnspan=2, sticky='wn', padx= 14, pady= 14)
        ttk.Combobox(self.frame_widgets, textvariable= self.intera_mouse_value_str, state= 'readonly', values= mouse_values, width= 8).grid(row= 1, rowspan=2, column=1, columnspan=2, sticky='en', pady= 14)

        # 2 linha Click
        click_values = ['Single', 'Double']
        ttk.Label(self.frame_widgets,text= 'Click:').grid(row= 2, rowspan= 2, column=1, columnspan=2, sticky='ws', padx= 14, pady= 14)
        ttk.Combobox(self.frame_widgets, textvariable= self.intera_click_value_str, state= 'readonly', values= click_values, width= 8).grid(row= 2, rowspan=2, column=1, columnspan=2, sticky='es', pady= 14)

        # 3 linha Freeze
        freeze_button = ttk.Checkbutton(self.frame_widgets, text= 'Freeze the pointer (only single click)', variable= self.intera_freeze_pointer_bool)
        freeze_button.grid(row= 4, column=1, columnspan=4, sticky= 'w', padx= 14)
        Tooltip_label(self.frame_widgets, freeze_button, 'Freeze the pointer on the place you want tc click')
        
        # Cancel/Ok
        ttk.Button(self.frame_widgets, text='Ok', command=lambda: self.fechar_janela(True), width=8).grid(row=5, rowspan=2, column=1, columnspan=2,  sticky='e', padx=16, ipady=3, pady= 9)
        ttk.Button(self.frame_widgets, text='Cancel', command=self.fechar_janela, width=8).grid(row=5, rowspan=2, column=3, columnspan=2,  sticky='w', padx=16, ipady=3, pady= 9)


    def fechar_janela(self, salvar=False):
        # salva a nova hot key
        if salvar:
            self.mouse_value_str.set(self.intera_mouse_value_str.get())
            self.click_value_str.set(self.intera_click_value_str.get())
            self.freeze_pointer_bool.set(self.intera_freeze_pointer_bool.get())

        # reativa a janela principal
        self.interna_close_window()





if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('228x105+1172+217')

    # vars
    janela_aberta = tk.BooleanVar(value= False)
    mouse_value_str = tk.StringVar(value='Left')
    click_value_str = tk.StringVar(value= 'Single')
    freeze_pointer_bool = tk.BooleanVar(value= False)

    ttk.Button(root, text= 'press', command= lambda: Window_click_config(root, janela_aberta, mouse_value_str, click_value_str, freeze_pointer_bool)).pack()

    root.mainloop()
