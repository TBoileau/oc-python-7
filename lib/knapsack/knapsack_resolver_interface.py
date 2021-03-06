"""Imported modules/packages"""
from abc import ABC
from typing import List, Tuple

from lib.knapsack.item import Item


class KnapsackResolverInterface(ABC):
    """
    Interface Resolver
    """

    @staticmethod
    def name() -> str:
        """
        Get name in knapsack
        :param item:
        :return:
        """

    def add(self, item: Item):
        """
        Add item in knapsack
        :param item:
        :return:
        """

    def resolve(self, volume: int) -> Tuple[List[Item], int]:
        """
        Resolve knapsack algorithm and return list of items

        :param volume:
        :return:
        """
