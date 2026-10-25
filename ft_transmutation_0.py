"""Import a nested module using its complete dotted name."""

import alchemy.transmutation.recipes


def main() -> None:
    """Display the transmutation recipe."""
    print("=== Transmutation 0 ===")
    recipe = alchemy.transmutation.recipes.lead_to_gold()
    print(f"Testing lead to gold: {recipe}")


if __name__ == "__main__":
    main()
