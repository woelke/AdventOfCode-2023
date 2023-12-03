#!/usr/bin/env python
from dotmap import DotMap
from more_itertools import iterate
from itertools import chain
import sys

lines = [line.strip() for line in open('input').readlines()]


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


def symbol_pos_iter():
    return (pos for pos, c in board.items() if not str.isdigit(c))


def rel_adjacent_poses():
    return [Pos(p) for p in [(1, 1), (0, 1), (-1, 1), (1, 0), (0, 0), (-1, 0), (1, -1), (0, -1), (-1, -1)]]


def get_unused_num(from_pos, used):
    def find_num_start(pos):
        for p in iterate(lambda x: x.left(), pos):
            if is_digit(p):
                continue
            return p.right()
        raise Exception("unreachable")

    res = ""
    for p in iterate(lambda x: x.right(), find_num_start(from_pos)):
        if p in used:
            return None

        if is_digit(p):
            used[p] = True
            res += board[p]
        else:
            if len(res) > 0:
                return int(res)
            else:
                raise Exception("unreachable")
    raise Exception("unreachable")


def get_adjacent_nums(pos, used):
    res = []
    for p in [x + pos for x in rel_adjacent_poses()]:
        if is_digit(p):
            n = get_unused_num(p, used)
            if n is None:
                continue
            res.append(n)
    return res

def get_nums_next_to_symbols():
    used = {}
    res = []
    for p in symbol_pos_iter():
        res.extend(get_adjacent_nums(p, used))
    return res

res = sum(get_nums_next_to_symbols())
print(res)




