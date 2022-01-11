from image import Img
from point import Point
import math


class Program:
    def __init__(self, board: Img, robot_pos: Point, robot_angle) -> None:
        "creates instance of Program"
        self._board = board
        self._robot_pos = robot_pos
        self._robot_angle = robot_angle
        self._distances = []

    def board(self):
        return self._board

    def robot_pos(self):
        return self._robot_pos

    def robot_angle(self):
        return self._robot_angle

    def check_angle(self, angle_diff):
        "sets angle in [0-360) range"
        angle = self._robot_angle + angle_diff
        if angle < 0:
            angle += 360
        if angle >= 360:
            angle -= 360
        return angle

    def calculate_point_for_angle(self, angle_diff, radius):
        """
        calculates point B for Bresenham
        using angle (y=ax+b, a=tg(angle))
        """
        angle = self.check_angle(angle_diff)
        angle_rad = angle / 180 * math.pi
        a = 0
        if angle != 90 and angle != 270:
            a = math.tan(angle_rad) * -1
        b = self._robot_pos.y() - a * self._robot_pos.x()
        if angle == 270:
            return Point(self._robot_pos.x(), self._robot_pos.y() + radius)
        if angle == 90:
            return Point(self._robot_pos.x(), self._robot_pos.y() - radius)
        if angle < 90 or angle > 270:
            diff = 1
        if angle > 90 and angle < 270:
            diff = -1
        return self.calculate_point_function(radius, diff, a, b)

    def calculate_point_function(self, radius, diff, a, b):
        """
        diff can be 1 or -1,
        calculates point B for Bresenham
        using function (y=ax+b)
        """
        distance = 0
        x = self._robot_pos.x()
        y = self._robot_pos.y()
        last_x, last_y = (x, y)
        while distance <= radius:
            last_x = x
            last_y = y
            x += diff
            y = a * x + b
            y = round(y)
            distance = self._robot_pos.distance(Point(x, y))
        x = last_x
        y = last_y
        return Point(x, y)

    def create_lines(self, fov, step, radius, rgb):
        "creates multiple lines with bresenham"
        distances = []
        for angle_diff in range(0, fov*2 + 1, step):
            angle_diff -= fov
            pt2 = self.calculate_point_for_angle(angle_diff, radius)
            rob_pos = self._robot_pos
            last_pt = self._board.pixel_values().bresenham(rob_pos, pt2, rgb)
            if last_pt.x() == -1:
                distances.append(255)
            else:
                distances.append(round(rob_pos.distance(last_pt)))
        self._distances = distances
        return self._distances

    def distances(self):
        return self._distances
