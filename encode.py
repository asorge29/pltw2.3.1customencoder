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

        self._draw_msg()
        self._take_screenshot(self.window)
        self.window.bye()
        
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
    
    def _calculate_length(self):
        self.colors_len = len(self.colors)
        
    def _draw_msg(self):
        self._setup_turtle()
        for color in self.colors:
            self.drawer.color(color)
            self.drawer.stamp()
            self.drawer.forward(20)
            if self.drawer.xcor() > 400:
                self.drawer.goto(-400, self.drawer.ycor()-20)
        self.drawer.ht()
        self.window.update()


    def _setup_turtle(self):
        self.drawer = trtl.Turtle()
        self.window = trtl.Screen()
        self.window.title("Encoder")
        self.window.tracer(0)
        self.window.setup(width=1000, height=1000)
        self.drawer.penup()
        self.drawer.shape("square")
        self.drawer.goto(-420, 420)
        self.drawer.color("red")
        self.drawer.stamp()
        self.drawer.forward(20)
        self.drawer.right(90)
        self.drawer.forward(20)
        self.drawer.left(90)

    def _take_screenshot(self, screen):
        with mss.mss() as sct:
            output_number = 0
            while True:
                try:
                    sct.shot(mon=1,output=f'{self.output_dir}/encoder_output{output_number}.gif')
                    output_path = f'{self.output_dir}/encoder_output{output_number}.gif'
                    break
                except OSError:
                    output_number += 1
        root = trtl.getcanvas().winfo_toplevel()
        x=root.winfo_rootx()
        y=root.winfo_rooty()
        x1 = x + self.window.window_width()
        y1 = y + self.window.window_height()

        image = Image.open(output_path)
        bounds = x,y,x1,y1
        if platform.system() == "Darwin":
            bounds = 2*x,2*y,2*x1,2*y1
        image = image.crop(bounds)
        image.save(output_path)

    def _test_format(self):
        tester = trtl.Turtle()
        tester.penup()
        tester.goto(-420, 420)
        tester.color("white")
        tester.shape("circle")
        tester.shapesize(0.5)
        tester.stamp()
        tester.goto(tester.xcor()+20, tester.ycor()-20)
        for i in range(200):
            tester.stamp()
            tester.forward(20)
            if tester.xcor() > 400:
                tester.goto(-400, tester.ycor()-20)