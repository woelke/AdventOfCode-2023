#!/usr/bin/env python

lines = [line.strip() for line in open('input').readlines()]

def to_res(line):
    res = list(filter(lambda c: str.isdigit(c), line))
    return int(res[0] + res[-1])

print(sum([ to_res(line) for line in lines]))



