from typing import List


def spiral_loop(n):
    """
     Given a number <n> this function will create an n*n grid with numbers going from 1 to n^2 in a spiral fashion
    :param n:
    :return:
    """
    grid = [[j + i for j in range(n)] for i in range(n)]

    return populate_grid(grid)


def populate_grid(grid, start=1):
    if len(grid) == 1:
        return [[start]]

    num = start
    new_grid = [[]]

    for _ in range(len(grid[0])):
        new_grid[0].append(num)
        num += 1
    sub_grid = [list(x) for x in zip(*grid[1:])]
    new_grid += [list(x[::-1]) for x in zip(*populate_grid(sub_grid, num))]
    return new_grid


def print_grid(grid):
    space = len(str(len(grid)**2))
    print(" " + ("_" * space + " ") * len(grid))
    for row in grid:
        print("|", end="")
        for elem in row:
            x = str(elem)
            x += " " * (space - len(x))
            print(x, end="|")
        print()
        print("|" + ("_" * space + "|") * len(grid))


if __name__ == "__main__":
    grid = spiral_loop(10)
    try:
        # assert False
        print_grid(grid)
    except:
        print(grid)
