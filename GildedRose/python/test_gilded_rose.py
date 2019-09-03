# -*- coding: utf-8 -*-
import unittest
from gilded_rose import Store, Item
testCases = [
    {
        "name": "foo",
        "sellin": 10,
        "quality": 5,
        "results": {
            1: "foo, 9, 4",
            2: "foo, 8, 3",
            4: "foo, 6, 1",
            5: "foo, 5, 0",
            6: "foo, 4, 0"
        }
    }, {
        "name": "foo",
        "sellin": 6,
        "quality": 10,
        "results": {
            5: "foo, 1, 5",
            6: "foo, 0, 4",
            7: "foo, -1, 2",
            8: "foo, -2, 0",
            10: "foo, -4, 0"
        }
    }, {
        "name": "Aged Brie",
        "sellin": 5,
        "quality": 12,
        "results": {
            1: "Aged Brie, 4, 13",
            3: "Aged Brie, 2, 15",
            7: "Aged Brie, -2, 21",
            10: "Aged Brie, -5, 27"
        }
    }, {
        "name": "Aged Brie",
        "sellin": 5,
        "quality": 48,
        "results": {
            3: "Aged Brie, 2, 50"
        }
    }, {
        "name": "Sulfuras, Hand of Ragnaros",
        "sellin": 5,
        "quality": 20,
        "results": {
            1: "Sulfuras, Hand of Ragnaros, 5, 20",
            5: "Sulfuras, Hand of Ragnaros, 5, 20"
        }
    }, {
        "name": "Backstage passes to a TAFKAL80ETC concert",
        "sellin": 15,
        "quality": 10,
        "results": {
            1: "Backstage passes to a TAFKAL80ETC concert, 14, 11",
            4: "Backstage passes to a TAFKAL80ETC concert, 11, 14",
            7: "Backstage passes to a TAFKAL80ETC concert, 8, 19",
            10: "Backstage passes to a TAFKAL80ETC concert, 5, 25",
            13: "Backstage passes to a TAFKAL80ETC concert, 2, 34",
            14: "Backstage passes to a TAFKAL80ETC concert, 1, 37",
            15: "Backstage passes to a TAFKAL80ETC concert, 0, 40",
            17: "Backstage passes to a TAFKAL80ETC concert, -2, 0"
        }
    }
]


class GildedRoseTest(unittest.TestCase):
    def testRegular(self):
        items = [Item(x['name'], x['sellin'], x['quality']) for x in testCases]
        store = Store(items)
        for dayIndex in range(20):
            store.update_quality()
            for index, item in enumerate(testCases):
                result = item["results"].get(dayIndex + 1)
                if result:
                    self.assertEquals(result, str(items[index]))


if __name__ == "__main__":
    # items = [Item("foo", 10, 5)]
    # for i in range(10):
    #     update_quality(items)
    #     print(i+1, items[0])
    unittest.main()
