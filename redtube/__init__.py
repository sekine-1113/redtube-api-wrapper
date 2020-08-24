"""
TODO: データ取得数
TODO: 出力形式をインスタンス生成時に
"""

from .core import *
from .videos import Videos
from .additionals import Additionals


class RedTube(Videos, Additionals):
    """
    :param output_type (optional): json, xml / default json
    """

    def __init__(self, output_type="json"):
        Videos.__init__(self, output_type)
        Additionals.__init__(self, output_type)

__all__ = ["RedTube",]