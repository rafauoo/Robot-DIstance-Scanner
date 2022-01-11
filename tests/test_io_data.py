import testconf
from io_data import take_robot_data
from io_data import export_data
from image import WrongFileError
testconf.load()


def test_take_robot_data():
    assert take_robot_data("tests/testdata.txt") == (120, 80, 90)

def test_take_robot_data2():
    assert take_robot_data("tests/testdata2.txt") == (0, 0, 0)

def test_take_robot_data3():
    assert take_robot_data("tests/testdata3.txt") == (130, 99, 12)

def test_take_robot_data4():
    assert take_robot_data("tests/testdata4.txt") == (14, 51, 20)

def test_take_robot_data5():
    assert take_robot_data("tests/testdata5.txt") == (32, 23, 23)
