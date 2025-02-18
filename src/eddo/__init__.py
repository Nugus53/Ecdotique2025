
import logging

from pathlib import Path
print("Initializing the lib package")

import importlib
import subprocess
import sys

# Initialize some variables, configuration, etc.
config = {
    "version": "0.0.alpha",
    "author": "Jules Nuguet",
}

modules = ["spacy_udpipe"]
for module in modules:
    if importlib.util.find_spec(module) is None:
        print(f"Module '{module}' not found. Installing...")
        subprocess.run([sys.executable, "-m", "pip", "install", module], check=True)
    else:
        print(f"Module '{module}' is already installed.")

from .freq import get_frequence
__all__ = ["get_frequence"]

