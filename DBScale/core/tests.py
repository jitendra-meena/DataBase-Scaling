from django.test import TestCase
from .models import Customer
class UserLoginTestCase(TestCase):
        def testProductModel(self):
            product = Customer.objects.create(name="ToyCar", price=800)
            self.assertEquals(str(product), 'ToyCar')
            print("IsInstance : ",isinstance(product,Customer))
            self.assertTrue(isinstance(product,Customer))

