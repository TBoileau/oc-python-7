"""Imported modules/packages"""
from typing import List, Tuple

from lib.knapsack.abstract_knapsack import AbstractKnapsack
from lib.knapsack.item import Item


class GreedyKnapsack(AbstractKnapsack):
    """
    Class GreedyKnapsack
    """

    def resolve(self, volume: int) -> Tuple[List[Item], int]:
        self.items.sort(reverse=True)
        total_value: int = 0
        items: List[Item] = []
        for item in self.items:
            if volume >= item.weight:
                volume -= item.weight
                total_value += item.value
                items.append(item)
        return items, total_value
