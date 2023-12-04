#!/usr/bin/env python
from dotmap import DotMap

lines = [line.strip() for line in open(0).readlines()]


def get_cards():
    def get_nums(nums):
        return set(int(num.strip()) for num in nums.strip().split(" ") if num != "")
    for line in lines:
        l, r = line.split(":")[1].split("|")
        yield DotMap(winning=get_nums(l), yours=get_nums(r), count=1)


cards = list(get_cards())


def count_wins(c):
    return len(c.yours) - len(c.yours - c.winning)


def do_copy_algo():
    for i, card in enumerate(cards):
        wins = count_wins(card)
        for j in range(i+1, i+1+wins):
            if j >= len(cards):
                break
            cards[j].count += cards[i].count

do_copy_algo()
res = sum(c.count for c in cards)
print(res)
