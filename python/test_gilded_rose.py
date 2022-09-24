# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose
from approvaltests.approvals import verify

class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("Quality degrades twice as fast", 0, 2), Item("Quality is never negative", 0, 0), Item("Aged Brie", 0, 0), Item("Quality never more than 50", 0, 52), Item("Sulfuras, Hand of Ragnaros", 0, 10), Item("Backstage passes to a TAFKAL80ETC concert", 12, 10), Item("Backstage passes to a TAFKAL80ETC concert", 10, 10), Item("Backstage passes to a TAFKAL80ETC concert", 4, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        verify(items)

        
if __name__ == '__main__':
    unittest.main()
