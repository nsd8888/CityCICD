from django.test import TestCase
from .models import City_Info

# Create your tests here.

class cityinfoTestCase(TestCase):
    def setUp(self):
        pass
        
    def test_model_creation(self):
        City_Info.objects.create(City='Test',Population=234)
        self.assertEqual(City_Info.objects.count(), 1)