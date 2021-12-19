from image import Img
from table import Table
from point import Point
import math


class Program:
    def __init__(self, board: Img, robot_pos: Point, robot_angle) -> None:
        self._board = board
        self._robot_pos = robot_pos
        self._robot_angle = robot_angle

    def calculate_angle_point(self, angle_diff, radius):
        angle = self._robot_angle + angle_diff
        if angle < 0:
            angle += 360
        if angle >= 360:
            angle -= 360
        angle_rad = angle / 180 * math.pi
        a = 0
        if angle != 90 and angle != 270:
            a = math.tan(angle_rad) * -1
        b = self._robot_pos.y() - a * self._robot_pos.x()
        if angle == 270:
            ret_y = self._robot_pos.y() + radius if self._robot_pos.y() + radius <= self._board.height() else 0
            return Point(self._robot_pos.x(), ret_y)
        if angle == 90:
            ret_y = self._robot_pos.y() - radius if self._robot_pos.y() - radius >= 0 else 0
            return Point(self._robot_pos.x(), ret_y)
        if angle < 90 or angle > 270:
            diff = 1
        if angle > 90 and angle < 270:
            diff = -1
        distance = 0
        x = self._robot_pos.x()
        y = self._robot_pos.y()
        last_x, last_y = (0, 0)
        while distance < radius:
            last_distance = distance
            last_x = x
            last_y = y
            x += diff
            y = a * x + b
            y = round(y)
            distance = self._robot_pos.distance(Point(x, y))
        if abs(last_distance - radius) < abs(distance - radius):
            x = last_x
            y = last_y
        if x < 0:
            x = 0
        if y < 0:
            y = 0
        if y > self._board.height():
            y = self._board.height()
        if x > self._board.width():
            x = self._board.width()
        return Point(x, y)

    def create_lines(self, plusminus, step, radius, rgb):
        r, g, b = rgb
        for angle_diff in range(0, plusminus*2 + 1, step):
            angle_diff -= plusminus
            point2 = self.calculate_angle_point(angle_diff, radius)
            self._board.pixel_values_R().bresenham(self._robot_pos, point2, r)
        for angle_diff in range(0, plusminus*2 + 1, step):
            angle_diff -= plusminus
            point2 = self.calculate_angle_point(angle_diff, radius)
            self._board.pixel_values_G().bresenham(self._robot_pos, point2, g)
        for angle_diff in range(0, plusminus*2 + 1, step):
            angle_diff -= plusminus
            point2 = self.calculate_angle_point(angle_diff, radius)
            self._board.pixel_values_B().bresenham(self._robot_pos, point2, b)
