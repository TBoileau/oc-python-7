"""Imported modules/packages"""
import copy
from typing import List, Tuple

from lib.knapsack.abstract_knapsack import AbstractKnapsack
from lib.knapsack.item import Item


class MemoizationTechnique(AbstractKnapsack):
    """
    Class MemoizationTechnique
    """

    def resolve(self, volume: int) -> Tuple[List[Item], int]:
        totals: List[List] = [[-1 for i in range(volume + 1)] for j in range(len(self.items) + 1)]
        items: List[List] = copy.deepcopy(totals)
        return self.__recursive(totals, items, volume, len(self.items))

    def __recursive(self, totals: List[List], items: List[List], volume: int, number_of_items: int) -> Tuple[List, int]:
        """
        Memoization Technique recursive implementation
        :param totals:
        :param items:
        :param volume:
        :param number_of_items:
        :return:
        """
        if number_of_items == 0 or volume == 0:
            return [], 0

        if totals[number_of_items][volume] != -1:
            return (
                list(map(lambda index: self.items[index], items[number_of_items][volume])),
                totals[number_of_items][volume],
            )

        if self.items[number_of_items - 1].weight <= volume:
            new_items, new_total = self.__recursive(
                totals, items, volume - self.items[number_of_items - 1].weight, number_of_items - 1
            )
            new_items.append(self.items[number_of_items - 1])
            new_total += self.items[number_of_items - 1].value
            last_items, last_total = self.__recursive(totals, items, volume, number_of_items - 1)

            return (last_items, last_total) if last_total > new_total else (new_items, new_total)

        return self.__recursive(totals, items, volume, number_of_items - 1)
