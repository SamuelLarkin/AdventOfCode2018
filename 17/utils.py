import re

class Clay:
    def __init__(self, x, y, v):
        self.x = x
        self.y = y
        self.v = v


    @property
    def p(self):
        return (self.x, self.y)


    def __repr__(self):
        return 'Clay(position: {p}, value: {v})'.format(p=self.p, v=self.v)



#x=526, y=383..390
def parse_data(f):
    data_xy_re = re.compile(r'x=(\d+), y=(\d+)\.\.(\d+)')
    data_yx_re = re.compile(r'y=(\d+), x=(\d+)\.\.(\d+)')
    clays = []
    for l in f:
        l = l.strip()
        xy = data_xy_re.match(l)
        yx = data_yx_re.match(l)
        if xy:
            x, y, v = xy.group(1, 2, 3)
            clays.append(Clay(x, y, v))
        elif yx:
            y, x, v = yx.group(1, 2, 3)
            clays.append(Clay(x, y, v))
        else:
            assert False, 'Error parsing ^{}$'.format(l)

    return clays
