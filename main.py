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
        self.success_message = ttk.Label(frame,text="")
        self.success_message.grid(column=0,row=1, columnspan=2)
        self.window.mainloop()

    def open_file(self):
        #Open Image
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
            wm_image_name = self.file_name.name[:-4] + "_wm.png"
            watermark_image.save(wm_image_name)
            self.success_message.config(text="You're picture has officially been watermarked!\n " \
                                           "It will be saved in the same folder as the original image!")
        print(self.file_name.name[:-4])

window=Window()