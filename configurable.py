from mhm_parser import *


class Config:

    items = MHMParser.get_items("config.mhm", ["width", "height", "lang"])

    width = int(items[0])
    height = int(items[1])
    lang = items[2]


class Lang:

    @staticmethod
    def get_item(identification):
        return MHMParser.get_item("lang/" + Config.lang + ".mhm", identification)