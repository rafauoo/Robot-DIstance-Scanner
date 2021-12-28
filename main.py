from interface import GUI, ConsoleInterface
from io_data import take_robot_data


def main():
    # filename = input("Enter image file name: ")
    filename = "otoczenie.png"
    choice = input("Choose interface (1 for console, 2 for GUI): ")
    if choice == "2":
        GUI(filename)
    if choice == "1":
        data_path = input("Enter data file name: ")
        console = ConsoleInterface(filename)
        x, y, angle = take_robot_data(data_path)
        console.set_robot_pos(x, y)
        console.set_robot_angle(angle)
        console.run()


if __name__ == "__main__":
    main()
