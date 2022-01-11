import testconf
import config as CFG
from program import Program
from image import Img
from point import Point
testconf.load()


def test_program_init():
    img = Img("tests/test.png")
    robot_pos = Point(1, 5)
    program = Program(img, robot_pos, 0)
    assert program.board() == img
    assert program.robot_pos().x() == 1
    assert program.robot_pos().y() == 5
    assert program.robot_angle() == 0


def test_program_check_angle():
    img = Img("tests/test.png")
    robot_pos = Point(1, 5)
    program = Program(img, robot_pos, 0)
    assert program.board() == img
    assert program.robot_pos().x() == 1
    assert program.robot_pos().y() == 5
    assert program.robot_angle() == 0
    assert program.check_angle(50) == 50


def test_program_check_angle_negative():
    img = Img("tests/test.png")
    robot_pos = Point(1, 5)
    program = Program(img, robot_pos, 0)
    assert program.board() == img
    assert program.robot_pos().x() == 1
    assert program.robot_pos().y() == 5
    assert program.robot_angle() == 0
    assert program.check_angle(-50) == 310


def test_program_check_angle_over360():
    img = Img("tests/test.png")
    robot_pos = Point(1, 5)
    program = Program(img, robot_pos, 0)
    assert program.board() == img
    assert program.robot_pos().x() == 1
    assert program.robot_pos().y() == 5
    assert program.robot_angle() == 0
    assert program.check_angle(380) == 20


def test_program_calculate_point_function_x_RIGHT():
    img = Img("tests/test.png")
    robot_pos = Point(5, 5)
    program = Program(img, robot_pos, 0)
    point = program.calculate_point_function(5, 1, 1, 0)
    # y = x
    assert point.x() == 8
    assert point.y() == 8


def test_program_calculate_point_function_2x_plus_1_RIGHT():
    img = Img("tests/test.png")
    robot_pos = Point(3, 7)
    program = Program(img, robot_pos, 0)
    point = program.calculate_point_function(5, 1, 2, 1)
    # y = 2x + 1
    assert point.x() == 5
    assert point.y() == 11


def test_program_calculate_point_function_x_LEFT():
    img = Img("tests/test.png")
    robot_pos = Point(5, 5)
    program = Program(img, robot_pos, 0)
    point = program.calculate_point_function(5, -1, 1, 0)
    # y = x
    assert point.x() == 2
    assert point.y() == 2


def test_program_calculate_point_function_2x_plus_1_LEFT():
    img = Img("tests/test.png")
    robot_pos = Point(3, 7)
    program = Program(img, robot_pos, 0)
    point = program.calculate_point_function(5, -1, 2, 1)
    # y = 2x + 1
    assert point.x() == 1
    assert point.y() == 3


def test_program_calculate_point_for_angle_0():
    img = Img("tests/test.png")
    robot_pos = Point(1, 10)
    program = Program(img, robot_pos, 0)
    assert program.robot_angle() == 0
    point = program.calculate_point_for_angle(0, 5)
    assert point.x() == 6
    assert point.y() == 10


def test_program_calculate_point_for_angle_90():
    img = Img("tests/test.png")
    robot_pos = Point(1, 10)
    program = Program(img, robot_pos, 0)
    assert program.robot_angle() == 0
    point = program.calculate_point_for_angle(90, 5)
    assert point.x() == 1
    assert point.y() == 5


def test_program_calculate_point_for_angle_180():
    img = Img("tests/test.png")
    robot_pos = Point(10, 10)
    program = Program(img, robot_pos, 0)
    assert program.robot_angle() == 0
    point = program.calculate_point_for_angle(180, 5)
    assert point.x() == 5
    assert point.y() == 10


def test_program_calculate_point_for_angle_270():
    img = Img("tests/test.png")
    robot_pos = Point(10, 10)
    program = Program(img, robot_pos, 0)
    assert program.robot_angle() == 0
    point = program.calculate_point_for_angle(270, 5)
    assert point.x() == 10
    assert point.y() == 15


def test_program_calculate_point_for_angle_over360():
    img = Img("tests/test.png")
    robot_pos = Point(1, 10)
    program = Program(img, robot_pos, 0)
    assert program.robot_angle() == 0
    point = program.calculate_point_for_angle(450, 5)
    assert point.x() == 1
    assert point.y() == 5


def test_program_calculate_point_for_angle_negative():
    img = Img("tests/test.png")
    robot_pos = Point(1, 10)
    program = Program(img, robot_pos, 0)
    assert program.robot_angle() == 0
    point = program.calculate_point_for_angle(-90, 5)
    assert point.x() == 1
    assert point.y() == 15


def test_program_calculate_point_for_angle_315():
    img = Img("tests/test.png")
    robot_pos = Point(10, 10)
    program = Program(img, robot_pos, 0)
    assert program.robot_angle() == 0
    point = program.calculate_point_for_angle(315, 5)
    assert point.x() == 13
    assert point.y() == 13


def test_program_calculate_point_for_angle_45():
    img = Img("tests/test.png")
    robot_pos = Point(10, 10)
    program = Program(img, robot_pos, 0)
    assert program.robot_angle() == 0
    point = program.calculate_point_for_angle(45, 5)
    assert point.x() == 13
    assert point.y() == 7


fov = 90
angle_diff = 45
radius = 5
line_colour = CFG.line_colour


def test_program_create_lines_distances():
    img = Img("tests/test.png")
    robot_pos = Point(5, 18)
    program = Program(img, robot_pos, 0)
    list = program.create_lines(fov, angle_diff, radius, line_colour)
    assert list == [2, 3, 255, 255, 255]
