from point import Point
import config as CFG


def swap(a, b):
    c = a
    a = b
    b = c
    return a, b


class Table:
    def __init__(self, size_x, size_y) -> None:
        "creates instance of table"
        self._size_x = size_x
        self._size_y = size_y
        self._table = self.create_table(size_x, size_y)

    def size_x(self):
        return self._size_x

    def size_y(self):
        return self._size_y

    def table(self):
        return self._table

    def create_table(self, size_x, size_y):
        "creating empty table"
        table = []
        background_color = CFG.background_colour
        for y in range(size_y):
            table.append([])
            for x in range(size_x):
                table[y].append(background_color)
        return table

    def print_table(self):
        for row in self._table:
            line = ""
            for el in row:
                format_el = f"{el:03} "
                line += format_el
            print(line)

    def modify(self, point: Point, value):
        x = point.x()
        y = point.y()
        self._table[y][x] = value

    def bresenham(self, point1: Point, point2: Point, value):
        """
        heart of whole project,
        it draws a line from point1 to point2
        with colour given by value (RGB)
        """
        x1 = point1.x()
        y1 = point1.y()
        x2 = point2.x()
        y2 = point2.y()
        dx = x2 - x1
        dy = y2 - y1
        x_step = 1 if dx >= 0 else -1
        y_step = 1 if dy >= 0 else -1
        dx = abs(dx)
        dy = abs(dy)
        self.modify(Point(x1, y1), value)
        if dx > dy:
            e = dx / 2
            while x1 != x2 or y1 != y2:
                last_pt = Point(x1, y1)
                x1 += x_step
                if x1 >= self.size_x() or x1 < 0:
                    return last_pt
                e -= dy
                if e < 0:
                    y1 += y_step
                    if y1 >= self.size_y() or y1 < 0:
                        return last_pt
                    if self.value(Point(x1 - x_step, y1)) == CFG.wall_colour:
                        return last_pt
                    if self.value(Point(x1, y1 - y_step)) == CFG.wall_colour:
                        return last_pt
                    e += dx
                if self.value(Point(x1, y1)) == CFG.wall_colour:
                    return last_pt
                self.modify(Point(x1, y1), value)
            return Point(-1, -1)
        else:
            e = dy / 2
            while x1 != x2 or y1 != y2:
                last_pt = Point(x1, y1)
                y1 += y_step
                if y1 >= self.size_y() or y1 < 0:
                    return last_pt
                e -= dx
                if e < 0:
                    x1 += x_step
                    if x1 >= self.size_x() or x1 < 0:
                        return last_pt
                    if self.value(Point(x1 - x_step, y1)) == CFG.wall_colour:
                        return last_pt
                    if self.value(Point(x1, y1 - y_step)) == CFG.wall_colour:
                        return last_pt
                    e += dy
                if self.value(Point(x1, y1)) == CFG.wall_colour:
                    return last_pt
                self.modify(Point(x1, y1), value)
            return Point(-1, -1)

    def value(self, point):
        x = point.x()
        y = point.y()
        return self._table[y][x]
