"""Imported modules/packages"""
from abc import ABC

from lib.dependency_injection.container import ContainerInterface, Container


class Kernel(ABC):
    """
    Kernel class
    """

    def __init__(self):
        self.container: ContainerInterface = Container()

    def run(self):
        """
        Run app

        :return:
        """
        self.build(self.container)

    def build(self, container: ContainerInterface):
        """
        Build container

        :return:
        """
