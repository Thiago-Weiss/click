import tkinter as tk
from tkinter import ttk

root = tk.Tk()

mb = ttk.Menubutton(root, text='My widgets', style='info.Outline.TMenubutton')

mb.pack()

# create menu
menu = tk.Menu(mb)

# add options
option_var = tk.StringVar()
for option in ['option 1', 'option 2', 'option 3']:
    menu.add_radiobutton(label=option, value=option, variable=option_var)

# associate menu with menubutton
mb['menu'] = menu

root.mainloop()
