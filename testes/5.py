import tkinter as tk
import webbrowser

def open_youtube():
    webbrowser.open("https://www.youtube.com")

root = tk.Tk()
root.title("Abrir YouTube")

button = tk.Button(root, text="Abrir YouTube", command=open_youtube)
button.pack()

root.mainloop()
