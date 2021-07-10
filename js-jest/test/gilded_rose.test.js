const {Shop, Item} = require("../src/gilded_rose");

describe("Gilded Rose", function() {
  //System takes in item
  it("should foo", function() {
    const gildedRose = new Shop([new Item("foo", 0, 0)]);
    const items = gildedRose.updateQuality();
    expect(items[0].name).toBe("foo");
  });

  //Once the sell by date has passed, Quality degrades twice as fast
  it("if SellIn is negative one & Quality is four, Quality result should be two", function() {
    const gildedRose = new Shop([new Item("foo", -1, 4)]);
    const items = gildedRose.updateQuality();
    expect(items[0].quality).toBe(2);
  });

  //The Quality of an item is never negative
  it("if Quality is zero, Quality result should be zero", function() {
    const gildedRose = new Shop([new Item("foo", 0, 0)]);
    const items = gildedRose.updateQuality();
    expect(items[0].quality).toBe(0);
  });

  //"Aged Brie" actually increases in Quality the older it gets
  it("if Aged Brie SellIn is one and Quality is one, Quality result should be two", function() {
    const gildedRose = new Shop([new Item("Aged Brie", 1, 1)]);
    const items = gildedRose.updateQuality();
    expect(items[0].quality).toBe(2);
  });

  it("if Aged Brie SellIn is negative one and Quality is zero, Quality result should be two", function() {
    const gildedRose = new Shop([new Item("Aged Brie", -1, 0)]);
    const items = gildedRose.updateQuality();
    expect(items[0].quality).toBe(2);
  });

  //The Quality of an item is never more than 50
  it("if Aged Brie SellIn is one and Quality is fifty, Quality result should be fifty", function() {
    const gildedRose = new Shop([new Item("Aged Brie", 1, 50)]);
    const items = gildedRose.updateQuality();
    expect(items[0].quality).toBe(50);
  });

  //"Sulfuras", being a legendary item, never has to be sold or decreases in Quality
  it("if Sulfuras Quality is one, Quality result should be one", function() {
    const gildedRose = new Shop([new Item("Sulfuras, Hand of Ragnaros", 1, 1)]);
    const items = gildedRose.updateQuality();
    expect(items[0].quality).toBe(1);
  });

  it("if Sulfuras is SellIn is one, SellIn result should be one", function() {
    const gildedRose = new Shop([new Item("Sulfuras, Hand of Ragnaros", 1, 1)]);
    const items = gildedRose.updateQuality();
    expect(items[0].sellIn).toBe(1);
  });

  //"Backstage passes", like aged brie, increases in Quality as its SellIn value approaches;
  //Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
  //Quality drops to 0 after the concert
  it("if Backstage passes SellIn is eleven and Quality is zero, Quality result should be one", function() {
    const gildedRose = new Shop([new Item("Backstage passes to a TAFKAL80ETC concert", 11, 0)]);
    const items = gildedRose.updateQuality();
    expect(items[0].quality).toBe(1);
  });

  it("if Backstage passes SellIn is ten and Quality is zero, Quality result should be two", function() {
    const gildedRose = new Shop([new Item("Backstage passes to a TAFKAL80ETC concert", 10, 0)]);
    const items = gildedRose.updateQuality();
    expect(items[0].quality).toBe(2);
  });

  it("if Backstage passes SellIn is six and Quality is zero, Quality result should be two", function() {
    const gildedRose = new Shop([new Item("Backstage passes to a TAFKAL80ETC concert", 6, 0)]);
    const items = gildedRose.updateQuality();
    expect(items[0].quality).toBe(2);
  });

  it("if Backstage passes SellIn is five and Quality is zero, Quality result should be three", function() {
    const gildedRose = new Shop([new Item("Backstage passes to a TAFKAL80ETC concert", 5, 0)]);
    const items = gildedRose.updateQuality();
    expect(items[0].quality).toBe(3);
  });

  it("if Backstage passes SellIn is one and Quality is zero, Quality result should be three", function() {
    const gildedRose = new Shop([new Item("Backstage passes to a TAFKAL80ETC concert", 1, 0)]);
    const items = gildedRose.updateQuality();
    expect(items[0].quality).toBe(3);
  });

  it("if Backstage passes SellIn is zero and Quality is fifty, Quality result should be zero", function() {
    const gildedRose = new Shop([new Item("Backstage passes to a TAFKAL80ETC concert", 0, 50)]);
    const items = gildedRose.updateQuality();
    expect(items[0].quality).toBe(0);
  });

  it("if Backstage passes SellIn is negative one and Quality is fifty, Quality result should be zero", function() {
    const gildedRose = new Shop([new Item("Backstage passes to a TAFKAL80ETC concert", -1, 50)]);
    const items = gildedRose.updateQuality();
    expect(items[0].quality).toBe(0);
  });

  //"Conjured" items degrade in Quality twice as fast as normal items
  it("if Conjured Quality is two, Quality result should be zero", function() {
    const gildedRose = new Shop([new Item("Conjured", 1, 2)]);
    const items = gildedRose.updateQuality();
    expect(items[0].quality).toBe(0);
  });
});
