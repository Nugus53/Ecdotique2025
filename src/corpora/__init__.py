

from pathlib import Path
import importlib
import subprocess
import sys

print("Initializing the lib package corpora")

# Initialize some variables, configuration, etc.
config = {
    "version": "0.0.alpha",
    "author": "Jules Nuguet",
}

modules = ["collatex","Levenshtein","scipy","numpy","pandas","pprint"]
for module in modules:
    if importlib.util.find_spec(module) is None:
        print(f"Module '{module}' not found. Installing...")
        subprocess.run([sys.executable, "-m", "pip", "install", module], check=True)
    else:
        print(f"Module '{module}' is already installed.")

from .ach import achP
from .corpora import corporaMenu
from .latexDoc import LatexDoc
from .specif import specificite
__all__ = ["achP","corporaMenu","LatexDoc","specificite"]