"""Imported modules/packages"""
import json
from functools import reduce
from pstats import Stats
from typing import List, Dict

from lib.knapsack.item import Item
from lib.logger.logger_interface import LoggerInterface


class Logger(LoggerInterface):
    """
    Logger implementation
    """
    def __init__(self):
        self.datasets: Dict[str, List] = {}


    def write(self):
        with open(f"docs/results.json", 'a') as file:
            file.write(
                json.dumps(self.datasets)
            )
            file.close()

    def log(self, dataset: str, algorithm: str, items: List[Item], stats: Stats):
        items.sort(key=lambda item: item.name)
        if dataset not in self.datasets:
            self.datasets[dataset] = []

        self.datasets[dataset].append({
            'algorithm': algorithm,
            'execution_time': round(stats.total_tt, 3),
            'items': list(map(lambda item: {'name': item.name, 'price': round(item.weight / 100, 2), 'profit': round(((item.value / 100)/(item.weight / 100)) * 100, 2)}, items)),
            'cost': round(reduce(lambda inc, item: inc + (item.weight / 100), items, 0), 2),
            'returns': round(reduce(lambda inc, item: inc + (item.value / 100), items, 0), 2)
        })
