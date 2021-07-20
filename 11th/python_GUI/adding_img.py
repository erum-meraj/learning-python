import tkinter as tk
from PIL import Image, ImageTk

def say_hi():
    print("button pressed")

root = tk.Tk()

canvas = tk.Canvas( root, width= 800, height= 400)
canvas.grid(columnspan = 4, rowspan = 5)
#picture adding 
pic = Image.open('makar_sankranti.jpg')
pic = ImageTk.PhotoImage(pic)
pic_label = tk.Label(image = pic)
pic_label.image = pic
pic_label.grid(column= 2, row = 0)

display_text = tk.Label(root, text = "Happy Makar Sankranti", font = "Raleway")
display_text.grid(column = 2, row = 1)

frame = tk.Frame(width = 56, height = 23)
frame.grid(column = 1, row = 4)

button1 = tk.Button(root, text = "Its a button", bg = '#53F325', command = say_hi)
button1.grid(column = 2, row = 2)

inp_text = tk.Entry(frame, bg = '#6A3458')
inp_text.grid(column = 1, row = 4)
root.mainloop()