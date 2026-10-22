"""The Gate: an entry point for travellers from all around the world.

Every visitor is admitted. The gate opens a window onto the nearest
monasteries, temples, research centres and folk houses, quotes fees for a
visit or a stay, and keeps a knowledge centre of the artefacts and tales
visitors bring.
"""
from .gate import Visitor, VisaState, admit, open_window
from .fees import quote
from .knowledge import KnowledgeCentre

__all__ = ["Visitor", "VisaState", "admit", "open_window", "quote", "KnowledgeCentre"]
