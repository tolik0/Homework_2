class Player:
    def __init__(self, name):
        self.__name = name

    def read_position(self):
        # read coordinates
        x, y = -1, -1
        coor = input("Player {}, enter move: ".format(self.__name))
        try:
            x = int(coor[1:]) - 1
            y = ord(coor[0]) - 65
        except:
            pass
        # check coordinates
        while not (-1 < x < 10 and -1 < y < 10):
            x, y = -1, -1
            coor = input("Player {}, enter move: ".format(self.__name))
            try:
                x = int(coor[1:]) - 1
                y = ord(coor[0]) - 65
            except:
                pass

        return (int(coor[1:]) - 1, ord(coor[0]) - 65)
