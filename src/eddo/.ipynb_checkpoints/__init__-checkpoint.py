
import logging

from pathlib import Path
print("Initializing the lib package")

# Initialize some variables, configuration, etc.
config = {
    "version": "0.0.alpha",
    "author": "Jules Nuguet",
}

from .freq import get_frequence
__all__ = ["get_frequence"]