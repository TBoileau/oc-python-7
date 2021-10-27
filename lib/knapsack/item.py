"""Imported modules/packages"""


class Item:
    """
    Class Item
    """

    def __init__(self, name: str, weight: int, value: int):
        """
        Constructor
        :param name:
        :param weight:
        :param value:
        """
        self.name: str = name
        self.weight: int = weight
        self.value: int = value

    @property
    def ratio(self) -> int:
        """
        Get item's ratio
        :return:
        """
        return self.value // self.weight

    def __lt__(self, other: "Item"):
        return self.ratio < other.ratio if self.ratio != other.ratio else self.value < other.value
