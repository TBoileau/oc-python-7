"""Imported modules/packages"""
from abc import ABC
from typing import List

from lib.knapsack.item import Item


class KnapsackResolverInterface(ABC):
    """
    Interface Resolver
    """

    def add(self, item: Item):
        """
        Add item in knapsack
        :param item:
        :return:
        """

    def resolve(self, volume: int) -> List[Item]:
        """
        Resolve knapsack algorithm and return list of items

        :param volume:
        :return:
        """
