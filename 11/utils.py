import numpy as np
from scipy import signal

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



def max_energy_coordinates(power_level):
    f = signal.convolve2d(power_level, np.ones((3,3)), 'valid')
    ind = np.unravel_index(np.argmax(f, axis=None), f.shape)
    return (ind[0] + 1, ind[1] + 1), np.amax(f)
