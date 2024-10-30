from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from .models import Hotel, Room

class HotelModelTest(TestCase):
    def setUp(self):
        Hotel.objects.create(name="Test Hotel", address="123 Test St", rating=4.5)

    def test_hotel_creation(self):
        hotel = Hotel.objects.get(name="Test Hotel")
        self.assertEqual(hotel.address, "123 Test St")
