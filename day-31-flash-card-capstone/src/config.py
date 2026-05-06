# ============================================================
# config.py
# Central configuration file for Flashy. Defines file paths
# for images, data, and application color settings.
# ============================================================
from pathlib import Path

# config.py lives in src/, so we go up two levels: src/ -> project_root/
BASE_DIR = Path(__file__).resolve().parent.parent


# --- Directory Paths ---
# The / operator here is a joiner operation
# BASE_DIR / "data" / "raw" is equivalent to os.path.join(BASE_DIR, "data", "raw")
DATA_DIR = BASE_DIR / "data"
IMAGE_DIR = BASE_DIR / "images"

# --- Canvas background color ---
BACKGROUND_COLOR = "#B1DDC6"

# --- UI Image filepaths ---
CARD_FRONT_IMAGE = str(IMAGE_DIR / "card_front.png")
CARD_BACK_IMAGE = str(IMAGE_DIR / "card_back.png")
RIGHT_BUTTON_IMAGE = str(IMAGE_DIR / "right.png")
WRONG_BUTTON_IMAGE = str(IMAGE_DIR / "wrong.png")
