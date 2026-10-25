"""Describe the active interpreter and virtual environment."""

import os
import site
import sys


def main() -> None:
    """Show isolation status and virtual environment setup instructions."""
    isolated = sys.prefix != sys.base_prefix
    status = "The laboratory is sealed" if isolated else "Working in the open"
    print(f"LABORATORY STATUS: {status}")
    print(f"Current Python: {sys.executable}")
    print(f"Global Python prefix: {sys.base_prefix}")
    print(f"Active Python prefix: {sys.prefix}")
    if isolated:
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}")
        print("SUCCESS: You are working in a virtual environment!")
    else:
        print("Virtual Environment: None detected")
        print("WARNING: Packages installed here are outside a project venv.")
        print("To seal the laboratory, run:")
        print("python3 -m venv lab_env")
        print("source lab_env/bin/activate  # Unix")
        print(r"lab_env\Scripts\activate  # Windows cmd")
        print("Then run this program again.")
    print("Active package locations:")
    for location in site.getsitepackages():
        print(f"  {location}")
    print("Base/global package locations:")
    for location in site.getsitepackages([sys.base_prefix]):
        print(f"  {location}")
    print("A venv isolates installed packages, not files or network access.")


if __name__ == "__main__":
    main()
