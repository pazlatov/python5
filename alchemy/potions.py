"""Combine root-level and package-level elements into potions."""

from elements import create_fire, create_water
from .elements import create_air, create_earth


def healing_potion() -> str:
    """Brew a potion using elements from this package."""
    return (
        f"Healing potion brewed with '{create_earth()}' "
        f"and '{create_air()}'"
    )


def strength_potion() -> str:
    """Brew a potion using the root-level elements module."""
    return (
        f"Strength potion brewed with '{create_fire()}' "
        f"and '{create_water()}'"
    )
