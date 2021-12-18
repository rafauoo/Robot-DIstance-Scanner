from table import Table
from image import Img
from point import Point


def main():
    table = Table(15, 15)
    print("\n")
    table.bresenham(Point(3, 2), Point(6, 13), 200)
    table.print_table()
    img = Img("testowy.png")
    img.print_pixel_values()


if __name__ == "__main__":
    main()
