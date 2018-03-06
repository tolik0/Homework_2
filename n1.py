import random


def read_field(path):
    """
    (str) -> (data)
    Read board for game * alive part of ship, X - dead and " " -  if cell
    is empty
    """
    data = []
    with open(path, "r") as file:
        for line in file:
            data.append(list(line.strip("\n")))
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
        # choose what in what side we will go
        side_v, side_h = 0, 0
        if side == 0: side_v = 1
        if side == 1: side_v = -1
        if side == 2: side_h = 1
        if side == 3: side_h = -1
        # check if there is ship in neighbour cell
        while -1 < coor0[0] + side_v < 10 and -1 < coor0[1] + side_h < 10 and \
                data[coor0[0] + side_v][coor0[1] + side_h] == "*":
            length += 1
            coor0 = [coor0[0] + side_v, coor0[1] + side_h]
    return length


def is_valid(data):
    """
    (data) -> (bool)
    Check if board is correct
    """
    check = [0 for i in range(4)]
    # calculate how many ships are with different lengths
    for i in range(10):
        for j in range(10):
            length = ship_size(data, (chr(65 + j), i + 1))
            # if ship is to big
            if length > 4:
                return False
            # if there is ship there
            if length:
                check[length - 1] += 1
    # check ships
    for i in range(4):
        if check[i] != (i + 1) * (4 - i):
            return False
    # check corners
    for i in range(1, 10):
        for j in range(10):
            try:
                if data[i - 1][j + 1] == "*" and data[i][j] == "*":
                    return False
            except:
                pass
            try:
                if data[i - 1][j - 1] == "*" and data[i][j] == "*":
                    return False
            except:
                pass
    return True


def field_to_str(data):
    """
    (data) -> (str)
    Transform field to string
    """
    field = "   " + "".join([chr(65 + i) for i in range(10)])
    for i in range(10):
        if i < 9:
            field += "\n" + str(i + 1) + "  " + "".join(data[i])
        else:
            field += "\n" + str(i + 1) + " " + "".join(data[i])
    return field


def generate_field():
    """
    () -> (data)
    Create random field
    """
    data = [["~" for i in range(10)] for j in range(10)]
    while not is_valid(data):
        data = [["~" for i in range(10)] for j in range(10)]
        x, y = 0, 0
        for i in range(4):
            for j in range(i + 1):
                x, y = random.randint(0, 6 + i), random.randint(0, 6 + i)
                while (data[x][y] == "*"):
                    x, y = random.randint(0, 6 + i), random.randint(0, 6 + i)
                n = random.randint(0, 1)
                if n:
                    for z in range(4 - i):
                        data[x][y + z] = "*"
                else:
                    for z in range(4 - i):
                        data[x + z][y] = "*"
    return data
