import numpy as np
import datetime as dt

puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]

hard_puzzle = [[8, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 3, 6, 0, 0, 0, 0, 0],
               [0, 7, 0, 0, 9, 0, 2, 0, 0],
               [0, 5, 0, 0, 0, 7, 0, 0, 0],
               [0, 0, 0, 0, 4, 5, 7, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 3, 0],
               [0, 0, 1, 0, 0, 0, 0, 6, 8],
               [0, 0, 8, 5, 0, 0, 0, 1, 0],
               [0, 9, 0, 0, 0, 0, 4, 0, 0]]


def print_board(puzzle: np.array) -> None:
    for i in range(puzzle.shape[0]):
        if not i % 3 and i != 0:
            print("---------------------")

        for j in range(puzzle.shape[1]):
            if j % 3 == 0 and j != 0:
                print('|', end=" ")
            if j == 8:
                print(puzzle[i, j])
            else:
                print(puzzle[i, j], end=" ")


def find_empty_pos(puzzle: np.array) -> tuple:
    for i in range(9):
        for j in range(9):
            if puzzle[i, j] == 0:
                return i, j
    return None


def valid_value(puzzle: np.array, pos: tuple, num: int) -> bool:
    if num not in puzzle[pos[0]] and \
            num not in puzzle[:, pos[1]] and \
            num not in puzzle[pos[0] // 3 * 3:pos[0] // 3 * 3 + 3, pos[1] // 3 * 3:pos[1] // 3 * 3 + 3]:
        return True
    return False


def solver(puzzle: np.array) -> bool:
    pos = find_empty_pos(puzzle)
    if pos is None:
        return True

    for i in range(1, 10):
        if valid_value(puzzle, pos, i):
            puzzle[pos] = i

            if solver(puzzle):
                return True

            puzzle[pos] = 0

    return False


def time_it(function):
    def wrapper(*args, **kwargs):
        start = dt.datetime.now()
        rv = function(*args, **kwargs)
        end = dt.datetime.now()
        time_took = end - start
        print(f"\n\nTotal runtime:{time_took.microseconds / 1000: .2f}ms")
        return rv
    return wrapper


@time_it
def soduku_solver(puzzle: list) -> None:
    puzzle = np.array(puzzle)
    print("Before solving:", end="\n\n")
    print_board(puzzle)
    solver(puzzle)
    print("\n\nAfter update!", end="\n\n")
    print_board(puzzle)
