"""
TODO: データ取得数
TODO: 出力形式をインスタンス生成時に
"""

from .core import *
from .videos import Videos
from .additionals import Additionals


class RedTube(Videos, Additionals):
    pass

__all__ = ["RedTube",]