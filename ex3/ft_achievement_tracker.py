class Player:
    def __init__(self, name: str, achievements: set = None) -> None:
        if name.__class__ != str:
            raise ValueError("Name must be a String !")

        self.name = name
        self.achievements = set() if achievements is None else achievements

    def add_ach(self, achievement: str) -> None:
        if achievement.__class__ != str:
            raise ValueError("Achievement must be a String !")
        self.achievements.add(achievement)

    def get_ach(self) -> set:
        return self.achievements


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    try:
        alice = Player("Alice")
        bob = Player("Bob")
        charlie = Player("Charlie")
    except ValueError as e:
        print("Error creating player:", e)
        return
    try:
        alice.add_ach("first_kill")
        alice.add_ach("level_10")
        alice.add_ach("treasure_hunter")
        alice.add_ach("speed_demon")
    except ValueError as e:
        print("Error adding achievement for Alice:", e)
        return

    try:
        bob.add_ach("first_kill")
        bob.add_ach("level_10")
        bob.add_ach("boss_slayer")
        bob.add_ach("collector")
    except ValueError as e:
        print("Error adding achievement for Bob:", e)
        return

    try:
        charlie.add_ach("level_10")
        charlie.add_ach("treasure_hunter")
        charlie.add_ach("speed_demon")
        charlie.add_ach("perfectionist")
        charlie.add_ach("boss_slayer")
    except ValueError as e:
        print("Error adding achievement for Charlie:", e)
        return

    print("Player alice achievements:", alice.get_ach())
    print("Player bob achievements:", bob.get_ach())
    print("Player charlie achievements:", charlie.get_ach())

    print("\n=== Achievement Analytics ===")

    all_achievements = (
        alice.get_ach()
        .union(bob.get_ach())
        .union(charlie.get_ach())
    )
    print("All unique achievements:", all_achievements)

    print("Total unique achievements:", len(all_achievements), "\n")

    common_all = (
        alice.get_ach()
        .intersection(bob.get_ach())
        .intersection(charlie.get_ach())
    )
    print("Common to all players:", common_all)

    rare_achievements = set(
        ach
        for ach in all_achievements
        if sum(
            ach in player.get_ach()
            for player in [alice, bob, charlie]
        ) == 1
    )
    print("Rare achievements (1 player):", rare_achievements, "\n")

    alice_bob_common = alice.get_ach().intersection(bob.get_ach())
    print("Alice vs Bob common:", alice_bob_common)

    alice_unique = alice.get_ach().difference(bob.get_ach())
    bob_unique = bob.get_ach().difference(alice.get_ach())

    print("Alice unique:", alice_unique)
    print("Bob unique:", bob_unique)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("An error occurred:", e)
