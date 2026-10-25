"""Demonstrate a package interface and an intentional missing attribute."""

import alchemy


def main() -> None:
    """Show that earth was not re-exported at package level."""
    print("=== Alembic 1 ===")
    print(f"Testing create_air: {alchemy.create_air()}")
    print("Testing unexposed create_earth (expected AttributeError):")
    try:
        print(alchemy.create_earth())
    except AttributeError as error:
        print(f"Expected AttributeError: {error}")


if __name__ == "__main__":
    main()
