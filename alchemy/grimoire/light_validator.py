"""Validate light ingredients using the spellbook's own ingredient list."""

from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    """Accept text containing an allowed ingredient, ignoring case."""
    for allowed in light_spell_allowed_ingredients():
        if allowed in ingredients.lower():
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
