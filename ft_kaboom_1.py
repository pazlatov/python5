"""Demonstrate a real, intentionally uncaught circular-import failure."""


def main() -> None:
    """Import the dark spellbook and expose the expected ImportError."""
    print("=== Kaboom 1 ===", flush=True)
    print("Importing dark spellbook: expected ImportError", flush=True)
    from alchemy.grimoire.dark_spellbook import dark_spell_record

    print(dark_spell_record("Nightfall", "bats and arsenic"))


if __name__ == "__main__":
    main()
