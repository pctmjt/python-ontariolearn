import vending_machine

def test_five_cents():
    inserted_coins = []
    vending_machine.insert_coin((5, 10, 25, 50, 100, 200), inserted_coins)

def test_append_inserted():
    inserted_coins = []

