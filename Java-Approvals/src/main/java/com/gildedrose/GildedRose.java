package com.gildedrose;

class GildedRose {
    Item[] items;

    public GildedRose(Item[] items) {
        this.items = items;
    }

    public void updateQuality() {
        for (Item item : items) {
            {
                final AgedBrie itemName = new AgedBrie();
                if (itemName.isItem(item)) {
                    itemName.updateItem(item);
                    continue;
                }
            }

            {
                final BackstagePasses backstagePasses = new BackstagePasses();
                if (backstagePasses.isItem(item)) {
                    backstagePasses.updateItem(item);
                    continue;
                }
            }

            {
                final Sulfuras sulfuras = new Sulfuras();
                if (sulfuras.isItem(item)) {
                    sulfuras.updateItem(item);
                    continue;
                }
            }

            {
                final OtherItems otherItems = new OtherItems();
                if (otherItems.isItem(item)) {
                    otherItems.updateItem(item);
                    continue;
                }
            }
        }
    }

}
