import vending_machine
import pytest


def test_return_change():
    assert vending_machine.return_change(0)
    balance = []
