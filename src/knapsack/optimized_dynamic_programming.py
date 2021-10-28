"""Imported modules/packages"""
from typing import List, Tuple, Dict

from lib.knapsack.abstract_knapsack import AbstractKnapsack
from lib.knapsack.item import Item


class OptimizedDynamicProgramming(AbstractKnapsack):
    """
    Class OptimizedDynamicProgramming
    """

    @staticmethod
    def name() -> str:
        return "optimized_dynamic_programming"

    def resolve(self, volume: int) -> Tuple[List[Item], int]:
        table = [0] * (volume + 1)
        items: Dict[int, List[Item]] = {}
        for item in self.items:
            for j in range(volume, item.weight, -1):
                total: int = item.value + table[j - item.weight]
                if table[j] <= total:
                    table[j] = total
                    items[j] = [item] + (items[j - item.weight] if j - item.weight in items else [])

        return items[volume], table[volume]
