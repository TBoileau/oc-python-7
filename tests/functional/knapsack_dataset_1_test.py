"""Imported modules/packages"""
import os

from lib.dependency_injection.container_interface import ContainerInterface
from lib.kernel import Kernel
from lib.knapsack.item import Item
from lib.knapsack.knapsack_resolver_interface import KnapsackResolverInterface
from lib.reader.reader_interface import ReaderInterface
from src.app_kernel import AppKernel
from src.knapsack.dynamic_programming_knapsack import DynamicProgrammingKnapsack
from src.knapsack.greedy_knapsack import GreedyKnapsack


def test_resolve_knapsack_dataset_1_with_greedy():
    kernel: Kernel = AppKernel()
    kernel.run()
    container: ContainerInterface = kernel.container
    knapsack: KnapsackResolverInterface = container.get(GreedyKnapsack)
    reader: ReaderInterface = container.get(ReaderInterface)

    data = reader.read(os.path.join(os.getcwd(), "fixtures", "dataset_1.csv"))

    assert len(data) == 1001

    for row in data:
        action_price: int = int(float(row['price']) * 100)
        if action_price <= 0:
            continue
        profit: int = int(action_price * (float(row['profit']) / 100))
        knapsack.add(Item(row['name'], action_price, profit))


    items, total = knapsack.resolve(50000)

    assert len(items) == 3

    total_weight = 0
    for item in items:
        total_weight += item.weight
    assert 50000 >= total_weight


def test_resolve_knapsack_dataset_1_with_dynamic_programming():
    kernel: Kernel = AppKernel()
    kernel.run()
    container: ContainerInterface = kernel.container
    knapsack: KnapsackResolverInterface = container.get(DynamicProgrammingKnapsack)
    reader: ReaderInterface = container.get(ReaderInterface)

    data = reader.read(os.path.join(os.getcwd(), "fixtures", "dataset_1.csv"))

    assert len(data) == 1001

    for row in data:
        action_price: int = int(float(row['price']) * 100)
        if action_price <= 0:
            continue
        profit: int = int(action_price * (float(row['profit']) / 100))
        knapsack.add(Item(row['name'], action_price, profit))

    items, total = knapsack.resolve(50000)

    assert len(items) == 22

    total_weight = 0
    for item in items:
        total_weight += item.weight
    assert 50000 >= total_weight