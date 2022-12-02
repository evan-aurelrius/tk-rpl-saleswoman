from django.test import TestCase
from .models import Product
from .views import *

class ProductModelTest(TestCase):
    def testProductModelExist(self):
        numberOfSavedProduct = Product.objects.count()
        self.assertEqual(0, numberOfSavedProduct)
    
    def testProductAttributesIsValid(self):
        product1 = Product(name="Laptop",brand="Lenova",variant="Gaming",price=15000000,stock=50)
        self.assertEqual(product1.name, "Laptop")
        self.assertEqual(product1.brand, "Lenova")
        self.assertEqual(product1.variant, "Gaming")
        self.assertEqual(product1.price, 15000000)
        self.assertEqual(product1.stock, 50)
        
class ProductViewTest(TestCase):
    def testProductIsSavedSuccessfully(self):
        product1 = Product(name="Laptop",brand="Lenova",variant="Gaming",price=15000000,stock=50)
        product2 = Product(name="Notebook",brand="Mec Buk",variant="Student",price=18000000,stock=30)
        product1.save()
        product2.save()
        numberOfSavedProduct = Product.objects.count()
        self.assertEqual(2, numberOfSavedProduct)
        
    def testProductIsRetrievableById(self):
        product1 = Product(name="Laptop",brand="Lenova",variant="Gaming",price=15000000,stock=50)
        product1.save()
        retrievedProduct = getProductDetails(1)
        self.assertEqual(product1, retrievedProduct)