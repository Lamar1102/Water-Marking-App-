from tkinter import *
from tkinter import ttk
import tkinter.filedialog
from PIL import ImageFont
from PIL import ImageDraw,Image
import matplotlib.pyplot as plt

class Window:

    def __init__(self):
        self.file_name=""

        self.window = Tk()
        self.window.title("Water Marking App")
        frame = ttk.Frame(self.window, padding=50, width=100)
        frame.grid()
        ttk.Label(frame, text="Choose an image you would like to watermark from your files:").grid(column=0, row=0)
        ttk.Button(frame, text="Browse", command=self.open_file).grid(column=1, row=0)
        self.window.mainloop()

    def open_file(self):
        self.file_name = tkinter.filedialog.askopenfile(parent=self.window,mode='rb',title='Choose a file')

        with Image.open(self.file_name.name) as img:
            watermark_image = img.copy()
            draw = ImageDraw.Draw(watermark_image)
            font = ImageFont.truetype("arial.ttf",50)

            #Add watermark
            draw.text((0,200),"LM",
                      (255,255,255),font=font)
            plt.subplot(1, 2, 1)
            plt.title("white text")
            plt.imshow(watermark_image)
            watermark_image.show()
            watermark_image = watermark_image.save("testing.png")
        print(self.file_name.name)

window=Window()