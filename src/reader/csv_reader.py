"""Imported modules/packages"""
import csv
from typing import Any, Dict, List

from lib.reader.reader_interface import ReaderInterface


class CsvReader(ReaderInterface):
    """
    Class CsvReader
    """

    def read(self, path: str) -> List[Dict[str, Any]]:
        with open(path, mode="r", encoding="utf8") as csv_file:
            data: List[List[Any]] = list(csv.reader(csv_file, delimiter=","))
            headers: List[str] = data[0]
            response: List[Dict[str, Any]] = []
            for row in data[1:]:
                response.append(dict(zip(headers, row)))
            return response
