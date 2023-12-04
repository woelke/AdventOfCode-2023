#!/usr/bin/env python
from dotmap import DotMap

lines = [line.strip() for line in open(0).readlines()]


def get_cards():
    def get_nums(nums):
        return set(int(num.strip()) for num in nums.strip().split(" ") if num != "")
    for line in lines:
        l, r = line.split(":")[1].split("|")
        yield DotMap(winning=get_nums(l), yours=get_nums(r))


cards = get_cards()


def count_wins(c):
    return len(c.yours) - len(c.yours - c.winning)


res = sum(int(2**(count_wins(c)-1)) for c in cards)
print(res)
