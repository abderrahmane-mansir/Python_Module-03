class Player:
    def __init__(self, name: str, achievements: set = set()) -> None:
        self.name = name
        self.achievements = achievements

    def add_ach(self, achievement: str) -> None:
        if achievement.__class__ != str:
            raise ValueError("please enter a String !")
        self.achievements.add(achievement)


def main():
    print("=== Achievement Tracker System ===")

    alice = {"first_kill", "level_10", "treasure_hunter", "speed_demon"}
    bob = {"first_kill", "level_10", "boss_slayer", "collector"}
    charlie = {"level_10", "treasure_hunter", "speed_demon", "perfectionist"}

    print("Player alice achievements:", alice)
    print("Player bob achievements:", bob)
    print("Player charlie achievements:", charlie)

    print("\n=== Achievement Analytics ===")

    all_achievements = alice.union(bob).union(charlie)
    print("All unique achievements:", all_achievements)

    print("Total unique achievements:", len(all_achievements))

    common_all = alice.intersection(bob).intersection(charlie)
    print("Common to all players:", common_all)

    alice_bob_common = alice.intersection(bob)
    print("Alice vs Bob common:", alice_bob_common)

    alice_unique = alice.difference(bob)
    bob_unique = bob.difference(alice)

    print("Alice unique:", alice_unique)
    print("Bob unique:", bob_unique)


if __name__ == "__main__":
    main()
