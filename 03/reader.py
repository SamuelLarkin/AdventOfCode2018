import re
from datum import Datum

def read_data(iterable):
    # #1 @ 596,731: 11x27
    data_re = re.compile(r'^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')

    data = []
    for l in iterable:
        m = re.match(data_re, l.strip())
        assert m, 'Error with the regular expression'
        data.append(Datum(*map(int, m.group(1,2,3,4,5))))

    return data
