"""Imported modules/packages"""
import os

from src.reader.csv_reader import CsvReader


def test_read_csv():
    csv_reader: CsvReader = CsvReader()
    data = csv_reader.read(os.path.join(os.getcwd(), "fixtures", "dataset_0.csv"))
    assert len(data) == 20
