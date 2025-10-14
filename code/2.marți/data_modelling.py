"""
ProductCategory:
 - id
 - name
# - slug

#name: Tricou de bumbac
#slug: tricou-de-bumbac

# - parent (default None)

# |- Electrocasnice
# |   |- Televizoare
# |   |- Laptop

Product:
 - id
 - name
 - purchase_price
 - sale_price
 - category_id

# Localities:
#  - id (postal_code)
#  - name
#  - county

Customer:
 - id
 - name
 - city
 #- locality

Sale:
 - id
 - timestamp
 - customer
 - productsale_collection
 - total (property)

# this will be a dictionary within `Sale`
# ProductSale:
#  - id
#  - sale
#  - product
#  - quantity
"""

"""
In computing there are two difficult problems:
- naming things
- cache invalidation
- off-by-one errors
"""

"""
ORM = object-relational mapper

Django (big framework)
SQLAlchemy

"""

import csv
import json
import os.path
from datetime import datetime
from utils import generate_id
from collections import defaultdict


class Model:
    def __init__(self, name):
        self.id = generate_id(name)
        self.name = name

    def as_dict(self):
        try:
            fields = self.EXPORT_FIELDS
        except AttributeError:
            return self.__dict__.copy()
        else:
            return {
                field: getattr(self, field)
                for field in fields
            }
        
    def to_json(self):
        # loads the object as a dict
        # and processes any "foreign keys"
        # and replaces them with their id
        data = self.as_dict()
        for k, v in data.items():
            if isinstance(v, Model):
                data[k] = v.id

        return json.dumps(data)

    def __repr__(self):
        return f"{self.__class__.__name__}(id={repr(self.id)})"

class ProductCategory(Model):
    # def __init__(self, name):
    #     self.id = generate_id(name)
    #     self.name = name
    pass

class Product(Model):
    EXPORT_FIELDS = (
        'id',
        'name',
        'purchase_price',
        'sale_price',
        'category',
    )

    def __init__(self,
                 name,
                 category,
                 purchase_price,
                 sale_price):
        
        super().__init__(name)

        self.purchase_price = purchase_price
        self.sale_price = sale_price
        self.category = category


        
cat1 = ProductCategory("Hrană animale")
prod1 = Product(name="Mâncare pisici",
                category=cat1,
                purchase_price=20,
                sale_price=32)

print(cat1.id)
print(prod1.id)


class WithAutoIncrementID:
    __AUTO_INCREMENT_NUM = 0

    @classmethod
    def __get_next_id(cls):
        cls.__AUTO_INCREMENT_NUM += 1
        return cls.__AUTO_INCREMENT_NUM

    def __init__(self):
        self.id = self.__get_next_id()

    def __repr__(self):
        return f"{self.__class__.__name__}(id={repr(self.id)})"


class Customer(WithAutoIncrementID):
    def __init__(self, name, city):
        super().__init__()

        self.city = city

    """
    # @property
    # def sales(self):
    #     # make some query to get all
    #     # sales for customer
    #     sales_collection = []
    #     return sales_collection
    """


class SaleClosedError(Exception):
    pass


SALES_LOG_FILE = "sales.csv"

class Sale(WithAutoIncrementID):
    def __init__(self, customer):
        super().__init__()

        self.customer = customer
        self.timestamp = datetime.now()

        # products and their quantities
        self.products = defaultdict(int)

        self.closed = False

    def __str__(self):
        return "%s(id=%s,total=%s)" % (self.__class__.__name__,
                                       self.id,
                                       self.total,
                                       )

    @property
    def total(self):
        # calculates the total value from
        # all products sold

        total = 0
        for product, quantity in self.products.items():
            total += product.sale_price * quantity

        return total

        ## alternativ:
        # return sum(
        #     product.sale_price * quantity
        #     for product, quantity in self.products.items()
        # )

    def add_product(self, product, quantity=1):
        if self.closed:
            raise SaleClosedError("Cannot add to a committed sale.")
        
        # add to self.products
        self.products[product] += quantity

    def commit(self):
        if self.closed:
            raise SaleClosedError("Cannot re-commit a sale.")

        # write the transaction to disk
        fresh_start = not os.path.exists(SALES_LOG_FILE)

        with open(SALES_LOG_FILE, 'a', encoding="utf-8", newline="\n") as fp:
            writer = csv.writer(fp)

            header = [
                "sale_id",
                "timestamp",
                "item_id",
                "customer_id",
                "city",
                "quantity",
                "unit_price",
            ]

            if fresh_start:
                writer.writerow(header)

            for product, quantity in self.products.items():
                row = (
                    self.id,
                    self.timestamp,
                    product.id,
                    self.customer.id,
                    self.customer.city,
                    quantity,
                    product.sale_price,
                )
                writer.writerow(row)

        # and disallow further modifications
        self.closed = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.commit()


c = Customer("John", "Cluj")
#c2 = Customer("Jane", "București")

prod1 = Product(name="Mâncare pisici",
                category=cat1,
                purchase_price=20,
                sale_price=32)

prod2 = Product(name="Iphone nou",
                category=cat1,
                purchase_price=200,
                sale_price=3200)


# s = Sale(c)

# s.add_product(prod1, 3)
# s.add_product(prod2, 1)

# print(s.total) # should be 32*2 + 3200 = 3264

# s.commit()


with Sale(c) as sale:
    sale.add_product(prod1, 3)
    sale.add_product(prod2, 1)

print(sale.total, sale.closed)