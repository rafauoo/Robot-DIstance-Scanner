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
