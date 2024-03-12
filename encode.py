import turtle as trtl

class Encoder():
    def __init__(self):
        self.input = ""
        self.unicode_chars = []
        self.hexes = []
        self.colors = []
        self.output_dir = ""
        
    def encode(self, input, output_dir, suffix='ff00'):
        self.input = input
        self.output_dir = output_dir
        self.suffix = suffix
        self.unicode_chars = self._chars_to_unicode(self.input)
        self.hexes = self._ints_to_hex(self.unicode_chars)
        self.colors = self._hexes_to_colors(self.hexes)

        print(self.unicode_chars)
        print(self.hexes)
        print(self.colors)
        
    def _chars_to_unicode(self, msg):
        unicode_chars = []
        for char in msg:
            unicode_chars.append(ord(char))
        return unicode_chars
    
    def _ints_to_hex(self, ints:list):
        hexes = []
        for i in range(0, len(ints)):
            hexes.append(hex(ints[i]))
        return hexes
    
    def _hexes_to_colors(self, hexes:list):
        colors = []
        for hex in hexes:
            colors.append(f'{hex.replace("0x", "#")}{self.suffix}')
        return colors