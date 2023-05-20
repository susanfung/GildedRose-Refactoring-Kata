package com.gildedrose;

public class OtherItems implements ItemName {

    @Override
    public void updateItem(Item item) {
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

    @Override
    public boolean isItem(Item item) {
        return true;
    }
}
