
def read_polymer(filename = 'data.txt'):
    with open(filename, 'r') as f:
        polymer = list(f.readline().strip())
    return polymer



def reduce_polymer(polymer):
    polymer = list(polymer)
    polymer_length = len(polymer)
    position = 0
    while position < polymer_length-1:
        if abs(ord(polymer[position]) - ord(polymer[position+1])) == 32:
            del(polymer[position+1])
            del(polymer[position])
            polymer_length -= 2
            position = max(0, position-1)
            continue
        position += 1

    return polymer
