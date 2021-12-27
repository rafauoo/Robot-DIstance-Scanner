import testconf
from point import Point
import pytest
testconf.load()


def test_point_init():
    point = Point(10, 10)
    assert point.x() == 10
    assert point.y() == 10


def test_point_distance():
    point = Point(10, 10)
    point2 = Point(13, 14)
    assert point.distance(point2) == 5


def test_point_distance_float():
    point = Point(10, 10)
    point2 = Point(17, 14)
    assert point.distance(point2) == pytest.approx(8.0622577)
