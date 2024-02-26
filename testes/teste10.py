import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()
    root.title("Botão dentro do Canvas")

    canvas = tk.Canvas(root, bg='pink')
    canvas.pack(expand=True, fill='both')
    canvas.create_text(10, 10, text='asdaaaaaa', font=('Arial', 10), fill='red')

    # Adicionando um botão dentro do canvas
    button = tk.Button(canvas, text="Clique Aqui", relief='raised',  borderwidth=0, )
    canvas.create_window(100, 50, window=button)  # Posiciona o botão no canvas

    root.mainloop()

if __name__ == "__main__":
    main()
