from table import Table
from image import Img
from point import Point
from program import Program


def main():
    image = Img("otoczenie.png")
    program = Program(image, Point(130, 86), 35)
    rgb = (255, 2, 2)
    program.create_lines(90, 10, 60, rgb)
    image.export("wynik")


if __name__ == "__main__":
    main()
