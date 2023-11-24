class GameBoard:

    def __init__(self, size):

        self.board = [0] * size
        i = 0
        while i < len(self.board):
            self.board[i] = [0] * size
            i += 1

    def print(self):
        i = 0
        while i < len(self.board):
            print(self.board[i])
            i += 1

    def add_rifts(self, rifts):
        for rift in rifts:
            start, end = rift.split(" -> ")

            startx, starty = start.split(",")
            startx = int(startx)
            starty = int(starty)
            endx, endy = end.split(",")
            endx = int(endx)
            endy = int(endy)

            # if startx == endx or starty == endy:
            x = startx
            y = starty
            while True:
                self.board[y][x] += 1

                if x == endx and y == endy:
                    break

                if endy > y:
                    y += 1
                elif endy < y:
                    y -= 1

                if endx > x:
                    x += 1
                elif endx < x:
                    x -= 1

    def count_points(self):
        count = 0
        for x in self.board:
            for y in x:
                if y > 1:
                    count += 1
        return count


def run_game_1():
    file = open("day5/input.txt")
    file_content = file.readlines()

    board = GameBoard(1000)
    board.add_rifts(file_content)
    # board.print()
    print(board.count_points())


run_game_1()
