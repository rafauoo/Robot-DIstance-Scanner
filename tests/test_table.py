import testconf
import config as CFG
from table import Table
from point import Point
testconf.load()


def test_table_create():
    table = Table(3, 3)
    bg = CFG.background_colour
    assert table.size_x() == 3
    assert table.size_y() == 3
    assert table.table() == [[bg, bg, bg],
                             [bg, bg, bg],
                             [bg, bg, bg]]


def test_table_modify():
    table = Table(3, 3)
    bg = CFG.background_colour
    assert table.size_x() == 3
    assert table.size_y() == 3
    assert table.table() == [[bg, bg, bg],
                             [bg, bg, bg],
                             [bg, bg, bg]]
    point = Point(2, 2)
    blue = (0, 0, 255)
    table.modify(point, blue)
    assert table.table() == [[bg, bg, bg],
                             [bg, bg, bg],
                             [bg, bg, blue]]


def test_table_value():
    table = Table(3, 3)
    bg = CFG.background_colour
    assert table.size_x() == 3
    assert table.size_y() == 3
    assert table.table() == [[bg, bg, bg],
                             [bg, bg, bg],
                             [bg, bg, bg]]
    point = Point(2, 2)
    blue = (0, 0, 255)
    table.modify(point, blue)
    assert table.table() == [[bg, bg, bg],
                             [bg, bg, bg],
                             [bg, bg, blue]]
    assert table.value(point) == blue


def test_table_bresenham():
    table = Table(8, 8)
    bg = CFG.background_colour
    assert table.table() == [[bg, bg, bg, bg, bg, bg, bg, bg],
                             [bg, bg, bg, bg, bg, bg, bg, bg],
                             [bg, bg, bg, bg, bg, bg, bg, bg],
                             [bg, bg, bg, bg, bg, bg, bg, bg],
                             [bg, bg, bg, bg, bg, bg, bg, bg],
                             [bg, bg, bg, bg, bg, bg, bg, bg],
                             [bg, bg, bg, bg, bg, bg, bg, bg],
                             [bg, bg, bg, bg, bg, bg, bg, bg]]
    point1 = Point(0, 0)
    point2 = Point(6, 5)
    OO = (0, 0, 255)
    last_pt = table.bresenham(point1, point2, OO)
    assert last_pt.x() == -1
    assert table.table() == [[OO, bg, bg, bg, bg, bg, bg, bg],
                             [bg, OO, bg, bg, bg, bg, bg, bg],
                             [bg, bg, OO, OO, bg, bg, bg, bg],
                             [bg, bg, bg, bg, OO, bg, bg, bg],
                             [bg, bg, bg, bg, bg, OO, bg, bg],
                             [bg, bg, bg, bg, bg, bg, OO, bg],
                             [bg, bg, bg, bg, bg, bg, bg, bg],
                             [bg, bg, bg, bg, bg, bg, bg, bg]]


def test_table_bresenham_2():
    table = Table(8, 8)
    bg = CFG.background_colour
    assert table.table() == [[bg, bg, bg, bg, bg, bg, bg, bg],
                             [bg, bg, bg, bg, bg, bg, bg, bg],
                             [bg, bg, bg, bg, bg, bg, bg, bg],
                             [bg, bg, bg, bg, bg, bg, bg, bg],
                             [bg, bg, bg, bg, bg, bg, bg, bg],
                             [bg, bg, bg, bg, bg, bg, bg, bg],
                             [bg, bg, bg, bg, bg, bg, bg, bg],
                             [bg, bg, bg, bg, bg, bg, bg, bg]]
    point1 = Point(4, 3)
    point2 = Point(1, 0)
    OO = (0, 0, 255)
    last_pt = table.bresenham(point1, point2, OO)
    assert last_pt.x() == -1
    assert table.table() == [[bg, OO, bg, bg, bg, bg, bg, bg],
                             [bg, bg, OO, bg, bg, bg, bg, bg],
                             [bg, bg, bg, OO, bg, bg, bg, bg],
                             [bg, bg, bg, bg, OO, bg, bg, bg],
                             [bg, bg, bg, bg, bg, bg, bg, bg],
                             [bg, bg, bg, bg, bg, bg, bg, bg],
                             [bg, bg, bg, bg, bg, bg, bg, bg],
                             [bg, bg, bg, bg, bg, bg, bg, bg]]


def test_table_bresenham_3():
    table = Table(8, 8)
    bg = CFG.background_colour
    assert table.table() == [[bg, bg, bg, bg, bg, bg, bg, bg],
                             [bg, bg, bg, bg, bg, bg, bg, bg],
                             [bg, bg, bg, bg, bg, bg, bg, bg],
                             [bg, bg, bg, bg, bg, bg, bg, bg],
                             [bg, bg, bg, bg, bg, bg, bg, bg],
                             [bg, bg, bg, bg, bg, bg, bg, bg],
                             [bg, bg, bg, bg, bg, bg, bg, bg],
                             [bg, bg, bg, bg, bg, bg, bg, bg]]
    point1 = Point(6, 0)
    point2 = Point(0, 3)
    OO = (0, 0, 255)
    last_pt = table.bresenham(point1, point2, OO)
    assert last_pt.x() == -1
    assert table.table() == [[bg, bg, bg, bg, bg, OO, OO, bg],
                             [bg, bg, bg, OO, OO, bg, bg, bg],
                             [bg, OO, OO, bg, bg, bg, bg, bg],
                             [OO, bg, bg, bg, bg, bg, bg, bg],
                             [bg, bg, bg, bg, bg, bg, bg, bg],
                             [bg, bg, bg, bg, bg, bg, bg, bg],
                             [bg, bg, bg, bg, bg, bg, bg, bg],
                             [bg, bg, bg, bg, bg, bg, bg, bg]]


def test_table_bresenham_wall():
    table = Table(8, 8)
    bg = CFG.background_colour
    WA = CFG.wall_colour
    for y in range(0, 8):
        table.modify(Point(4, y), WA)
    assert table.table() == [[bg, bg, bg, bg, WA, bg, bg, bg],
                             [bg, bg, bg, bg, WA, bg, bg, bg],
                             [bg, bg, bg, bg, WA, bg, bg, bg],
                             [bg, bg, bg, bg, WA, bg, bg, bg],
                             [bg, bg, bg, bg, WA, bg, bg, bg],
                             [bg, bg, bg, bg, WA, bg, bg, bg],
                             [bg, bg, bg, bg, WA, bg, bg, bg],
                             [bg, bg, bg, bg, WA, bg, bg, bg]]
    point1 = Point(0, 0)
    point2 = Point(6, 5)
    OO = (0, 0, 255)
    last_pt = table.bresenham(point1, point2, OO)
    assert last_pt.x() == 3
    assert last_pt.y() == 2
    assert table.table() == [[OO, bg, bg, bg, WA, bg, bg, bg],
                             [bg, OO, bg, bg, WA, bg, bg, bg],
                             [bg, bg, OO, OO, WA, bg, bg, bg],
                             [bg, bg, bg, bg, WA, bg, bg, bg],
                             [bg, bg, bg, bg, WA, bg, bg, bg],
                             [bg, bg, bg, bg, WA, bg, bg, bg],
                             [bg, bg, bg, bg, WA, bg, bg, bg],
                             [bg, bg, bg, bg, WA, bg, bg, bg]]
