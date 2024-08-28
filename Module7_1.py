from pprint import pprint
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        contents = file.read()
        file.close()
        return contents

    def add(self, *products):
        existing_products = self.get_products()
        for product in products:
            if product.name not in existing_products:
                file = open(self.__file_name, 'a')
                file.write(str(product) + '\n')
                file.close()
            else:
                print(f"Продукт {product.name} уже есть в магазине")



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)
print("Содержимое магазина:")
print(s1.get_products())

s2 = Shop()
s2.add(p1, p2, p3)
print("Содержимое магазина после второго запуска:")
print(s2.get_products())