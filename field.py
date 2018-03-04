import n1
from ship import Ship
import copy


class Field:
    def __init__(self):
        # generate field
        data = n1.generate_field()
        # look for ships
        for i in range(10):
            for j in range(10):
                # when we see part of ship
                if data[i][j] == "*":
                    try:
                        # if ship is vertical
                        if type(data[i - 1][j]) == Ship:
                            # update information about the ship
                            data[i - 1][j]._Ship__length += 1
                            data[i - 1][j]._Ship__hit.append(False)
                            data[i - 1][j].horizontal = False
                            data[i][j] = data[i - 1][j]
                    except:
                        pass
                    try:
                        # if ship is horizontal
                        if type(data[i][j - 1]) == Ship:
                            # update information about the ship
                            data[i][j - 1]._Ship__hit.append(False)
                            data[i][j - 1]._Ship__length += 1
                            data[i][j] = data[i][j - 1]
                    except:
                        pass
                    # create ship if we see part of it at first time
                    if type(data[i][j] != Ship):
                        data[i][j] = Ship((i, j), True, 1)
        self.ships = data

    def shoot_at(self, coor):
        # choose cell of a field
        cell = self.ships[coor[0]][coor[1]]
        if type(cell) == Ship:
            # choose in what part of ship is shooting
            cell._Ship__hit[
                max(cell.bow[0] - coor[0], cell.bow[1] - coor[1])] = True
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
                    if data[i][j]._Ship__hit[max(data[i][j].bow[0] - i,
                                                 data[i][j].bow[1] - j)]:
                        if all(self.ships[i][j]._Ship__hit):
                            # if ship is dead
                            data[i][j] = "k"
                        else:
                            print(self.ships[i][j]._Ship__hit)
                            print(self.ships[i][j]._Ship__hit)
                            print(data[i][j]._Ship__length)
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


field1 = Field()
for i in range(10):
    field1.shoot_at((0, i))
print(field1.field_with_ships())
print(field1.field_without_ships())
