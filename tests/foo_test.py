"""Imported modules/packages"""
import pytest

from src.test import test


def test_foo():
    assert True == test()
