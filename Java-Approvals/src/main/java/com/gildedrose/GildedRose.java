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

            if (isSulfuras(item)) {
                updateSulfuras(item);
                continue;
            }

            if (isItem(item)) {
                updateItem(item);
                continue;
            }
        }
    }

    private static boolean isItem(Item item) {
        return true;
    }

    private static boolean isSulfuras(Item item) {
        return item.name.equals("Sulfuras, Hand of Ragnaros");
    }

    private void updateSulfuras(Item item) {
        return;
    }

    private static void updateItem(Item item) {
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

}
