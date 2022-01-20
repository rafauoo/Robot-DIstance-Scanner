import tkinter as tk
from tkinter import filedialog as fd
from tkinter.simpledialog import askinteger
from image import Img, WrongFileError
from point import Point
import config as CFG
from program import Program
from io_data import export_data


class GUI:
    def __init__(self) -> None:
        "creates GUI"
        self._root = tk.Tk()
        filetypes = (
            ('Image files', '*.png'),
            ('All files', '*.*')
        )
        self._path = fd.askopenfilename(title="Open image",
                                        filetypes=filetypes)
        try:
            self._photo = tk.PhotoImage(file=self._path)
        except tk.TclError:
            self._root.destroy()
            raise WrongFileError
        self._label = tk.Label(self._root, image=self._photo)
        self._label.pack()
        self._root.bind("<Button-1>", self.onclick)
        self._root.mainloop()

    def onclick(self, e):
        "runs whole program while LMB on image"
        x = e.x
        y = e.y
        robot_angle = askinteger("Input", "Input robot angle")
        image = Img(self._path)
        program = Program(image, Point(x, y), robot_angle)
        rgb = CFG.line_colour
        fov = CFG.fov
        angle_diff = CFG.angle_diff
        radius = CFG.radius
        line_len = program.create_lines(fov, angle_diff, radius, rgb)
        export_data(reversed(line_len), "wyniki.txt")
        image.export("symulacja")
        photo = tk.PhotoImage(file="symulacja.png")
        self._label.configure(image=photo)
        self._label.image = photo


class ConsoleInterface:
    def __init__(self, img_path) -> None:
        "creates console interface"
        self._img_path = img_path
        self._robot_pos = Point(0, 0)
        self._robot_angle = 0
        self._image = Img(self._img_path)

    def set_robot_pos(self, x, y):
        point = Point(x, y)
        self._robot_pos = point

    def set_robot_angle(self, angle):
        self._robot_angle = angle

    def run(self):
        "runs whole program"
        program = Program(self._image, self._robot_pos, self._robot_angle)
        rgb = CFG.line_colour
        fov = CFG.fov
        angle_diff = CFG.angle_diff
        radius = CFG.radius
        line_len = program.create_lines(fov, angle_diff, radius, rgb)
        export_data(reversed(line_len), "wyniki.txt")
        self._image.export("symulacja")
