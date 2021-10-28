"""Imported modules/packages"""
from abc import ABC

from lib.knapsack.knapsack_resolver_interface import KnapsackResolverInterface


class KnapsackFactoryInterface(ABC):
    """
    Interface KnapsackFactory
    """

    def create(self, name: str) -> KnapsackResolverInterface:
        """
        Create knapsack
        :param name:
        :return:
        """
