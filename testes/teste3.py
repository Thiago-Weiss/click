
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
        clicking.add_command(label='Options', command=lambda: Window_click_config(self, self.janela_secundaria_aberta, self.mouse_value_str, self.click_value_str, self.freeze_pointer_bool))
        clicking.add_command(label='Repeat', command=lambda: Window_repeat_config(self, self.janela_secundaria_aberta, self.infinite_repeat, self.quant_repeat, self.timer_list))
        # 2.2.1
        recording.add_command(label='Multiple clicks', command=lambda: Window_multi_clicks_config(
            self, self.janela_secundaria_aberta, self.multiplos_clicks_bool, self.multi_clicks_pos))
        # 2.3.1, 2.3.2 e 2.3.3
        settings.add_command(label='Hotkey', command=lambda: Window_hot_key_config(self, self.janela_secundaria_aberta, self.hot_key, self.att_text_hotkey_button))
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