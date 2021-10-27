"""Imported modules/packages"""
import os
from abc import ABC

from dotenv import load_dotenv

from lib.dependency_injection.container import ContainerInterface, Container


class Kernel(ABC):
    """
    Kernel class
    """

    def __init__(self):
        load_dotenv(".env")
        load_dotenv(f".env.{os.getenv('APP_ENV')}")
        self.__container: ContainerInterface = Container()

    def run(self):
        """
        Run app

        :return:
        """
        self.build(self.__container)

    def build(self, container: ContainerInterface):
        """
        Build container

        :return:
        """
