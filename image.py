from PIL import Image
from table import Table
import os.path
from point import Point


class WrongFileError(Exception):
    pass


class Img:
    def __init__(self, path) -> None:
        self._path = path
        self._handle = None
        self._width = 0
        self._height = 0
        self._pixel_values = self.get_pixel_values()

    def path(self):
        return self._path

    def height(self):
        return self._height

    def width(self):
        return self._width

    def handle(self):
        return self._handle

    def get_pixel_values(self):
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            img = Image.open(os.path.join(script_dir, self._path))
        except FileNotFoundError:
            raise WrongFileError
        self._handle = img
        imgWidth, imgHeight = img.size
        self._width = imgWidth
        self._height = imgHeight
        img = img.convert("RGB")
        imgdata = img.getdata()
        table = Table(imgWidth, imgHeight)
        x = 0
        y = 0
        for pixel in imgdata:
            table.modify(Point(x, y), (pixel[0], pixel[1], pixel[2]))
            if x == imgWidth - 1:
                x = 0
                y += 1
            else:
                x += 1
        return table

    def pixel_values(self):
        return self._pixel_values

    def print_pixel_values(self):
        rgb = self.pixel_values()
        rgb.print_table()

    def export(self, name):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        img = Image.open(os.path.join(script_dir, self._path))
        img = img.convert("RGB")
        pixel_map = img.load()
        for y in range(self._height):
            for x in range(self._width):
                r, g, b = self.pixel_values().value(Point(x, y))
                pixel_map[x, y] = r, g, b
        img.save(f"{name}.png", format="png")
