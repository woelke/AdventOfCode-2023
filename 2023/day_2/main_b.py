#!/usr/bin/env python
import math
import itertools

lines = [line.strip() for line in open('input').readlines()]


def get_games(ls):
    def to_tuple(p):
        return (p[1][0], int(p[0]))
    def set_to_dict(s):
        return dict([to_tuple(qs.strip().split(" ")) for qs in s.split(",")])
    return [list(map(set_to_dict, l.partition(":")[2].split(";"))) for l in ls]


gs = get_games(lines)


def get_min_set(g):
    return dict((color, max(*g, key=lambda s: 0 if color not in s else s[color])[color]) for color in list(itertools.chain(*g)))

res = sum(math.prod(filter(lambda x: x != 0, get_min_set(g).values())) for g in gs)
print(res)
