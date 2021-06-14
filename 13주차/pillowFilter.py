from PIL import Image, ImageTk, ImageFilter
import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, width=500, height=500)
canvas.pack()

img = Image.open("lenna.png")
img_filt = img.filter(ImageFilter.CONTOUR)
tk_img = ImageTk.PhotoImage(img_filt)

canvas.create_image(250, 250, image=tk_img)

window.mainloop()
