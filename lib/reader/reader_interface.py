"""Imported modules/packages"""
from abc import ABC
from typing import Any, Dict, List


class ReaderInterface(ABC):
    """
    Interface Reader
    """
    def read(self, path: str) -> List[Dict[str, Any]]:
        """
        Read file and return dictionary
        :param path:
        :return:
        """
