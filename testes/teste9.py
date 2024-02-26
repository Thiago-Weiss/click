import tkinter as tk
from tkinter import ttk


def main():
    root = tk.Tk()
    root.title("Símbolo de Correto")
    root.geometry("200x200")  # Define o tamanho da janela para 200x200 pixels

    # Define a cor de fundo da janela como azul
    root.configure()

    # Adiciona um frame para o símbolo
    frame = ttk.Frame(root)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Desenha o símbolo de correto (um simples quadrado preto)
    symbol = ttk.Label(frame, text="✓", font=(
        'Arial', 20), background="blue", foreground="black")
    symbol.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
