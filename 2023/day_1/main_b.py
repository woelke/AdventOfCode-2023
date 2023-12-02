#!/usr/bin/env python

from itertools import takewhile

lines = [line.strip() for line in open('input').readlines()]
# lines = [line.strip() for line in open('test_b_input').readlines()]

place_holders = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
place_holder_mapping = dict([(p, i+1) for (i, p) in enumerate(place_holders)])

def to_real_digits(line):
    end = len(list(takewhile(lambda x: not str.isdigit(x), line)))

    findings_end = [(real, line.find(real, 0, end)) for real in place_holders]
    findings_start = [(real, line.rfind(real)) for real in place_holders]

    try:
        first = min(filter(lambda x: x[1] != -1, findings_end), key=lambda x: x[1])
        res = line.replace(first[0], str(place_holder_mapping[first[0]]), 1)
    except:
        res = line

    try:
        last = max(filter(lambda x: x[1] != -1, findings_start), key=lambda x: x[1])
        res = res.replace(last[0], str(place_holder_mapping[last[0]]))
    except:
        pass

    return res


def to_res(line):
    res = list(filter(lambda c: str.isdigit(c), to_real_digits(line)))
    return int(res[0] + res[-1])

print(sum([ to_res(line) for line in lines]))



