"""Demonstrate importing a root-level module."""

import elements


def main() -> None:
    """Create fire using a module-qualified name."""
    print("=== Alembic 0 ===")
    print("Using: import elements")
    print(f"Testing create_fire: {elements.create_fire()}")


if __name__ == "__main__":
    main()
