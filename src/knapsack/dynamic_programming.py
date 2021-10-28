"""Imported modules/packages"""
import copy
from typing import List, Tuple

from lib.knapsack.abstract_knapsack import AbstractKnapsack
from lib.knapsack.item import Item


class DynamicProgramming(AbstractKnapsack):
    """
    Class DynamicProgramming
    """

    @staticmethod
    def name() -> str:
        return "dynamic_programming"

    def resolve(self, volume: int) -> Tuple[List[Item], int]:
        number_of_items: int = len(self.items)
        values: List[List] = [[0 for x in range(volume + 1)] for x in range(number_of_items + 1)]
        items: List[List] = copy.deepcopy(values)

        for i in range(number_of_items + 1):
            for j in range(volume + 1):
                if i == 0 or j == 0:
                    values[i][j] = 0
                    items[i][j] = []
                    continue

                if self.items[i - 1].weight <= j:
                    temp_total: int = self.items[i - 1].value + values[i - 1][j - self.items[i - 1].weight]
                    if temp_total >= values[i - 1][j]:
                        values[i][j] = temp_total
                        items[i][j] = items[i - 1][j - self.items[i - 1].weight] + [i - 1]
                        continue

                values[i][j] = values[i - 1][j]
                items[i][j] = items[i - 1][j]

        return (
            list(map(lambda index: self.items[index], items[number_of_items][volume])),
            values[number_of_items][volume],
        )
