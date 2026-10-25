"""Delay the validator import until the spellbook is initialized."""


def light_spell_allowed_ingredients() -> list[str]:
    """List ingredients that can validate a light spell."""
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    """Validate a spell after module initialization has finished."""
    from .light_validator import validate_ingredients

    result = validate_ingredients(ingredients)
    if result.endswith(" - VALID"):
        return f"Spell recorded: {spell_name} ({result})"
    return f"Spell rejected: {spell_name} ({result})"
