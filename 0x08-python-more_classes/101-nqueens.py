#!/usr/bin/python3
"""
This module tries to solve the Nqueen problem
It does it 2 ways:
1 - uses a recursive backtracking algorithm in a class
2 - uses a stack
"""
import sys


class Queens:
    """
    This class is used to solve the n-queens problem, giving all solutions

    **instance attributes**
    solution: an array, each index is a column each value is a row
    size: size of chessboard
    """
    def __init__(self, value):
        """
        initializes a Queens object

        Arguments:
            value: the size of the chess board
        """
        self.solution = [0 for i in range(value)]
        self.size = value

    def place_queen(self, row, col):
        """
        Places a queen at row and column

        Arguments:
            row: a row index
            col: a column index
        """
        self.solution[col] = row

    def remove_queen(self, col):
        """
        Removes a queen in a column

        Arguments:
            col: a column index
        """
        self.solution[col] = 0

    def is_safe(self, row, col):
        """
        Checks if a case satisfies the constraints

        Arguments:
            row: row index
            col: column index
        """
        for i in range(col):
            if self.solution[i] == row:
                return False
        for i in range(col):
            if (abs((i - col) / (self.solution[i] - row)) == 1):
                return False
        return True

    def solve_rec(self, col):
        """
        Solves the problem through recursion

        Arguments:
            col: the starting point
        """
        if col >= self.size:
            self.print_fancy()
        for i in range(self.size):
            if self.is_safe(i, col):
                self.place_queen(i, col)
                if self.solve_rec(col + 1):
                    return True
                self.remove_queen(col)
        return False

    def print_fancy(self):
        """Print according to school requirements"""
        print("[" + ", ".join(["[{:d}, {:d}]".format(i, self.solution[i])
                               for i in range(self.size)]) + "]")


# for the stack I did not use the class as the requirements are a bit different

def next_choices(solution, size):
    """
    Given a tentative solution, returns the possible next moves

    Arguments:
        solution: a tentative solution
        size: size of chess board

    Return:
        list of possible choices
    """
    children = []
    col = len(solution)
    for j in range(size):
        ok = True
        for i in range(len(solution)):
            if solution[i] == j:
                ok = False
                break
            if (abs((i - col) / (solution[i] - j)) == 1):
                ok = False
        if ok:
            children.append(j)
    return children


def print_nice(sol, size):
    """print according to requirements"""
    print("[" + ", ".join(["[{:d}, {:d}]".format(i, sol[i])
                           for i in range(size)]) + "]")


def solve_stack(size):
    """
    Solves the n-queens problem with a stack of possible beginning of solutions

    Arguments:
        size: size of chess board
    """
    for i in range(size):
        stack = [[i]]
        while stack:
            last = stack.pop()
            for choice in next_choices(last, size):
                sol = last + [choice]
                if len(sol) == size:
                    print_nice(sol, size)
                    break
                stack.append(sol)


if __name__ == "__main__":

    # the error checking is done here to use both solutions

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)

    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    q = Queens(int(sys.argv[1]))
    # q.solve_rec(0)

    solve_stack(int(sys.argv[1]))
