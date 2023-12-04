#!/usr/bin/env python
from dotmap import DotMap

lines = [line.strip() for line in open(0)]


def get_cards():
    def get_nums(nums):
        return set(int(num) for num in nums.split())
    for line in lines:
        l, r = map(get_nums, line.split(":")[1].split("|"))
        yield DotMap(winning=l, yours=r, count=1)


cards = get_cards()


def count_wins(c):
    return len(c.yours) - len(c.yours - c.winning)


res = sum(int(2**(count_wins(c)-1)) for c in cards)
print(res)
