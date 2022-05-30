from PIL import Image, ImageDraw, ImageFont
from tkinter import filedialog
from tkinter import Tk

root = Tk()
root.withdraw()
filename = filedialog.askopenfilename(initialdir='/Users/koira/Downloads', title='Select an Image:')
##print(filename)

def add_watermark(image, wm_text):
    #creates the image object
    opened_image = Image.open(image)

    #Get Image size
    image_width, image_height = opened_image.size

    #Draw in Image
    draw = ImageDraw.Draw(opened_image)

    #Specify a font size
    font_size = int(image_width / 8)

    #specify a font type
    font = ImageFont.truetype('arial.ttf', font_size)

    #coordinates for where we want the image
    x, y = int(image_width/2), int(image_height / 2)

    #add the watermark
    draw.text((x,y), wm_text, font=font, fill='#FFF', stroke_width=5, stroke_fill='#223', anchor='ms')

    #show the new image
    opened_image.show()

add_watermark(filename, "code with susmin")