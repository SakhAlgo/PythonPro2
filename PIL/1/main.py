from PIL import Image, ImageFilter, ImageEnhance

#открой файл с оригиналом картинки
with Image.open('1/original.jpg') as original:
    gray = original.convert('L')
    # gray.show()
#сделай оригинал изображения чёрно-белым

#сделай оригинал изображения размытым
    pic_blur = original.filter(ImageFilter.BLUR)
    # pic_blur.show()
#поверни оригинал изображения на 180 градусов
    contrast = ImageEnhance.Contrast(original)
    rot = contrast.enhance(1.5)
    rot.show()