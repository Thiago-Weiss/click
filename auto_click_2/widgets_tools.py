from PIL import Image, ImageTk
import tkinter as tk
import mouse
import winreg

class Tooltip_label:
    def __init__(self, parent, widget, text, verificar_state = False):
        self.parent = parent
        self.widget = widget
        self.verificar_state = verificar_state

        # binds
        self.widget.bind("<Enter>", lambda event: self.create_timer(event, text))
        self.widget.bind("<Leave>", lambda event: self.create_timer(event, ''))

        # data
        self.timer = False
        self.tooltip = False

    def create_timer(self, event, text):
        if event.type == '7':  # '7' representa o evento <Enter>
            if not self.timer:
                self.tooltip_id = self.parent.after(1000, self.creat_tooltip, text)
                self.timer = True

        elif event.type == '8':  # '8' representa o evento <Leave>
            self.timer = False
            self.parent.after_cancel(self.tooltip_id)
            if self.tooltip:
                self.tooltip = False
                self.top_level_text.destroy()

    def creat_tooltip(self, text):

        if self.timer and not self.tooltip:
            if self.verificar_state:
                if not self.widget.cget("state") == 'enabled':
                    return
            self.top_level_text = tk.Toplevel(self.parent)
            self.top_level_text.overrideredirect(True)
            self.top_level_text.attributes('-topmost', True)
            x, y = mouse.get_position()
            self.top_level_text.geometry(f"+{x}+{y+20}")
            tk.Label(self.top_level_text, text= text, bg='lightyellow', relief='solid', borderwidth=1).pack()
            self.tooltip = True





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

        image_pil = Image.open('x.png')
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





# cria uma estrutura de dados de lista estilo a do tkinter
class ListVar:
    def __init__(self, initial_value=None):
        self._value = initial_value if initial_value is not None else []

    def set(self, value):
        self._value = value

    def get(self):
        return self._value





# retorna a cor do windows ou o branco
def get_color_hex_windows():
    def get_windows_color():
        key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Accent'
        try:
            reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
            subkey = winreg.OpenKey(reg, key)
            value, _ = winreg.QueryValueEx(subkey, 'AccentColorMenu')
            return value
        except Exception as e:
            print(f"Erro ao acessar o registro: {e}")
            return None

    def decimal_to_hex(decimal_color):
        blue = decimal_color & 255
        green = (decimal_color >> 8) & 255
        red = (decimal_color >> 16) & 255
        return "#{:02x}{:02x}{:02x}".format(blue, green, red)

    window_color_decimal = get_windows_color()
    if window_color_decimal is not None:
        hex_color = decimal_to_hex(window_color_decimal)
    else:
        hex_color = "#FFFFFF"
    return hex_color
