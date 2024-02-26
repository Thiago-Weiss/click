import tkinter as tk
from PIL import Image, ImageTk, ImageOps



root = tk.Tk()


width = 266
height = 55
root.geometry(f"{width}x{height}")


canvas = tk.Canvas(root, )
canvas.pack(expand=True, fill='both')


imagem_list = [
    (Image.open('tinytask/data_img/open.png'), "Open", 'gray'),
    (Image.open('tinytask/data_img/save.png'), "Save", 'gray'),
    (Image.open('tinytask/data_img/rec.png'), "Rec", 'blue'),
    (Image.open('tinytask/data_img/play.png'), "Play", 'green'),
    (Image.open('tinytask/data_img/exe.png'), ".exe", 'gray'),
    (Image.open('tinytask/data_img/prefs.png'), "Prefs", 'gray'),
]
imagens_tk = []
imagem_ids = []
textos_ids = []

tamanho = int(min((width - 100) / 6, height - 20))

y = height / 2 - 8
margem = int(100 / 12)
x = int(-margem / 2)


for index, img in enumerate(imagem_list):
    # formata a imagem e converte para uma imagem do tkinter
    imagem = ImageTk.PhotoImage(ImageOps.contain(img[0], size=(tamanho, tamanho)))
    imagens_tk.append(imagem)

    x += tamanho + margem * 2
    image_id = canvas.create_image(x, y, anchor=tk.E, image=imagens_tk[index])
    texto_id = canvas.create_text(x - tamanho / 2, int(y + 11 + tamanho / 2), anchor=tk.CENTER, text=f'{img[1]}', font=('Arial', 10), fill=img[2])

    imagem_ids.append(image_id)
    textos_ids.append(texto_id)




'''
# como mudar o texto
canvas.itemconfigure(textos_ids[3], text="asdasd")

# como mudar a imagem
nova_imagem = ImageTk.PhotoImage(ImageOps.contain(imagem_list[0][0], size=(tamanho, tamanho)))
canvas.itemconfigure(imagem_ids[3], image=nova_imagem)
'''



def mostrar_clicar(event):
    valor = width / 6
    if event.x < valor:
        print("open")
    elif event.x < valor * 2:
        print("save")
    elif event.x < valor * 3:
        print("rec")
    elif event.x < valor * 4:
        print("play")
    elif event.x < valor * 5:
        print("exe")
    elif event.x < valor * 6:
        print("prefs")


canvas.bind('<Motion>', mostrar_clicar)
canvas.configure(cursor="hand2")

root.mainloop()


