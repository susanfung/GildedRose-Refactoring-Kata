# -*- coding: utf-8 -*-
import unittest

from approvaltests import verify_all_combinations

from gilded_rose import Item, GildedRose


def create_items(name, sellIn, quality):
    items = [Item(name, sellIn, quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    return items[0]

class GildedRoseTest(unittest.TestCase):
    def test_sellIn_decreases_by_one(self):
        name = ["foo"]
        sellIn = [1, 0]
        quality = [2]
        verify_all_combinations(lambda a, b, c: create_items(a, b, c), [name, sellIn, quality])
    def test_quality_decreases_by_2_when_sellIn_less_than_or_equal_to_zero(self):
        name = ["foo"]
        sellIn = [1, 0, -1]
        quality = [2]
        verify_all_combinations(lambda a, b, c: create_items(a, b, c), [name, sellIn, quality])

    def test_quality_is_never_negative(self):
        name = ["foo"]
        sellIn = [1, 0, -1]
        quality = [0]
        verify_all_combinations(lambda a, b, c: create_items(a, b, c), [name, sellIn, quality])

    def test_quality_for_items(self):
        name = ["Aged Brie", "Sulfuras, Hand of Ragnaros", "Backstage passes to a TAFKAL80ETC concert"]
        sellIn = [11, 10, 9, 5, 4, 0, -1]
        quality = [0, 50]
        verify_all_combinations(lambda a, b, c: create_items(a, b, c), [name, sellIn, quality])

        
if __name__ == '__main__':
    unittest.main()
