"""Imported modules/packages"""
import os

from lib.dependency_injection.container_interface import ContainerInterface
from lib.kernel import Kernel
from lib.knapsack.item import Item
from lib.knapsack.knapsack_resolver_interface import KnapsackResolverInterface
from lib.reader.reader_interface import ReaderInterface
from src.app_kernel import AppKernel


def test_resolve_knapsack_with_dataset_1():
    kernel: Kernel = AppKernel()
    kernel.run()
    container: ContainerInterface = kernel.container
    knapsack: KnapsackResolverInterface = container.get(KnapsackResolverInterface)
    reader: ReaderInterface = container.get(ReaderInterface)

    data = reader.read(os.path.join(os.getcwd(), "fixtures", "dataset_1.csv"))

    assert len(data) == 1001

    for row in data:
        action_price: int = int(float(row['price']) * 100)
        if action_price <= 0:
            continue
        profit: int = int(action_price * (float(row['profit']) / 100))
        knapsack.add(Item(row['name'], action_price, profit))

    total: int = 0
    for item in knapsack.resolve(20000):
        total += item.weight

    assert total == 19997