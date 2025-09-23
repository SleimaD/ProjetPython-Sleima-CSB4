from package.game import Game

# Dummy class to simulate a character with attributes needed for attack tests
class Dummy:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

# Test that attacking reduces the defender's HP according to the defense formule
def test_attack_damage():
    g = Game()
    attacker = Dummy("Attacker", hp=100, attack=30, defense=0)
    defender = Dummy("Defender", hp=100, attack=0, defense=10)

    # Calculate expected damage reduction based on defender's defense
    reduction = defender.defense / (defender.defense + 60)
    # Calculate expected damage dealt, ensuring at least 1 damage
    expected = max(1, int(attacker.attack * (1 - reduction)))

    # Perform attack and check if defender's HP is reduced correctly
    g.attack(attacker, defender)
    assert defender.hp == 100 - expected