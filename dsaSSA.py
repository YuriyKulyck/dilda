import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

files = os.listdir("photos")
for photo in files:
    with Image.open("photos/" + photo) as image:

        draw = ImageDraw.Draw(image)

        font = ImageFont.truetype("Adventure.ttf", 30)

        draw.text((10, 10), "communism", font=font, fill="red")
        image.save("result/"+photo)