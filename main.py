"""Imported modules/packages"""
import cProfile
import io
import os
import pstats
import sys
from typing import List, Dict, Any, Union

from lib.kernel import Kernel
from lib.knapsack.item import Item
from lib.knapsack.knapsack_factory_interface import KnapsackFactoryInterface
from lib.knapsack.knapsack_resolver_interface import KnapsackResolverInterface
from lib.logger.logger_interface import LoggerInterface
from lib.reader.reader_interface import ReaderInterface
from src.app_kernel import AppKernel
from src.knapsack.knapsack_factory import KnapsackFactory


def graph_calls(profile: cProfile.Profile, dataset: str, algorithm: str):
    stream = io.StringIO()
    sys.stdout = stream
    print(f'Dataset : {dataset}')
    print(f'Algorithm : {algorithm}')
    print(f'Graph calls')
    profile.print_stats()
    output = stream.getvalue()
    output.replace(os.path.normpath(os.path.join(os.getcwd(), "..", "..", "..", "profiles")), "")
    output.replace(sys.base_prefix, "").replace("\\", "/")
    file = open(os.path.join(os.getcwd(), 'profiles', dataset, algorithm, 'graph_calls.txt'), 'w')
    file.write(output)
    file.close()


def visualization(profile: cProfile.Profile, dataset: str, algorithm: str):
    stream = io.StringIO()
    stats = pstats.Stats(profile, stream=stream).sort_stats('cumulative')
    stats.print_stats()
    rem = os.path.normpath(os.path.join(os.getcwd(), "..", "..", "..", "profiles"))
    res = stream.getvalue().replace(rem, "")
    res.replace(sys.base_prefix, "").replace("\\", "/")
    try:
        os.mkdir(os.path.join(os.getcwd(), 'profiles', dataset))
    except:
        pass
    try:
        os.mkdir(os.path.join(os.getcwd(), 'profiles', dataset, algorithm))
    except:
        pass
    stats.dump_stats(os.path.join(os.getcwd(), 'profiles', dataset, algorithm, 'profile.prof'))
    stats.print_stats()

if __name__ == '__main__':
    kernel: Kernel = AppKernel()
    kernel.run()
    factory: KnapsackFactory = kernel.container.get(KnapsackFactoryInterface)
    reader: ReaderInterface = kernel.container.get(ReaderInterface)
    logger: LoggerInterface = kernel.container.get(LoggerInterface)

    datasets: Dict[str, List[str]] = {
        "dataset_0": [
            "dynamic_programming",
            "optimized_dynamic_programming",
            "greedy",
            "naive_recursive",
            "memoization_technique",
        ],
        "dataset_1": [
            "dynamic_programming",
            "optimized_dynamic_programming",
            "greedy",
        ],
        "dataset_2": [
            "dynamic_programming",
            "optimized_dynamic_programming",
            "greedy",
        ],
    }

    for dataset, knapsacks in datasets.items():
        data = reader.read(os.path.join(os.getcwd(), "fixtures", f"{dataset}.csv"))

        def create_item(row: Dict[str, Any]) -> Union[None, Item]:
            action_price: int = int(float(row['price']) * 100)
            if action_price <= 0:
                return None
            profit: int = int(action_price * (float(row['profit']) / 100))
            return Item(row['name'], action_price, profit)

        dataset_items: List[Item] = list(filter(lambda item: item is not None, map(create_item, data)))
        dataset_items.sort(key=lambda item: item.value, reverse=True)

        for knapsack_name in knapsacks:
            knapsack: KnapsackResolverInterface = factory.create(knapsack_name)
            knapsack.items = dataset_items
            profile: cProfile.Profile = cProfile.Profile()
            profile.enable()
            items, total = knapsack.resolve(50000)
            profile.disable()
            visualization(profile, dataset, knapsack_name)
            graph_calls(profile, dataset, knapsack_name)
            logger.log(dataset, knapsack_name, items, pstats.Stats(profile))

    logger.write()

