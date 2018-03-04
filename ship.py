class Ship:
    def __init__(self, bow, horizontal, length):
        self.bow = bow
        self.horizontal = horizontal
        self.__length = length
        self.__hit = [False for i in range(length)]

    def shoot_at(self, coor):
        # choose in what side is ship
        self.__hit[max(self.bow[0] - coor[0], self.bow[1]-coor[1])] = True