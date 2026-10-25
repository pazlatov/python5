"""Report external dependency versions without crashing when unavailable."""

import importlib
import os


def main() -> None:
    """Inspect both declared dependencies and show installation commands."""
    print("REAGENT STATUS: Loading reagents...")
    ready = True
    for name in ("pandas", "numpy"):
        try:
            reagent = importlib.import_module(name)
            print(f"[OK] {name} ({reagent.__version__})")
        except (ImportError, OSError, ValueError) as error:
            ready = False
            print(f"[MISSING OR BROKEN] {name}: {error}")
    print("\npip vs Poetry:")
    print("requirements.txt declares dependencies; pip resolves at install.")
    print("pyproject.toml declares dependencies for Poetry.")
    print("Poetry locks resolved versions in poetry.lock for repeat installs.")
    if ready:
        print("All reagents present and accounted for.")
    else:
        directory = os.path.dirname(os.path.abspath(__file__))
        print("Install with pip:")
        print(f'python3 -m pip install -r "{directory}/requirements.txt"')
        print("Or install with Poetry (pyproject.toml is inside ex0):")
        print(f'poetry -C "{directory}" install')
        print(f'poetry -C "{directory}" run python loading.py')


if __name__ == "__main__":
    main()
