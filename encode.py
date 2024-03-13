import turtle as trtl
import mss
import platform
from PIL import Image
from os import path

class Encoder():
    def __init__(self):
        self.input = ""
        self.input_len = len(self.input)
        self.unicode_chars = []
        self.hexes = []
        self.colors = []
        self.colors_len = len(self.colors)
        self.output_dir = path.expanduser("~/Documents")
        
    def encode(self, input, output_dir, suffix=65280):
        self.input = input
        self.input_len = len(self.input)
        if output_dir != '':
            self.output_dir = output_dir
        self.suffix = hex(suffix)[2:6]
        while len(self.suffix) < 4:
            self.suffix = "0" + self.suffix
        self.unicode_chars = self._chars_to_unicode(self.input)
        self.hexes = self._ints_to_hex(self.unicode_chars)
        self.colors = self._hexes_to_colors(self.hexes)

        self._generate_image()
        
    def _chars_to_unicode(self, msg) -> list:
        unicode_chars = []
        for char in msg:
            unicode_chars.append(ord(char))
        return unicode_chars
    
    def _ints_to_hex(self, ints:list) -> list:
        hexes = []
        for i in range(0, len(ints)):
            hexes.append(hex(ints[i]))
        return hexes
    
    def _hexes_to_colors(self, hexes:list) -> list:
        colors = []
        for hex in hexes:
            colors.append(f'{hex.replace("0x", "#")}{self.suffix}')
        return colors
    
    def _calculate_pixel_length(self) -> int:
        self.colors_len = len(self.colors)
        return self.colors_len
        
    def _generate_image(self) -> Image:
        pixels = self._calculate_pixel_length()
        rows = pixels // 98 + 3
        cols = 100
        image = Image.new('RGB', (cols, rows), (255, 255, 255))
        image.putpixel((0, 0), (255, 0, 0))
        x, y = 1, 1
        for color in self.colors:
            image.putpixel((x, y), self._hex_to_rgb(color))
            x += 1
            if x == cols-1:
                x = 1
                y += 1
        y += 1
        image.putpixel((x, y), (255, 0, 0))

        image.save(f'{self.output_dir}/encoder_output.gif')

    def _hex_to_rgb(self, hex) -> tuple:
        hex = hex.lstrip('#')
        r, g, b = hex[0:2], hex[2:4], hex[4:6]
        return (int(r, 16), int(g, 16), int(b, 16))