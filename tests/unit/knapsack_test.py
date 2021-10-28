"""Imported modules/packages"""
from typing import List, Tuple

from lib.knapsack.item import Item
from lib.knapsack.knapsack_resolver_interface import KnapsackResolverInterface
from src.knapsack.dynamic_programming import DynamicProgramming
from src.knapsack.greedy import Greedy
from src.knapsack.memoization_technique import MemoizationTechnique
from src.knapsack.naive_recursive import NaiveRecursive
from src.knapsack.optimized_dynamic_programming import OptimizedDynamicProgramming


def test_resolve_greedy():
    knapsack: KnapsackResolverInterface = Greedy()
    knapsack.add(Item('1', 1, 10))
    knapsack.add(Item('2', 5, 50))
    knapsack.add(Item('3', 3, 20))
    knapsack.add(Item('4', 2, 30))
    knapsack.add(Item('5', 4, 60))
    items, total = knapsack.resolve(11)
    assert total == 140



def test_resolve_dynamic_programming():
    knapsack: KnapsackResolverInterface = DynamicProgramming()
    knapsack.add(Item('5', 4, 60))
    knapsack.add(Item('2', 5, 50))
    knapsack.add(Item('4', 2, 30))
    knapsack.add(Item('3', 3, 20))
    knapsack.add(Item('1', 1, 10))
    items, total = knapsack.resolve(11)
    assert total == 140


def test_resolve_optimized_dynamic_programming():
    knapsack: KnapsackResolverInterface = OptimizedDynamicProgramming()
    knapsack.add(Item('1', 1, 10))
    knapsack.add(Item('3', 3, 20))
    knapsack.add(Item('4', 2, 30))
    knapsack.add(Item('2', 5, 50))
    knapsack.add(Item('5', 4, 60))
    items, total = knapsack.resolve(11)
    assert total == 120


def test_resolve_naive_recursive():
    knapsack: KnapsackResolverInterface = NaiveRecursive()
    knapsack.add(Item('1', 1, 10))
    knapsack.add(Item('2', 5, 50))
    knapsack.add(Item('3', 3, 20))
    knapsack.add(Item('4', 2, 30))
    knapsack.add(Item('5', 4, 60))
    items, total = knapsack.resolve(11)
    assert total == 140


def test_resolve_memoization_technique():
    knapsack: KnapsackResolverInterface = MemoizationTechnique()
    knapsack.add(Item('1', 1, 10))
    knapsack.add(Item('2', 5, 50))
    knapsack.add(Item('3', 3, 20))
    knapsack.add(Item('4', 2, 30))
    knapsack.add(Item('5', 4, 60))
    items, total = knapsack.resolve(11)
    assert total == 140

