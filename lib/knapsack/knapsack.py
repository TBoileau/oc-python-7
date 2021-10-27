"""Imported modules/packages"""
from typing import List

from lib.knapsack.item import Item
from lib.knapsack.knapsack_resolver_interface import KnapsackResolverInterface


class Knapsack(KnapsackResolverInterface):
    """
    Class Knapsack
    """

    def __init__(self):
        """
        Constructor
        """
        self.items: List[Item] = []

    def add(self, item: Item):
        self.items.append(item)

    def resolve(self, volume: int) -> List[Item]:
        self.items.sort(reverse=True)
        total_value: int = 0
        items: List[Item] = []
        for item in self.items:
            if volume >= item.weight:
                volume -= item.weight
                total_value += item.value
                items.append(item)
        return items
