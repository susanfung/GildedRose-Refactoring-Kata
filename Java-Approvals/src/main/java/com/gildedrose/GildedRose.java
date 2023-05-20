package com.gildedrose;

class GildedRose {
    Item[] items;

    public GildedRose(Item[] items) {
        this.items = items;
    }

    public void updateQuality() {
        for (Item item : items) {
            if (AgedBrie.isAgedBrie(item)) {
                AgedBrie.updateAgedBrie(item);
                continue;
            }

            if (BackstagePasses.isBackstagePasses(item)) {
                BackstagePasses.updateBackstagePasses(item);
                continue;
            }

            if (Sulfuras.isSulfuras(item)) {
                Sulfuras.updateSulfuras(item);
                continue;
            }

            if (OtherItems.isItem(item)) {
                OtherItems.updateItem(item);
                continue;
            }
        }
    }

}
