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
                if (agedBrie.isItem(item)) {
                    agedBrie.updateItem(item);
                    continue;
                }
            }

            {
                BackstagePasses backstagePasses = new BackstagePasses();
                if (backstagePasses.isItem(item)) {
                    backstagePasses.updateBackstagePasses(item);
                    continue;
                }
            }

            {
                Sulfuras sulfuras = new Sulfuras();
                if (sulfuras.isSulfuras(item)) {
                    sulfuras.updateSulfuras(item);
                    continue;
                }
            }

            {
                OtherItems otherItems = new OtherItems();
                if (otherItems.isItem(item)) {
                    otherItems.updateItem(item);
                    continue;
                }
            }
        }
    }

}
