"""Imported modules/packages"""
from typing import List, Tuple

from lib.knapsack.abstract_knapsack import AbstractKnapsack
from lib.knapsack.item import Item


class NaiveRecursiveKnapsack(AbstractKnapsack):
    """
    Class GreedyKnapsack
    """

    def resolve(self, volume: int) -> Tuple[List[Item], int]:
        return self.__recursive(volume, len(self.items))

    def __recursive(self, volume: int, number_of_items: int) -> Tuple[List[Item], int]:
        """
        Naive recursive implementation
        :param volume:
        :param number_of_items:
        :return:
        """
        if number_of_items == 0 or volume == 0:
            return [], 0

        if self.items[number_of_items - 1].weight > volume:
            return self.__recursive(volume, number_of_items - 1)

        new_items, new_total = self.__recursive(
            volume - self.items[number_of_items - 1].weight, number_of_items - 1
        )
        new_items.append(self.items[number_of_items - 1])
        new_total += self.items[number_of_items - 1].value
        last_items, last_total = self.__recursive(volume, number_of_items - 1)
        return (last_items, last_total) if last_total > new_total else (new_items, new_total)
