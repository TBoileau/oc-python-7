"""Imported modules/packages"""
from typing import Dict, Callable

from lib.knapsack.knapsack_factory_interface import KnapsackFactoryInterface
from lib.knapsack.knapsack_resolver_interface import KnapsackResolverInterface
from src.knapsack.dynamic_programming import DynamicProgramming
from src.knapsack.greedy import Greedy
from src.knapsack.memoization_technique import MemoizationTechnique
from src.knapsack.naive_recursive import NaiveRecursive
from src.knapsack.optimized_dynamic_programming import OptimizedDynamicProgramming


class KnapsackFactory(KnapsackFactoryInterface):
    """
    Class KnapsackFactory
    """

    def __init__(self):
        """
        Constructor
        """
        self.knapsacks: Dict[str, Callable] = {
            "dynamic_programming": DynamicProgramming,
            "optimized_dynamic_programming": OptimizedDynamicProgramming,
            "greedy": Greedy,
            "naive_recursive": NaiveRecursive,
            "memoization_technique": MemoizationTechnique,
        }

    def create(self, name: str) -> KnapsackResolverInterface:
        return self.knapsacks[name]()
