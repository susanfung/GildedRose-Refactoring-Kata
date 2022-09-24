# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Sulfuras, Hand of Ragnaros":
                if item.name == "Aged Brie":
                    if item.quality < 50:
                        self.quality_increase_by_one(item)
                elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                    self.quality_increase_by_one(item)
                    if item.sell_in < 11:
                        if item.quality < 50:
                            self.quality_increase_by_one(item)
                    if item.sell_in < 6:
                        if item.quality < 50:
                            self.quality_increase_by_one(item)
                else:
                    if item.quality > 0:
                        self.quality_decrease_by_one(item)
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name == "Backstage passes to a TAFKAL80ETC concert":
                    item.quality = item.quality - item.quality
                elif item.name == "Aged Brie":
                    if item.quality < 50:
                        self.quality_increase_by_one(item)
                else:
                    if item.quality > 0:
                        self.quality_decrease_by_one(item)

    def quality_increase_by_one(self, item):
        item.quality = item.quality + 1

    def quality_decrease_by_one(self, item):
        item.quality = item.quality - 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
