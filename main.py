"""Imported modules/packages"""
from lib.kernel import Kernel
from src.app_kernel import AppKernel


if __name__ == '__main__':
    kernel: Kernel = AppKernel()
    kernel.run()
