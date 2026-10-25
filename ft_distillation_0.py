"""Demonstrate from-import syntax for potion functions."""

from alchemy.potions import healing_potion, strength_potion


def main() -> None:
    """Display both potions."""
    print("=== Distillation 0 ===")
    print(f"Testing strength_potion: {strength_potion()}")
    print(f"Testing healing_potion: {healing_potion()}")


if __name__ == "__main__":
    main()
