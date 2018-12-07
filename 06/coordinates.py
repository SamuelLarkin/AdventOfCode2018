import numpy as np


test_data = [
        '1, 1',
        '1, 6',
        '8, 3',
        '3, 4',
        '5, 5',
        '8, 9',
        ]



def get_coordinates(iterable):
    def coordinate(l):
        x, y = l.strip().split(',')
        return int(x), int(y)

    return np.asarray(list(map(coordinate, iterable)), dtype=np.int)



def calculate_distances(coordinates):
    x_max, y_max = np.amax(coordinates, axis=0)
    meshes = np.asarray(np.meshgrid(list(range(x_max)), list(range(y_max)), indexing='ij'))
    meshes = np.expand_dims(meshes, axis=0)
    # meshes.shape: (1, 2, x_max, y_max)

    coordinates = np.expand_dims(coordinates, axis=-1)
    coordinates = np.expand_dims(coordinates, axis=-1)
    # coordinates.shape = (#coords, 2, 1, 1)

    distance = np.sum(np.abs(meshes - coordinates), axis=1)
    # distance.shape = (#coords, x_max, y_max)

    return distance



def get_mask_equidistant(distance):
    # Remove coordinates that are share by two groups
    # for a given coordinate on the grid, is there more than one point that is at equi-distance?
    # If so, this grid coordinate cannot be part of any group.
    a = np.sort(distance, axis=0)
    #print(a.shape)
    #print(a[0] == a[1])

    return a[0] == a[1]



def find_id_of_infinite_area(territories):
    # If a group touches the edge of the grid, it is considered infinite.
    border = np.copy(territories)
    border[1:-1, 1:-1] = -1
    #print('border:', border)

    infinite = np.unique(border)
    #print('infinite:', infinite)

    return infinite
