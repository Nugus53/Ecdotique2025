
import logging

from pathlib import Path
print("Initializing the lib package widget")

# Initialize some variables, configuration, etc.
config = {
    "version": "0.0.alpha",
    "author": "Jules Nuguet",
}

from .screen import ashMenu,Partition
__all__ = ["ashMenu","Partition"]