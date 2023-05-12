class polygon():
    """
    This class polygon
    """

    def __init__(self, number_of_sides) -> None:
        self.sides = number_of_sides


class rectangle (polygon):
    """
    This class polygon
    """

    def __init__(self, hight, widht) -> None:
        super().__init__(self)
        self.hight = hight
        self.widht = widht

    def area(self):
        return self.hight * self.widht


if __name__ == '__main__':
    rec = rectangle(4, 5)
    print(rec.area())
