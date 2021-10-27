"""Imported modules/packages"""
from typing import List, Tuple

from lib.knapsack.item import Item
from lib.knapsack.knapsack_resolver_interface import KnapsackResolverInterface
from src.knapsack.dynamic_programming_knapsack import DynamicProgrammingKnapsack
from src.knapsack.greedy_knapsack import GreedyKnapsack
from src.knapsack.naive_recursive import NaiveRecursiveKnapsack


def test_resolve_greedy_knapsack():
    knapsack: KnapsackResolverInterface = GreedyKnapsack()
    knapsack.add(Item('1', 1, 10))
    knapsack.add(Item('2', 5, 50))
    knapsack.add(Item('3', 3, 20))
    knapsack.add(Item('4', 2, 30))
    knapsack.add(Item('5', 4, 60))
    items, total = knapsack.resolve(11)
    assert total == 140
    assert len(items) == 3
    assert items[0].name == '5'
    assert items[1].name == '4'
    assert items[2].name == '2'


def test_resolve_dynamic_programming_knapsack():
    knapsack: KnapsackResolverInterface = DynamicProgrammingKnapsack()
    knapsack.add(Item('1', 1, 10))
    knapsack.add(Item('2', 5, 50))
    knapsack.add(Item('3', 3, 20))
    knapsack.add(Item('4', 2, 30))
    knapsack.add(Item('5', 4, 60))
    items, total = knapsack.resolve(11)

    assert total == 140
    assert len(items) == 3
    assert items[0].name == '2'
    assert items[1].name == '4'
    assert items[2].name == '5'


def test_resolve_naive_recursive_knapsack():
    knapsack: KnapsackResolverInterface = NaiveRecursiveKnapsack()
    knapsack.add(Item('1', 1, 10))
    knapsack.add(Item('2', 5, 50))
    knapsack.add(Item('3', 3, 20))
    knapsack.add(Item('4', 2, 30))
    knapsack.add(Item('5', 4, 60))
    items, total = knapsack.resolve(11)

    assert total == 140
    assert len(items) == 3
    assert items[0].name == '2'
    assert items[1].name == '4'
    assert items[2].name == '5'
