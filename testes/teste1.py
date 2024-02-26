import tkinter as tk
from PIL import Image, ImageTk

# Função para carregar a imagem
def carregar_imagem():
    imagem = Image.open('tinytask/data_img/ask.png')  # Substitua "exemplo.png" pelo caminho da sua imagem
    imagem = imagem.resize((100, 100))  # Ajuste o tamanho conforme necessário
    imagem = ImageTk.PhotoImage(imagem)
    return imagem

# Criando a janela principal
root = tk.Tk()
root.geometry("300x200")
root.title("Frame com Label e Imagem")

# Criando o frame
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Criando a label e a imagem
label = tk.Label(frame, text="Minha Label")
label.pack(pady=10)

imagem = carregar_imagem()
label_imagem = tk.Label(frame, image=imagem)
label_imagem.image = imagem  # Mantenha uma referência para a imagem
label_imagem.pack(pady=10)

root.mainloop()
