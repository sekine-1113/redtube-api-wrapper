from .core import *
from .videos import Videos
from .informations import Informations


class RedTube(Videos, Informations):

    def __init__(self):
        pass

__all__ = ["RedTube",]