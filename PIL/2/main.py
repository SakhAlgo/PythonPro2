#подключи нужные модули PIL
from PIL import Image, ImageEnhance, ImageFilter
#создай класс ImageEditor
class ImageEditor():
    #создай конструктор класса
    def __init__(self, file):
        self.file = file
        self.origin = None
        self.list = []

    #создай метод "открыть и показать оригинал"
    def make_origin(self):
        try:
            self.origin = Image.open(self.file)
        except:
            print('Не получилось открыть файл.')
        self.list.append('origin.jpg')

    def get_len_list(self):
        return len(self.list)

    def open(self):
        self.origin.show()

    #создай методы для редактирования оригинала
    def get_bw(self):
        pic_bw = self.origin.convert('L')
        num = self.get_len_list()
        pic_bw.save(f'./img/origin{num}.jpg')
        self.list.append(f'origin{num}.jpg')
        pic_bw.show()

    def get_blur(self):
        pic_blur = self.origin.filter(ImageFilter.BLUR)
        num = self.get_len_list()
        pic_blur.save(f'./img/origin{num}.jpg')
        self.list.append(f'origin{num}.jpg')
        pic_blur.show()

    def do_cropped(self):
        box = (300, 100, 500, 350)
        crop = self.origin.crop(box)
        crop.save('./img/pic_crop.jpg')
        self.list.append('pic_crop.jpg')
        crop.show()

#создай объект класса ImageEditor с данными картинки-оригинала
pic = ImageEditor('original.jpg')
pic.make_origin()
pic.get_bw()
pic.get_blur()
# pic.do_cropped()
#отредактируй изображение и сохрани результат