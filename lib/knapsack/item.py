"""Imported modules/packages"""
from typing import Union


class Item:
    """
    Class Item
    """

    def __init__(self, name: str, weight: int, value: Union[int,float]):
        """
        Constructor
        :param name:
        :param weight:
        :param value:
        """
        self.name: str = name
        self.weight: int = weight
        self.value: Union[int,float] = value

    @property
    def ratio(self) -> int:
        """
        Get item's ratio
        :return:
        """
        return self.value // self.weight

    def __lt__(self, other: "Item"):
        return self.ratio < other.ratio if self.ratio != other.ratio else self.value < other.value
