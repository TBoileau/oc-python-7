"""Imported modules/packages"""
import os
from typing import Dict, Any, Union, List

from lib.dependency_injection.container_interface import ContainerInterface
from lib.kernel import Kernel
from lib.knapsack.item import Item
from lib.knapsack.knapsack_resolver_interface import KnapsackResolverInterface
from lib.reader.reader_interface import ReaderInterface
from src.app_kernel import AppKernel
from src.knapsack.dynamic_programming import DynamicProgramming
from src.knapsack.greedy import Greedy
from src.knapsack.memoization_technique import MemoizationTechnique
from src.knapsack.naive_recursive import NaiveRecursive
from src.knapsack.optimized_dynamic_programming import OptimizedDynamicProgramming


def test_resolve_knapsack_dataset_0_with_greedy():
    kernel: Kernel = AppKernel()
    kernel.run()
    container: ContainerInterface = kernel.container
    knapsack: KnapsackResolverInterface = container.get(Greedy)
    reader: ReaderInterface = container.get(ReaderInterface)

    data = reader.read(os.path.join(os.getcwd(), "fixtures", "dataset_0.csv"))

    assert len(data) == 20

    for row in data:
        action_price: int = int(float(row['price']) * 100)
        if action_price <= 0:
            continue
        profit: int = int(action_price * (float(row['profit']) / 100))
        knapsack.add(Item(row['name'], action_price, profit))


    items, total = knapsack.resolve(50000)

    assert len(items) == 8
    total_weight = 0
    for item in items:
        total_weight += item.weight
    assert 50000 >= total_weight


def test_resolve_knapsack_dataset_0_with_dynamic_programming():
    kernel: Kernel = AppKernel()
    kernel.run()
    container: ContainerInterface = kernel.container
    knapsack: KnapsackResolverInterface = container.get(DynamicProgramming)
    reader: ReaderInterface = container.get(ReaderInterface)

    data = reader.read(os.path.join(os.getcwd(), "fixtures", "dataset_0.csv"))

    def create_item(row: Dict[str, Any]) -> Union[None, Item]:
        action_price: int = int(float(row['price']) * 100)
        if action_price <= 0:
            return None
        profit: int = int(action_price * (float(row['profit']) / 100))
        return Item(row['name'], action_price, profit)

    items: List[Item] = list(filter(lambda item: item is not None, map(create_item, data)))
    items.sort(key=lambda item: item.value, reverse=True)

    knapsack.items = items
    items, total = knapsack.resolve(50000)

    total_weight = 0
    for item in items:
        total_weight += item.weight
    assert 50000 >= total_weight


def test_resolve_knapsack_dataset_0_with_optimized_dynamic_programming():
    kernel: Kernel = AppKernel()
    kernel.run()
    container: ContainerInterface = kernel.container
    knapsack: KnapsackResolverInterface = container.get(OptimizedDynamicProgramming)
    reader: ReaderInterface = container.get(ReaderInterface)

    data = reader.read(os.path.join(os.getcwd(), "fixtures", "dataset_0.csv"))

    def create_item(row: Dict[str, Any]) -> Union[None, Item]:
        action_price: int = int(float(row['price']) * 100)
        if action_price <= 0:
            return None
        profit: int = int(action_price * (float(row['profit']) / 100))
        return Item(row['name'], action_price, profit)

    items: List[Item] = list(filter(lambda item: item is not None, map(create_item, data)))
    items.sort(key=lambda item: item.value, reverse=True)

    knapsack.items = items
    items, total = knapsack.resolve(50000)

    total_weight = 0
    for item in items:
        total_weight += item.weight
    assert 50000 >= total_weight


def test_resolve_knapsack_dataset_0_with_naive_recursive():
    kernel: Kernel = AppKernel()
    kernel.run()
    container: ContainerInterface = kernel.container
    knapsack: KnapsackResolverInterface = container.get(NaiveRecursive)
    reader: ReaderInterface = container.get(ReaderInterface)

    data = reader.read(os.path.join(os.getcwd(), "fixtures", "dataset_0.csv"))

    assert len(data) == 20

    for row in data:
        action_price: int = int(float(row['price']) * 100)
        if action_price <= 0:
            continue
        profit: int = int(action_price * (float(row['profit']) / 100))
        knapsack.add(Item(row['name'], action_price, profit))

    items, total = knapsack.resolve(50000)

    assert len(items) == 10
    total_weight = 0
    for item in items:
        total_weight += item.weight
    assert 50000 >= total_weight


def test_resolve_knapsack_dataset_0_with_memoization_technique():
    kernel: Kernel = AppKernel()
    kernel.run()
    container: ContainerInterface = kernel.container
    knapsack: KnapsackResolverInterface = container.get(MemoizationTechnique)
    reader: ReaderInterface = container.get(ReaderInterface)

    data = reader.read(os.path.join(os.getcwd(), "fixtures", "dataset_0.csv"))

    assert len(data) == 20

    for row in data:
        action_price: int = int(float(row['price']) * 100)
        if action_price <= 0:
            continue
        profit: int = int(action_price * (float(row['profit']) / 100))
        knapsack.add(Item(row['name'], action_price, profit))

    items, total = knapsack.resolve(50000)

    assert len(items) == 10
    total_weight = 0
    for item in items:
        total_weight += item.weight
    assert 50000 >= total_weight

