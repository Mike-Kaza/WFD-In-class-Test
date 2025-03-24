import unittest
from PartA import House, Apartment

class TestHouse(unittest.TestCase):
    def setUp(self):
        self.house = House(123, "Casta", "Latchford", 3, 250000)
        self.apartment = Apartment(456, "Castle", "Field", 2, 180000, 5, True)
    
    def test_instance_of_house(self):
        self.assertIsInstance(self.house, House)
    
    def test_instance_of_apartment(self):
        self.assertIsInstance(self.apartment, Apartment)
    
    def test_not_instance_of_house(self):
        self.assertNotIsInstance(self.apartment, House)  
    
    def test_objects_identical(self):
        another_house = self.house
        self.assertIs(self.house, another_house)
    
    def test_update_house_number(self):
        self.house.update_house_number(456)
        self.assertEqual(self.house.house_number, 456)
    
    def test_update_price(self):
        self.house.update_price(300000)
        self.assertEqual(self.house.price, 300000)
    
    def test_update_floor(self):
        self.apartment.update_floor(7)
        self.assertEqual(self.apartment.floor, 7)
    
    def test_update_has_elevator(self):
        self.apartment.update_has_elevator(False)
        self.assertFalse(self.apartment.has_elevator)
    
if __name__ == "__main__":
    unittest.main()
