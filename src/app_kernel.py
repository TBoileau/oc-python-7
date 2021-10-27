"""Imported modules/packages"""
from lib.dependency_injection.container_interface import ContainerInterface
from lib.kernel import Kernel
from lib.knapsack.knapsack_resolver_interface import KnapsackResolverInterface
from lib.reader.reader_interface import ReaderInterface
from src.knapsack.greedy import Greedy
from src.reader.csv_reader import CsvReader


class AppKernel(Kernel):
    """
    AppKernel class
    """

    def build(self, container: ContainerInterface):
        container.alias(ReaderInterface, CsvReader)
        container.alias(KnapsackResolverInterface, Greedy)
