from image import Img
from table import Table
import math


class Program:
    def __init__(self, board: Img, robot_pos, robot_angle) -> None:
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
            a = math.tan(angle_rad)
        b = self._robot_pos[1] - a * self._robot_pos[0]
        if angle == 270:
            return self._robot_pos[1] - radius
        if angle == 90:
            return self._robot_pos[1] + radius
        if angle < 90 or angle > 270:
            pass
        if angle > 90 and angle < 270:
            pass
    
    def create_lines(self):
        pass
