from field import Field
from player import Player
import os


class Game:
    def __init__(self):
        print("Game Battleship")
        self.__field = [Field(), Field()]
        self.__players = [Player(input("Input name of first player: ")),
                          Player(input("Input name of second player: "))]
        self.__current_player = 0

    def shoot_at(self):
        if self.__current_player == 0:
            opposite_player = 1
        else:
            opposite_player = 0
        self.__field[opposite_player].shoot_at(
            self.__players[self.__current_player].read_position())

    def field_without_ships(self):
        if self.__current_player == 0:
            opposite_player = 1
        else:
            opposite_player = 0
        return self.__field[opposite_player].field_without_ships()

    def field_with_ships(self):
        return self.__field[self.__current_player].field_with_ships()

    def play(self):
        check = []
        for i in range(10):
            for j in range(10):
                if self.__field[self.__current_player].ships[i][j] != "~" and \
                        self.__field[self.__current_player].ships[i][j] != "x":
                    check.append(all(self.__field[
                                         self.__current_player].ships[i][
                                         j]._Ship__hit))
        while not all(check):
            print(self.field_without_ships())
            self.shoot_at()
            # os.system('cls' if os.name == 'nt' else 'clear')
            if self.__current_player == 0:
                self.__current_player = 1
            else:
                self.__current_player = 0
            check = []
            for i in range(10):
                for j in range(10):
                    if self.__field[self.__current_player].ships[i][
                        j] != "~" and \
                            self.__field[self.__current_player].ships[i][
                                j] != "x":
                        check.append(all(self.__field[
                                             self.__current_player].ships[i][
                                             j]._Ship__hit))
        print("The winner is {}".format(
            self.__players[self.__current_player]._Player__name))


if __name__ == '__main__':
    game = Game()
    game.play()
