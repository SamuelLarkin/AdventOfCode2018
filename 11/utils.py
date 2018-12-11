import numpy as np
from scipy import signal
from tqdm import trange
from collections import namedtuple


Datum = namedtuple('Datum', ('coordinates', 'power', 'size'))


def grid(grid_serial_number, size=300):
    grid_y, grid_x = np.meshgrid(range(size), range(size), indexing='ij')
    grid_x += 1
    grid_y += 1
    # Find the fuel cell's rack ID, which is its X coordinate plus 10.
    rack_id = grid_x + 10
    # Begin with a power level of the rack ID times the Y coordinate.
    power_level = rack_id * grid_y
    # Increase the power level by the value of the grid serial number (your puzzle input).
    power_level += grid_serial_number
    # Set the power level to itself multiplied by the rack ID.
    power_level *= rack_id
    # Keep only the hundreds digit of the power level (so 12345 becomes 3; numbers with no hundreds digit become 0).
    power_level = (power_level / 100).astype(np.int)
    power_level = (power_level % 10).astype(np.int)
    # Subtract 5 from the power level.
    power_level -= 5

    return power_level.T



def max_energy(power_level, size=3):
    f = signal.convolve2d(power_level, np.ones((size,size)), 'valid')
    coordinates = np.unravel_index(np.argmax(f, axis=None), f.shape)
    coordinates = (coordinates[0]+1, coordinates[1]+1)
    return Datum(coordinates, int(np.amax(f)), size)



def partII(power_level):
   most_power_cell = Datum((0,0), 0, 0)
   for size in trange(1, 300+1):
      most_power_cell = max(most_power_cell,
            max_energy(power_level, size),
            key=lambda x: x.power)

   return most_power_cell
