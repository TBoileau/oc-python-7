"""Imported modules/packages"""
from typing import List

from lib.knapsack.item import Item
from src.knapsack.greedy_knapsack import GreedyKnapsack


def test_resolve_greedy_knapsack():
    knapsack: GreedyKnapsack = GreedyKnapsack()
    knapsack.add(Item('1', 1, 10))
    knapsack.add(Item('2', 5, 50))
    knapsack.add(Item('3', 3, 20))
    knapsack.add(Item('4', 2, 30))
    knapsack.add(Item('5', 4, 60))
    items: List[Item] = knapsack.resolve(11)
    assert len(items) == 3
    assert items[0].name == '5'
    assert items[1].name == '4'
    assert items[2].name == '2'
