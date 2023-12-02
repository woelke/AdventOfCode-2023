#!/usr/bin/env python

lines = [line.strip() for line in open('input').readlines()]

def get_games(ls):
    def to_tuple(p):
        return (p[1][0], int(p[0]))
    def set_to_dict(s):
        return dict([to_tuple(qs.strip().split(" ")) for qs in s.split(",")])
    return [list(map(set_to_dict, l.partition(":")[2].split(";"))) for l in ls]

def is_set_valid(ss, r):
    return not any(r[color] < count for (color, count) in ss.items())

rules = {"r": 12, "g": 13, "b": 14}
gs = get_games(lines)

res = sum([i+1 if all(map(lambda x: is_set_valid(x, rules), g)) else 0 for (i,g) in enumerate(gs)])
print(res)

