from interface import GUI, ConsoleInterface
from io_data import take_robot_data
from image import WrongFileError


def main():
    choice = input("Choose interface (1 for console, 2 for GUI): ")
    error = True
    if choice == "2":
        while error:
            try:
                GUI()
                error = False
            except WrongFileError:
                continue
    if choice == "1":
        error = True
        while error:
            try:
                filename = input("Enter image file name: ")
                console = ConsoleInterface(filename)
                error = False
            except WrongFileError:
                print("ERROR: File with that name not found!")
                continue
        error = True
        while error:
            try:
                data_path = input("Enter data file name: ")
                x, y, angle = take_robot_data(data_path)
                console.set_robot_pos(x, y)
                console.set_robot_angle(angle)
                console.run()
                error = False
            except WrongFileError:
                print("ERROR: File with that name not found!")
                continue


if __name__ == "__main__":
    main()
