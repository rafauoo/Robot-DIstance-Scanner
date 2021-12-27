from interface import GUI, ConsoleInterface


def main():
    # filename = input("Enter file name: ")
    filename = "otoczenie.png"
    choice = input("Choose interface (1 for console, 2 for GUI): ")
    if choice == "2":
        GUI(filename)
    if choice == "1":
        console = ConsoleInterface(filename)
        while True:
            x = int(input("Enter robot position (x): "))
            y = int(input("Enter robot position (y): "))
            console.set_robot_pos(x, y)
            angle = int(input("Enter robot angle: "))
            console.set_robot_angle(angle)
            console.run()


if __name__ == "__main__":
    main()
