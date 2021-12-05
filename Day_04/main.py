class Board:
    def __init__(self, board, board_id):
        self.id = board_id
        self.board = board
        self.score = self._get_score()
        self.columns = self._walk_columns()
        self.wins = 0
        attrs = vars(self)
        print(', '.join("%s: %s" % item for item in attrs.items()))

    def __repr__(self):
        return str(self.id)

    def __str__(self):
        return str(self.id)

    def _walk_one_column(self, index):
        column = []
        for row in self.board:
            column.append(row[index])
        return column

    def _walk_columns(self):
        columns = []
        for column in range(len(self.board[0])):
            columns.append(self._walk_one_column(column))
        return columns

    def _get_score(self):
        score = 0
        for line in self.board:
            for num in line:
                score = score + num
        return score

    def _mark(self, called):
        for row in self.board:
            if called in row:
                row.remove(called)
        for column in self.columns:
            if called in column:
                column.remove(called)

    def check(self, called):
        subtracted = False
        for row in self.board:
            if called in row:
                self._mark(called)
                self.score = self._get_score()
                subtracted = True
            if len(row) == 0:
                self.wins = self.wins + 1
                print(f"Found row winner! Board: {self.board}\n\tColumns: {self.columns}\n\tBoard ID: {self.id}\n\tCalled: {called}\n\tScore: {self.score * called}")
                return True
        for col in self.columns:
            if called in col:
                self._mark(called)
                if not subtracted:
                    self.score = self._get_score()
            if len(col) == 0:
                self.wins = self.wins + 1
                print(f"Found column winner! Board: {self.board}\n\tColumns: {self.columns}\n\tCalled: {called}\n\tScore: {self.score * called}")
                return True
        return False


def get_input():
    nums = []
    boards = []
    with open("test2.txt", "r") as file:
        nums = list(map(int, file.readline().strip().split(",")))
        temp_list = []
        for line in file:
            if line == "\n":
                if temp_list == []:
                    pass
                else:
                    boards.append(temp_list)
                    temp_list = []
                    pass
            else:
                temp_list.append(list(map(int, line.strip().split())))
    return nums, boards


def main():
    nums, raw_boards = get_input()
    boards = []
    counter = 0
    for board in raw_boards:
        boards.append(Board(board, counter))
        counter = counter + 1
    for num in nums:
        if len(boards) >= 1:
            for board1 in boards:
                if board1.check(num):
                    boards.remove(board1)
                    pass


if __name__ == '__main__':
    main()
