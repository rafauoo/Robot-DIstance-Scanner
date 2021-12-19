from gui import GUI


def main():
    GUI("otoczenie.png")
    # global root
    # global label
    # root = tk.Tk()
    # photo = tk.PhotoImage(file="otoczenie.png")
    # label = tk.Label(root, image=photo)
    # label.pack()
    # root.bind("<Button-1>", onclick)
    # root.mainloop()

# def onclick(e):
#     x = e.x
#     y = e.y
#     global root
#     global label
#     robot_angle = askinteger("Input", "Input robot angle")
#     image = Img("otoczenie.png")
#     program = Program(image, Point(x, y), robot_angle)
#     rgb = (255, 2, 2)
#     # fov = askinteger("Input", "Input robot's FOV")
#     # angle_diff = askinteger("Input", "Input angle diff")
#     # radius = askinteger("Input", "Input laser radius")
#     fov = 90
#     angle_diff = 10
#     radius = 60
#     program.create_lines(fov, angle_diff, radius, rgb)
#     image.export("wynik")
#     photo = tk.PhotoImage(file="wynik.png")
#     label.configure(image=photo)
#     label.image = photo


if __name__ == "__main__":
    main()
