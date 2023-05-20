package com.gildedrose;

public class OtherItems {

    public static void updateItem(Item item) {
        if (item.quality > 0) {
            item.quality = item.quality - 1;
        }

        item.sellIn = item.sellIn - 1;

        if (item.sellIn < 0) {
            if (item.quality > 0) {
                item.quality = item.quality - 1;
            }
        }
    }

    public boolean isItem(Item item) {
        return true;
    }
}
