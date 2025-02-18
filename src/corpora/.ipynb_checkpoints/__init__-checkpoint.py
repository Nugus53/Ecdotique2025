

from pathlib import Path
print("Initializing the lib package corpora")

# Initialize some variables, configuration, etc.
config = {
    "version": "0.0.alpha",
    "author": "Jules Nuguet",
}

from .ach import achP
from .corpora import corporaMenu
from .latexDoc import LatexDoc
from .specif import specificite
__all__ = ["achP","corporaMenu","LatexDoc","specificite"]