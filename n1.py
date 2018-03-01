def read_field(path):
    """
    (str) -> (data)
    Read board for game * alive part of ship, X - dead and " " -  if cell
    is empty
    """
    data = []
    with open(path, "r") as file:
        for line in file:
            data.append(list(line[:-1]))
    return data


def has_ship(data, coor):
    """
    (data, tuple) -> (bool)
    Check if there is ship in the cell
    """
    if data[coor[1] - 1][ord(coor[0]) - 65] == "*":
        return True
    return False


def ship_size(data, coor):
    """
    (data, tuple) -> (tuple)
    Return length of ship which is in given cell
    """
    coor = [coor[1] - 1, ord(coor[0]) - 65]
    if data[coor[0]][coor[1]] != "*":
        return 0
    length = 1
    for side in range(4):
        coor0 = coor
        side_v, side_h = 0, 0
        if side == 0: side_v = 1
        if side == 1: side_v = -1
        if side == 2: side_h = 1
        if side == 3: side_h = -1
        while 0 < coor0[0] + side_v < 10 and 0 < coor0[1] + side_h < 10 and \
                data[coor0[0] + side_v][coor0[1] + side_h] == "*":
            length += 1
            coor0 = [coor0[0] + side_v, coor0[1] + side_h]
    return length


data = read_field("field.txt")
print(ship_size(data, ("B", 2)))
