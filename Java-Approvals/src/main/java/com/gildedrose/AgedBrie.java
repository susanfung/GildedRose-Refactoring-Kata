package com.gildedrose;

public class AgedBrie implements ItemName {

    @Override
    public void updateItem(Item item) {
        if (item.quality < 50) {
            item.quality = item.quality + 1;
        }

        item.sellIn = item.sellIn - 1;

        if (item.sellIn < 0) {
            if (item.quality < 50) {
                item.quality = item.quality + 1;
            }
        }
    }

    @Override
    public boolean isItem(Item item) {
        return item.name.equals("Aged Brie");
    }
}
