import tkinter
from PIL import Image, ImageTk

main = tkinter.Tk()
img = Image.open('oreilly.jpg')
tkimg = ImageTk.PhotoImage(img)
tkinter.Label(main, image=tkimg).pack()
main.mainloop()