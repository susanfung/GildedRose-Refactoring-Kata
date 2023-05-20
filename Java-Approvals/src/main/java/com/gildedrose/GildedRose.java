package com.gildedrose;

class GildedRose {
    Item[] items;

    public GildedRose(Item[] items) {
        this.items = items;
    }

    public void updateQuality() {
        for (Item item : items) {
            {
                AgedBrie agedBrie = new AgedBrie();
                if (agedBrie.isAgedBrie(item)) {
                    agedBrie.updateAgedBrie(item);
                    continue;
                }
            }

            {
                BackstagePasses backstagePasses = new BackstagePasses();
                if (backstagePasses.isBackstagePasses(item)) {
                    backstagePasses.updateBackstagePasses(item);
                    continue;
                }
            }

            if (new Sulfuras().isSulfuras(item)) {
                new Sulfuras().updateSulfuras(item);
                continue;
            }

            if (OtherItems.isItem(item)) {
                OtherItems.updateItem(item);
                continue;
            }
        }
    }

}
