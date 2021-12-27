import tkinter as tk
from tkinter.simpledialog import askinteger
from image import Img
from point import Point
import config as CFG
from program import Program


class GUI:
    def __init__(self, path) -> None:
        self._path = path
        self._root = tk.Tk()
        self._photo = tk.PhotoImage(file=path)
        self._label = tk.Label(self._root, image=self._photo)
        self._label.pack()
        self._root.bind("<Button-1>", self.onclick)
        self._root.mainloop()

    def onclick(self, e):
        x = e.x
        y = e.y
        robot_angle = askinteger("Input", "Input robot angle")
        image = Img(self._path)
        program = Program(image, Point(x, y), robot_angle)
        rgb = CFG.line_colour
        # fov = askinteger("Input", "Input robot's FOV")
        # angle_diff = askinteger("Input", "Input angle diff")
        # radius = askinteger("Input", "Input laser radius")
        fov = CFG.fov
        angle_diff = CFG.angle_diff
        radius = CFG.radius
        program.create_lines(fov, angle_diff, radius, rgb)
        image.export("wynik")
        photo = tk.PhotoImage(file="wynik.png")
        self._label.configure(image=photo)
        self._label.image = photo


class ConsoleInterface:
    def __init__(self, path) -> None:
        self._path = path
        self._robot_pos = Point(0, 0)
        self._robot_angle = 0

    def set_robot_pos(self, x, y):
        point = Point(x, y)
        self._robot_pos = point

    def set_robot_angle(self, angle):
        self._robot_angle = angle

    def run(self):
        image = Img(self._path)
        program = Program(image, self._robot_pos, self._robot_angle)
        rgb = (255, 0, 0)
        fov = 90
        angle_diff = 10
        radius = 60
        program.create_lines(fov, angle_diff, radius, rgb)
        image.export("wynik")
