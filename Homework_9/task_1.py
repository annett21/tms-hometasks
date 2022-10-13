class Good:
    def __init__(self, goods_name, shop_name, price):
        self.__good_name = goods_name
        self.__shop_name = shop_name
        self.__price = price

    def __str__(self):
        return f"{self.__good_name}, { self.__shop_name}, {self.__price}"

    @property
    def good_name(self):
        return self.__good_name

    @property
    def shop_name(self):
        return self.__shop_name

    @property
    def price(self):
        return self.__price

    def __add__(self, other):
        return self.price + other.price


class Warehouse:
    def __init__(self, goods=None):
        self.__goods = goods or []

    def find_good(self, *, index=None, name=None):
        if index is None and name is None:
            raise ValueError("Expected at least 1 argument.")
        if index:
            return self.__goods[index]
        if name:
            for good in self.__goods:
                if good.good_name == name:
                    return good

    def sort_by_name(self):
        return sorted(self.__goods, key=lambda good: good.good_name)

    def sort_by_shop(self):
        return sorted(self.__goods, key=lambda good: good.shop_name)

    def sort_by_price(self):
        return sorted(self.__goods, key=lambda good: good.price)


good1 = Good("Phone", "Asos", 299)
good2 = Good("Cola", "Fixprice", 2)
good3 = Good("Skirt", "Ozon", 30)
good4 = Good("Luck", "Amazon", 4)

warehouse = Warehouse([good1, good2, good3, good4])
print(warehouse.find_good(index=2))
print(warehouse.find_good(name="Phone"))
print()
print([str(good) for good in warehouse.sort_by_name()])
print([str(good) for good in warehouse.sort_by_shop()])
print([str(good) for good in warehouse.sort_by_price()])
print()
print(good1 + good2)
