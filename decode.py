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
        self._find_start_pixel()
        self.colors = self._pull_hex_colors()
        self.hexes = self._pull_hexes()
        self.unicode_chars = self._hex_to_unicode()
        self.chars = self._unicode_to_chars()
        self.msg = self._chars_to_str()

    def _open_image(self):
        self.image = Image.open(self.image_path)
        self.image = self.image.convert('RGB')

    def _find_start_pixel(self):
        for i in range(0, self.image.width):
            for j in range(0, self.image.height):
                r, g, b = self.image.getpixel((i, j))
                if r == 255 and g == 0 and b == 0:
                    self.start_pixel = (i, j)
                    break
            break

    def _pull_hex_colors(self) -> list:
        colors = []
        x, y = (x + 1 for x in self.start_pixel)
        while True:
            r, g, b = self.image.getpixel((x, y))
            if r == 255 and g == 255 and b == 255:
                r, g, b = self.image.getpixel((x, y + 1))
                if r == 255 and g == 0 and b == 0:
                    break
            else:
                colors.append(f"{format(r, '02X')}{format(g, '02X')}{format(b, '02X')}")
            x += 1
            if x == self.image.width - 1:
                x = 1
                y += 1
        return colors

    def _pull_hexes(self):
        hexes = []
        for color in self.colors:
            hexes.append(color[0:2])
        return hexes
    
    def _hex_to_unicode(self) -> list:
        unicode_chars = []
        for hex in self.hexes:
            unicode_chars.append(int(hex, 16))
        return unicode_chars
    
    def _unicode_to_chars(self) -> list:
        chars = []
        for uni in self.unicode_chars:
            chars.append(chr(uni))
        return chars
    
    def _chars_to_str(self):
        str = ''
        for char in self.chars:
            str = str + char
        return str