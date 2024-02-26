import tkinter as tk
from PIL import Image, ImageTk


class Alerta_entry(tk.Toplevel):
    def __init__(self, parent, x, y, destroy_bool):
        super().__init__(master= parent, background= 'lightyellow')
        self.destroy_bool = destroy_bool
        # configrando a tela
        self.overrideredirect(True)
        self.attributes('-topmost', True)
        self.geometry(f'+{x}+{y}')

        x1, y1, x2, y2 = 4, 4, 255, 55
        raio = 10
        grosura = 2
        canvas = tk.Canvas(self, width= x2, height= y2, background= 'lightyellow')
        canvas.pack()
        # Criar um retângulo com bordas arredondadas
        canvas.create_arc(x1, y1, x1 + raio*2, y1 + raio*2, start=90,extent=90, style=tk.ARC, width=grosura)
        canvas.create_arc(x1, y2 - raio*2, x1 + raio*2, y2, start=180,extent=90, style=tk.ARC, width=grosura)
        canvas.create_arc(x2 - raio*2, y1, x2, y1 + raio*2, start=0,extent=90, style=tk.ARC, width=grosura)
        canvas.create_arc(x2 - raio*2, y2 - raio*2, x2, y2, start=270,extent=90, style=tk.ARC, width=grosura)
        # Linhas retas entre os arcos
        canvas.create_line(x1 + raio, y1, x2 - raio, y1, width=grosura)
        canvas.create_line(x1 + raio, y2, x2 - raio, y2, width=grosura)
        canvas.create_line(x1, y1 + raio, x1, y2 - raio, width=grosura)
        canvas.create_line(x2, y1 + raio, x2, y2 - raio, width=grosura)

        image_pil = Image.open('auto_click_2/data_img/x.png')
        image_pil_resized = image_pil.resize((20, 20))
        image = ImageTk.PhotoImage(image_pil_resized)
        canvas.create_image(25, 20, anchor='center', image=image)

        canvas.create_text(45, 20, text='Unacceptable character',font=("Arial", 12), fill='blue', anchor='w')
        canvas.create_text(45, 40, text='You can only enter numbers here!',font=("Arial", 10), anchor='w')

        self.after(10000, self.time_to_destroy)
        self.after(50, self.verificar_destroy)

        self.mainloop()

    def time_to_destroy(self):
        self.destroy_bool.set(False)
        self.verificar_destroy()

    def verificar_destroy(self):
        if not self.destroy_bool.get():
            self.destroy()
        else:
            self.after(50, self.verificar_destroy)

