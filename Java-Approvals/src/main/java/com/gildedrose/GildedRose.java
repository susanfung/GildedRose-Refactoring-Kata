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
                final BackstagePasses itemName = new BackstagePasses();
                if (itemName.isItem(item)) {
                    itemName.updateItem(item);
                    continue;
                }
            }

            {
                final Sulfuras itemName = new Sulfuras();
                if (itemName.isItem(item)) {
                    itemName.updateItem(item);
                    continue;
                }
            }

            {
                final OtherItems itemName = new OtherItems();
                if (itemName.isItem(item)) {
                    itemName.updateItem(item);
                    continue;
                }
            }
        }
    }

}
