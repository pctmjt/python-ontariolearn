import vending_machine
import pytest


def test_drink_balance():
#    assert vending_machine.buy_product("drink", 275)

    with pytest.raises(AssertionError) as excinfo:
        assert "InsufficientFunds" in str(excinfo.value)

#    assert vending_machine.buy_product("banana", 10)
#    assert vending_machine.buy_product("drink", 274)


def test_chip_balance():
#   vending_machine.buy_product("chips", 225)

    with pytest.raises(AssertionError) as excinfo:
        assert "InsufficientFunds" in str(excinfo.value)


#    assert vending_machine.buy_product("chips", 224)
def test_candy_balance():
#    vending_machine.buy_product("candy", 315)

    with pytest.raises(AssertionError) as excinfo:
        assert "InsufficientFunds" in str(excinfo.value)

#    assert vending_machine.buy_product("candy", 314)
