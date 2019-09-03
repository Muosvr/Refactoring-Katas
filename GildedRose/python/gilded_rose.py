# -*- coding: utf-8 -*-


class Store:
    def __init__(self, items):
        self.items = items

    def _handleAgesBrie(self, item):
        if item.sell_in > 0:
            item.quality += 1
        else:
            item.quality += 2
        item.quality = min(50, item.quality)

    def _handleSulfuras(self, item):
        pass

    def _handleRegular(self, item):
        if item.sell_in > 0:
            item.quality -= 1
        else:
            item.quality -= 2
        item.quality = max(item.quality, 0)

    def _handleBackstagePasses(self, item):
        tenDays = 10
        fiveDays = 5
        dayOf = 0

        if tenDays < item.sell_in:
            item.quality += 1
        elif fiveDays < item.sell_in <= tenDays:
            item.quality += 2
        elif dayOf < item.sell_in <= fiveDays:
            item.quality += 3
        else:
            item.quality = 0
        item.quality = min(50, item.quality)

    def update_quality(self):
        items = self.items
        for item in items:
            if item.name == "Aged Brie":
                self._handleAgesBrie(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self._handleBackstagePasses(item)
            elif item.name == "Sulfuras, Hand of Ragnaros":
                self._handleSulfuras(item)
            else:
                self._handleRegular(item)

            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
        return items


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
