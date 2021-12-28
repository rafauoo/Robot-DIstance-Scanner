import testconf
import config as CFG
from image import Img
testconf.load()

black = CFG.wall_colour
white = CFG.background_colour


def test_image_init():
    img = Img("tests/test2.png")
    assert img.pixel_values().table() == [[white, black, white],
                                          [black, white, black],
                                          [white, black, white]]
    assert img.width() == 3
    assert img.height() == 3


def test_image_init_2():
    img = Img("tests/test3.png")
    assert img.pixel_values().table() == [[white, black, white],
                                          [white, white, white],
                                          [white, black, white]]
    assert img.width() == 3
    assert img.height() == 3


def test_image_init_3():
    img = Img("tests/test4.png")
    assert img.pixel_values().table() == [[black, black, white],
                                          [black, white, black],
                                          [black, black, white]]
    assert img.width() == 3
    assert img.height() == 3
