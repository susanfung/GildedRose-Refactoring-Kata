package com.gildedrose;

public class Sulfuras implements ItemName {

    @Override
    public void updateItem(Item item) {
        return;
    }

    @Override
    public boolean isItem(Item item) {
        return item.name.equals("Sulfuras, Hand of Ragnaros");
    }
}
