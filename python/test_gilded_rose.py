# -*- coding: utf-8 -*-
import unittest

from approvaltests import verify_all_combinations

from gilded_rose import Item, GildedRose


def create_items(name, sell_in, quality):
    items = [Item(name, sell_in, quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    return items[0]

class GildedRoseTest(unittest.TestCase):
    def test_sell_in_decreases_by_one(self):
        name = ["foo"]
        sell_in = [1, 0]
        quality = [2]
        verify_all_combinations(lambda a, b, c: create_items(a, b, c), [name, sell_in, quality])
    def test_quality_decreases_by_2_when_sell_in_less_than_or_equal_to_zero(self):
        name = ["foo"]
        sell_in = [1, 0, -1]
        quality = [2]
        verify_all_combinations(lambda a, b, c: create_items(a, b, c), [name, sell_in, quality])

    def test_quality_is_never_negative(self):
        name = ["foo"]
        sell_in = [1, 0, -1]
        quality = [0]
        verify_all_combinations(lambda a, b, c: create_items(a, b, c), [name, sell_in, quality])

    def test_quality_for_items(self):
        name = ["Aged Brie", "Sulfuras, Hand of Ragnaros", "Backstage passes to a TAFKAL80ETC concert"]
        sell_in = [11, 10, 9, 5, 4, 0, -1]
        quality = [0, 50]
        verify_all_combinations(lambda a, b, c: create_items(a, b, c), [name, sell_in, quality])

        
if __name__ == '__main__':
    unittest.main()
