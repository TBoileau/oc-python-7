"""Imported modules/packages"""
from typing import List

from lib.knapsack.item import Item
from lib.knapsack.knapsack_resolver_interface import KnapsackResolverInterface


class AbstractKnapsack(KnapsackResolverInterface):
    """
    Abstract class Knapsack
    """

    def __init__(self):
        """
        Constructor
        """
        self.items: List[Item] = []

    def add(self, item: Item):
        self.items.append(item)
