class Item {
  constructor(name, sellIn, quality){
    this.name = name;
    this.sellIn = sellIn;
    this.quality = quality;
  }
}

class Shop {
  constructor(items=[]){
    this.items = items;
  }

  subtractOne(x) {
    return x - 1;
  }

  addOne(x) {
    return x + 1;
  }

  updateQuality() {
    for (let i = 0; i < this.items.length; i++) {
      if (this.items[i].name != 'Sulfuras, Hand of Ragnaros') {
        if (this.items[i].name != 'Conjured') {
          if (this.items[i].name != 'Aged Brie' && this.items[i].name != 'Backstage passes to a TAFKAL80ETC concert' && this.items[i].quality > 0) {
            this.items[i].quality = this.subtractOne(this.items[i].quality);
          } else {
            if (this.items[i].quality < 50) {
              this.items[i].quality = this.addOne(this.items[i].quality);
  
              if (this.items[i].name == 'Backstage passes to a TAFKAL80ETC concert') {
                if (this.items[i].sellIn < 11 && this.items[i].quality < 50) {
                  this.items[i].quality = this.addOne(this.items[i].quality);
                }
  
                if (this.items[i].sellIn < 6 && this.items[i].quality < 50) {
                  this.items[i].quality = this.addOne(this.items[i].quality);
                }
              }
            }
          }
        } else {
          this.items[i].quality = this.items[i].quality - 2;
        }

        this.items[i].sellIn = this.items[i].sellIn - 1;

        if (this.items[i].sellIn < 0) {
          if (this.items[i].name != 'Aged Brie') {
            if (this.items[i].name != 'Backstage passes to a TAFKAL80ETC concert') {
              if (this.items[i].quality > 0) {
                this.items[i].quality = this.subtractOne(this.items[i].quality);
              }
            } else {
              this.items[i].quality = this.items[i].quality - this.items[i].quality;
            }
          } else {
            if (this.items[i].quality < 50) {
              this.items[i].quality = this.addOne(this.items[i].quality);
            }
          }
        }
      }
      }

    return this.items;
  }
}

module.exports = {
  Item,
  Shop
}
