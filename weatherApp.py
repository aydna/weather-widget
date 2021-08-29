import tkinter as tk
from PIL import Image
from PIL import ImageTk


HEIGHT = 700
WIDTH = 800

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

bgImg = Image.open('weatherBg.png')
bgImg = ImageTk.PhotoImage(bgImg)
bgLabel = tk.Label(root, image=bgImg)
bgLabel.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#99ceff', bd=5)
frame.place(relwidth=0.75, relheight=0.1, relx=0.5, rely=0.1, anchor="n")

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.7, relheight=1)

button1 = tk.Button(frame, text="Test button", font=40)
button1.place(relwidth=0.3, relheight=1, relx=0.7)

lowerFrame = tk.Frame(root, bg='#99ceff', bd=10)
lowerFrame.place(relwidth=0.75, relheight=0.6, relx=0.5, rely=0.25, anchor='n')

label = tk.Label(lowerFrame)
label.place(relwidth=1, relheight=1)

root.mainloop()