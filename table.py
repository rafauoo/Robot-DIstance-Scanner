class Table:
    def __init__(self, size_x, size_y) -> None:
        self._size_x = size_x
        self._size_y = size_y
        self._table = self.create_table(size_x, size_y)

    def create_table(self, size_x, size_y):
        table = []
        for y in range(size_y):
            table.append([])
            for x in range(size_x):
                table[y].append(0)
        return table

    def print_table(self):
        for row in self._table:
            line = ""
            for el in row:
                format_el = f"{el:03} "
                line += format_el
            print(line)

    def modify(self, point, value):
        x, y = point
        self._table[y][x] = value

    def bresenham(self, point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        dx = x2 - x1
        dy = y2 - y1
        x_step = 1 if dx >= 0 else -1
        y_step = 1 if dy >= 0 else -1
        dx = abs(dx)
        dy = abs(dy)
        self.modify((x1, y1), 211)
        if dx > dy:
            e = dx / 2
            while x1 != x2 or y1 != y2:
                x1 += x_step
                e -= dy
                if e < 0:
                    y1 += y_step
                    e += dx
                self.modify((x1, y1), 211)
        else:
            e = dy / 2
            while x1 != x2 or y1 != y2:
                y1 += y_step
                e -= dx
                if e < 0:
                    x1 += x_step
                    e += dy
                self.modify((x1, y1), 211)

    def value(self, point):
        x, y = point
        return self._table[y][x]
