# -*- coding: utf-8 -*-


def handleAgesBrie(item):
    if item.quality < 50:
        item.quality += 1


def handleSulfuras(item):
    pass


def handleRegular(item):
    if item.sell_in > 0:
        item.quality -= 1
    else:
        item.quality -= 2
    item.quality = max(item.quality, 0)


def update_quality(items):
    for item in items:
        if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
            if item.name != "Sulfuras, Hand of Ragnaros":
                handleRegular(item)
        else:
            if item.quality < 50:
                item.quality = item.quality + 1
                if item.name == "Backstage passes to a TAFKAL80ETC concert":
                    if item.sell_in < 11:
                        if item.quality < 50:
                            item.quality = item.quality + 1
                    if item.sell_in < 6:
                        if item.quality < 50:
                            item.quality = item.quality + 1

        if item.name != "Sulfuras, Hand of Ragnaros":
            item.sell_in = item.sell_in - 1

        if item.sell_in < 0:
            if item.name != "Aged Brie":
                if item.name != "Backstage passes to a TAFKAL80ETC concert":
                    pass
                else:
                    item.quality = 0
            else:
                handleAgesBrie(item)
    return items


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
