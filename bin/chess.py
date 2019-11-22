import itertools

class Queens:

    def __init__(self, size_borad):
        self.size = size_borad
        self.solutions = dict()
        self.desc_solution = []

    def __check_legal(self, board):
        legal = True
        for i, ci in enumerate(board):
            for cj in board[(i + 1):]:
                if abs(ci - cj) == abs(board.index(ci) - board.index(cj)):
                    legal = False
        return legal

    def __check_if_legal(self, boards):
        count = 0
        valid_boards = []
        for board in boards:
            n = len(board)
            if self.__check_legal(board):
                count += 1
                valid_boards.append(board)
        self.desc_solution.append('{} QUEENS |'
                        ' {} legal boards'.format(n, count))
        return valid_boards

    def __generate_configs(self, size):
        n_board = list(range(1, size + 1))
        # size = 5 -> n_board = [1, 2, 3, 4, 5]
        configs = itertools.permutations(n_board)
        return configs

    def resolve(self):
        for i in range(1, self.size + 1):
            self.solutions[i] = self.__check_if_legal(self.__generate_configs(i))
        return self.solutions
