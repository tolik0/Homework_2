class Ship:
    def __init__(self, bow, horizontal, length):
        self.bow = bow
        self.horizontal = horizontal
        self.__length = length
        self.__hit = [False for i in range(length)]

    def shoot_at(self, coor):
        # choose in what side is ship
        print(1)
        self.__hit[max(coor[0] - self.bow[0], coor[1] - self.bow[1])] = True
        print(coor, self.bow)