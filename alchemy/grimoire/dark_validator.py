"""Intentionally request a name from a partially initialized spellbook."""

from .dark_spellbook import dark_spell_allowed_ingredients


def dark_validate_ingredients(ingredients: str) -> str:
    """Check dark ingredients if module initialization could finish."""
    for allowed in dark_spell_allowed_ingredients():
        if allowed in ingredients.lower():
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
