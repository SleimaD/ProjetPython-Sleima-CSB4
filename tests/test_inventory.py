from package.items import Item, Inventory

class DummyHero:
    def __init__(self):
        # Initialize hero with current and max HP
        self.hp = 80
        self.max_hp = 100

def test_use_item_effect():
    # Create inventory and hero instances
    inv = Inventory()
    hero = DummyHero()

    # Define a healing effect function
    def heal(h):
        h.hp = min(h.hp + 20, h.max_hp)

    # Add a healing potion to inventory
    inv.add_item(Item("Potion", effect=heal))
    assert len(inv.items) == 1  # Confirm item added

    # Use the potion on hero and check results
    used = inv.use_item("Potion", hero)
    assert used is True
    assert len(inv.items) == 0  # Item removed after use
    assert hero.hp == 100       # Hero HP healed correctly

def test_use_item_unknown():
    # Create inventory and hero instances
    inv = Inventory()
    hero = DummyHero()

    # Attempt to use an unknown item
    used = inv.use_item("Unknown", hero)
    assert used is False  # Should return False if item not found