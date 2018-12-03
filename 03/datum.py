from collections import namedtuple

DataBase = namedtuple('Data', ('id', 'left', 'bottom', 'width', 'height'))

class Datum(DataBase):
    @property
    def top(self):
        return self.bottom + self.height - 1

    @property
    def right(self):
        return self.left + self.width - 1


