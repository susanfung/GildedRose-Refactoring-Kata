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

        
if __name__ == '__main__':
    unittest.main()
