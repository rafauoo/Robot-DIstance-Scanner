from PIL import Image
from table import Table
import os.path


class Img:
    def __init__(self, path) -> None:
        self._path = path
        self._pixel_values_R = self.get_pixel_values(0)
        self._pixel_values_G = self.get_pixel_values(1)
        self._pixel_values_B = self.get_pixel_values(2)

    def path(self):
        return self._path

    def get_pixel_values(self, rgb):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        img = Image.open(os.path.join(script_dir, self._path))
        imgWidth, imgHeight = img.size
        img = img.convert("RGB")
        imgdata = img.getdata()
        table = Table(imgWidth, imgHeight)
        x = 0
        y = 0
        for pixel in imgdata:
            table.modify((x, y), pixel[rgb])
            if x == imgWidth - 1:
                x = 0
                y += 1
            else:
                x += 1
        return table

    def pixel_values_R(self):
        return self._pixel_values_R

    def pixel_values_G(self):
        return self._pixel_values_G

    def pixel_values_B(self):
        return self._pixel_values_B

    def print_pixel_values(self):
        r = self.pixel_values_R()
        g = self.pixel_values_G()
        b = self.pixel_values_B()
        r.print_table()
        print("\n")
        g.print_table()
        print("\n")
        b.print_table()
        print("\n")
