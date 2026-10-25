"""Read configuration without printing credentials or contacting services."""

import os


def main() -> None:
    """Load development settings while preserving environment overrides."""
    print("ORACLE STATUS: Consulting the configuration...")
    try:
        from dotenv import load_dotenv
    except ImportError:
        print("Missing python-dotenv. Install it with:")
        directory = os.path.dirname(os.path.abspath(__file__))
        print(f'python3 -m pip install -r "{directory}/requirements.txt"')
        return

    directory = os.path.dirname(os.path.abspath(__file__))
    env_path = os.path.join(directory, ".env")
    if not os.path.isfile(env_path):
        print("No .env found; using environment variables and defaults.")
    try:
        load_dotenv(env_path, override=False)
    except (OSError, UnicodeError):
        print("WARNING: Cannot read .env; using environment and defaults.")

    mode = os.getenv("MATRIX_MODE", "development").strip().lower()
    if mode not in ("development", "production"):
        print("Invalid MATRIX_MODE; expected development or production.")
        return
    default_level = "DEBUG" if mode == "development" else "WARNING"
    level = os.getenv("LOG_LEVEL", default_level).strip().upper()
    if level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
        print(f"Invalid LOG_LEVEL; using {default_level}.")
        level = default_level

    print(f"Mode: {mode}")
    print(f"Log Level: {level}")
    if mode == "development":
        print("Development diagnostics enabled; missing settings warn.")
    else:
        print("Production mode: complete configuration is required.")
        print("Detailed development diagnostics disabled.")

    complete = True
    for key in ("DATABASE_URL", "API_KEY", "ZION_ENDPOINT"):
        value = os.getenv(key, "").strip()
        placeholder = value == "replace-me" or "example.invalid" in value
        if not value or placeholder:
            complete = False
            print(f"[WARNING] {key}: missing or placeholder value")
        else:
            print(f"[OK] {key}: configured (value hidden)")

    print("Configuration only: no database, API or network checks performed.")
    if mode == "production" and not complete:
        print("Production startup blocked: supply all required settings.")
        return
    print("The Oracle has read the available configuration.")


if __name__ == "__main__":
    main()
