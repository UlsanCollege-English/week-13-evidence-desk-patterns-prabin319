"""conftest.py — makes src/ importable for pytest in all environments."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))