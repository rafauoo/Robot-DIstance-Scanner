from table import Table
from image import Img


def main():
    table = Table(15, 15)
    print("\n")
    table.bresenham((3, 2), (6, 13))
    table.print_table()
    img = Img("testowy.png")
    img.print_pixel_values()


if __name__ == "__main__":
    main()
