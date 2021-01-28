import unittest
from main import Product
from main import DataBase


class Test_Product(unittest.TestCase):
    def setUp(self):
        self.product = Product()

    def test_setCost(self):
        self.assertEqual(self.product.setCost(),self.product.privat_cost)

    def test_getSales(self):
        self.assertEqual(self.product.getSales(900)

class Test_DataBase(unittest.TestCase):
    def setUp(self):
        self.database = DataBase()

    def test_id(self):
        self.assertEqual(self.database.id(),self.database.articl)

if __name__ == "__main__":
  unittest.main()