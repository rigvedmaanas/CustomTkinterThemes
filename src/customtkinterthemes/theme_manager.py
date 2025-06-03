from pathlib import Path

HERE = Path(__file__).parent
THEME_DIR = HERE / "Themes"
FONT_DIR = HERE / "Fonts"

def get(theme_name: str) -> Path:
    """
    Returns the path to the theme JSON file.
    """
    theme_path = THEME_DIR / f"{theme_name}.json"
    if not theme_path.exists():
        raise FileNotFoundError(f"Theme '{theme_name}' not found")
    validate_theme_fonts()
    return theme_path

def get_all_themes() -> list[str]:
    """
    Returns a list of theme names (without .json extension)
    by scanning the local themes directory on disk.
    """
    # Adjust this path depending on where this function is located
    base_dir = Path(__file__).parent  # directory of this script/module
    themes_dir = base_dir / "themes"

    if not themes_dir.exists() or not themes_dir.is_dir():
        print(f"Themes directory not found at {themes_dir}")
        return []

    theme_files = [f.stem for f in themes_dir.iterdir() if f.is_file() and f.suffix == ".json"]
    return theme_files


def get_font_path():
    return FONT_DIR


def check_font_exists(font_family: str) -> bool:
    import tkinter as tk
    from tkinter import font

    root = tk.Tk()
    root.withdraw()

    exists = font_family in list(font.families())
    root.destroy()
    return exists


def validate_theme_fonts():
    for font in ["HaxrCorp 4089"]:
        if not check_font_exists(font):
            print(f"{font} not installed. Please install it... Fonts dir: {FONT_DIR}")


