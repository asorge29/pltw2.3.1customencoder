from PIL import Image

class Decoder():
    def __init__(self):
        self.image_path = ''
        self.colors = []
        self.hexes = []
        self.unicode_chars = []
        self.chars = []
        self.msg = ''
        self.suffix = 0
        self.image = None
        self.start_pixel = (0, 0)

    def decode(self, image_path, suffix=65280):
        self.image_path = image_path
        self.suffix = hex(suffix)[2:6]
        while len(self.suffix) < 4:
            self.suffix = "0" + self.suffix

        self._open_image()

    def _open_image(self):
        self.image = Image.open(self.image_path)
        self.image = self.image.convert('RGB')
        for i in range(0, self.image.width):
            for j in range(0, self.image.height):
                r, g, b = self.image.getpixel((i, j))
                if r == 255 and g == 0 and b == 0:
                    self.start_pixel = (i, j)
                    print(self.start_pixel)
                    break