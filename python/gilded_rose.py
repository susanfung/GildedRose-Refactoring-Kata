# -*- coding: utf-8 -*-

items = ["Aged Brie", "Backstage passes to a TAFKAL80ETC concert"]
class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
                if item.quality < 50:
                    if item.name in items:
                        if item.sell_in > 0:
                            if item.name == "Aged Brie":
                                item.quality = item.quality + 1
                            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                                if item.sell_in < 6:
                                    item.quality = item.quality + 3
                                elif item.sell_in < 10:
                                    item.quality = item.quality + 2
                                else:
                                    item.quality = item.quality + 1
                        else:
                            if item.name == "Aged Brie":
                                item.quality = item.quality + 2
                            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                                item.quality = item.quality - item.quality
                    elif item.quality > 0:
                        if item.sell_in < 0:
                            item.quality = item.quality - 2
                        else:
                            item.quality = item.quality - 1
                elif item.name == "Backstage passes to a TAFKAL80ETC concert" and item.sell_in < 1:
                    item.quality = item.quality - item.quality

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
