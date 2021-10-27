"""Imported modules/packages"""
from lib.dependency_injection.container_interface import ContainerInterface
from lib.kernel import Kernel
from lib.reader.reader_interface import ReaderInterface
from src.reader.csv_reader import CsvReader


class AppKernel(Kernel):
    """
    AppKernel class
    """

    def build(self, container: ContainerInterface):
        container.alias(ReaderInterface, CsvReader)
