"""Import the validator before its dependency exists: deliberately broken."""

from .dark_validator import dark_validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    """List the dark ingredients (unreachable during the broken import)."""
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    """Describe a dark spell if the deliberate import cycle were repaired."""
    result = dark_validate_ingredients(ingredients)
    if result.endswith(" - VALID"):
        return f"Spell recorded: {spell_name} ({result})"
    return f"Spell rejected: {spell_name} ({result})"
