"""Imported modules/packages"""
from abc import ABC
from pstats import Stats
from typing import List

from lib.knapsack.item import Item


class LoggerInterface(ABC):
    """
    Logger interface
    """
    def write(self):
        """
        Write json report
        :return:
        """
    def log(self, dataset: str, algorithm: str, items: List[Item], stats: Stats):
        """
        Log report

        :param dataset:
        :param algorithm:
        :param items:
        :param stats:
        :return:
        """
