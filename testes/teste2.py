import tkinter as tk

def atualizar_texto():
    novo_texto = "Novo texto para o botão"

    play_menu.entryconfigure(1, label=novo_texto)

root = tk.Tk()

# Criando o menu
menubar = tk.Menu(root)
root.config(menu=menubar)

play_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Play", menu=play_menu)

# Armazenando as referências aos botões no próprio menu
botoes_menu = {}

# Adicionando um botão ao menu
texto_botao = "Botão Inicial"
play_menu.add_command(label=texto_botao, state='disabled', activebackground='#d3d3d3', command=lambda: print("Botão clicado"))
botoes_menu[texto_botao] = texto_botao

# Criando um botão para atualizar o texto
atualizar_button = tk.Button(root, text="Atualizar Texto", command=atualizar_texto)
atualizar_button.pack()

root.mainloop()
