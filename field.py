import n1
from ship import Ship
import copy
import random


class Field:
    def __init__(self):
        def is_valid(data):
            """
            (data) -> (bool)
            Check if board is correct
            """
            check = [0 for i in range(4)]
            # calculate how many ships are with different lengths
            for i in range(10):
                for j in range(10):
                    if type(data[i][j]) == Ship:
                        check[data[i][j]._Ship__length-1] += 1
            # check ships
            for i in range(4):
                if check[i] != (i + 1) * (4 - i):
                    return False
            # check corners
            for i in range(1, 10):
                for j in range(10):
                    try:
                        if type(data[i - 1][j + 1]) == Ship and \
                                type(data[i][j]) == Ship:
                            return False
                    except:
                        pass
                    try:
                        if type(data[i - 1][j - 1]) == Ship and \
                                type(data[i][j]) == Ship:
                            return False
                    except:
                        pass
            return True

        def generate_field():
            """
            () -> (data)
            Create random field
            """
            data = [["~" for i in range(10)] for j in range(10)]
            while not is_valid(data):
                data = [["~" for i in range(10)] for j in range(10)]
                for i in range(4):
                    for j in range(i + 1):
                        x, y = random.randint(0, 6 + i), random.randint(0,
                                                                        6 + i)
                        ship = Ship([x, y], random.choice([True, False]),
                                    4 - i)
                        while (type(data[x][y]) == Ship):
                            x, y = random.randint(0, 6 + i), random.randint(0,
                                                                            6 + i)
                            ship = Ship([x, y], random.choice([True, False]),
                                        4 - i)
                        if ship.horizontal:
                            for z in range(4 - i):
                                data[x][y + z] = ship
                        else:
                            for z in range(4 - i):
                                data[x + z][y] = ship
            return data

        self.ships = generate_field()

    def shoot_at(self, coor):
        # choose cell of a field
        cell = self.ships[coor[0]][coor[1]]
        if type(cell) == Ship:
            # choose in what part of ship is shooting
            cell.shoot_at(coor)
        else:
            self.ships[coor[0]][coor[1]] = "x"

    def field_without_ships(self):
        # create copy to modify it
        data = copy.deepcopy(self.ships)
        for i in range(10):
            for j in range(10):
                # if sheep is in that cell
                if type(data[i][j]) == Ship:
                    # if that part of ship is shooted
                    if data[i][j]._Ship__hit[max(i -data[i][j].bow[0],
                                                 j - data[i][j].bow[1])]:
                        if all(self.ships[i][j]._Ship__hit):
                            # if ship is dead
                            data[i][j] = "k"
                        else:
                            # if that part of ship is shooted
                            data[i][j] = "#"
                    else:
                        # if it is empty cell
                        data[i][j] = "~"
        return n1.field_to_str(data)

    def field_with_ships(self):
        data = copy.deepcopy(self.ships)
        for i in range(10):
            for j in range(10):
                # if sheep is in that cell
                if type(data[i][j]) == Ship:
                    # if that part of ship is shooted
                    if data[i][j]._Ship__hit[max(data[i][j].bow[0] - i,
                                                 data[i][j].bow[1] - j)]:
                        if all(data[i][j]._Ship__hit):
                            # if ship is dead
                            data[i][j] = "k"
                        else:
                            # if that part of ship is shooted
                            data[i][j] = "#"
                    else:
                        # if that part of ship is alive
                        data[i][j] = "*"
        return n1.field_to_str(data)

# We can use it for testing
# field1 = Field()
# for i in range(10):
#     field1.shoot_at((0, i))
# for i in range(10):
#     field1.shoot_at((1, i))
# for i in range(10):
#     field1.shoot_at((2, i))
# print(field1.field_with_ships())
# print(field1.field_without_ships())

