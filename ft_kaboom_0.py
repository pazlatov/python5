"""Use the working grimoire package interface."""

import alchemy.grimoire


def main() -> None:
    """Demonstrate valid, invalid and case-insensitive light spells."""
    print("=== Kaboom 0 ===")
    for name, ingredients in (
        ("Fantasy", "Earth, wind and fire"),
        ("Mist", "WATER"),
        ("Empty", ""),
        ("Forbidden", "bats and frogs"),
    ):
        print(alchemy.grimoire.light_spell_record(name, ingredients))


if __name__ == "__main__":
    main()
