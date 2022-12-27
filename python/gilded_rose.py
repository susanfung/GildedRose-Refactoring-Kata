# -*- coding: utf-8 -*-

items = ["Aged Brie", "Backstage passes to a TAFKAL80ETC concert"]
class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Sulfuras, Hand of Ragnaros":
                self.decrease_item_sell_in_by_1(item)
                if item.quality < 50:
                    if item.name in items:
                        if item.sell_in > 0:
                            if item.name == "Aged Brie":
                                self.increase_item_quality_by_1(item)
                            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                                if item.sell_in < 6:
                                    self.increase_item_quality_by_3(item)
                                elif item.sell_in < 10:
                                    self.increase_item_quality_by_2(item)
                                else:
                                    self.increase_item_quality_by_1(item)
                        else:
                            if item.name == "Aged Brie":
                                self.increase_item_quality_by_2(item)
                            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                                self.change_item_quality_to_zero(item)
                    elif item.quality > 0:
                        if item.sell_in < 0:
                            self.decrease_item_quality_by_2(item)
                        else:
                            self.decrease_item_quality_by_1(item)
                elif item.name == "Backstage passes to a TAFKAL80ETC concert" and item.sell_in < 1:
                    self.change_item_quality_to_zero(item)

    def decrease_item_quality_by_1(self, item):
        item.quality = item.quality - 1

    def decrease_item_quality_by_2(self, item):
        item.quality = item.quality - 2

    def change_item_quality_to_zero(self, item):
        item.quality = item.quality - item.quality

    def increase_item_quality_by_2(self, item):
        item.quality = item.quality + 2

    def increase_item_quality_by_3(self, item):
        item.quality = item.quality + 3

    def increase_item_quality_by_1(self, item):
        item.quality = item.quality + 1

    def decrease_item_sell_in_by_1(self, item):
        item.sell_in = item.sell_in - 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
