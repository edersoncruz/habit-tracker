from pathlib import Path
import os

ROOT_DIR = Path(__file__).parent.parent
FILES_DIR = ROOT_DIR / 'files'
WINDOW_ICON_PATH = FILES_DIR / 'logo.png'
BASE_DIR = BASE_DIR = Path(__file__).resolve().parent.parent
HABITS_FILE = os.path.join(BASE_DIR, "files/habits.json")