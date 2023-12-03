#!/usr/bin/env python
from itertools import product
import math

lines = [line.strip() for line in open(0).readlines()]


class Pos:
    def __init__(self, p):
        self.x = p[0]
        self.y = p[1]

    def __add__(self, o):
        if isinstance(o, Pos):
            return Pos((self.x + o.x, self.y + o.y))
        else:
            raise ValueError("o is not a position")

    def __eq__(self, o):
        return isinstance(o, Pos) and self.x == o.x and self.y == o.y

    def __hash__(self):
        return hash((self.x, self.y))

    def left(self):
        return self + Pos((-1, 0))

    def right(self):
        return self + Pos((1, 0))

    def __str__(self):
        return str((self.x, self.y))


def get_board(ls):
    res = {}
    for (y, line) in enumerate(ls):
        for (x, c) in enumerate(line):
            if c != '.':
                res[Pos((x, y))] = c
    return res


board = get_board(lines)


def is_digit(pos):
    try:
        return str.isdigit(board[pos])
    except:
        return False


def gear_pos_iter():
    return (pos for pos, c in board.items() if c == "*")


def rel_adjacent_poses():
    return [Pos((x, y)) for x, y in product((-1, 0, 1), (-1, 0, 1))]


def get_unused_num(from_pos, used):
    def get_unused_num_impl(pos):
        if not is_digit(pos) or pos in used:
            return []

        used.add(pos)
        return get_unused_num_impl(pos.left()) + [board[pos]] + get_unused_num_impl(pos.right())

    try:
        return int(''.join(get_unused_num_impl(from_pos)))
    except:
        return None


def get_adjacent_nums(pos, used):
    res = []
    for p in [x + pos for x in rel_adjacent_poses()]:
        if is_digit(p):
            n = get_unused_num(p, used)
            if n is None:
                continue
            res.append(n)
    return res


def get_gear_ratios():
    res = []
    for p in gear_pos_iter():
        nums = get_adjacent_nums(p, set())
        if len(nums) == 2:
            res.append(math.prod(nums))
    return res


res = sum(get_gear_ratios())
print(res)
