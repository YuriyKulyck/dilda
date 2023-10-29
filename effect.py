from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

with Image.open('img.png') as pic_original:
    pic_blured = pic_original.filter(ImageFilter.GaussianBlur(3.1111111))
    pic_blured.save('blured.jpg')
    pic_blured.show()