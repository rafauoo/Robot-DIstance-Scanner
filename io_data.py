import os.path
from image import WrongFileError


def take_robot_data(path):
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(script_dir, path), "r") as txt:
            for line in txt:
                data = line
            x, y, angle = data.split()
            return int(x), int(y), int(angle)
    except FileNotFoundError:
        raise WrongFileError


def export_data(data, path):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(script_dir, path), "w") as txt:
        for el in data:
            txt.write(str(el) + "\n")
