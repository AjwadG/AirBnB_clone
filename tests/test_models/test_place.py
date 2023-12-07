#!/usr/bin/python3
""" Unittest for Place """
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """
    TestPlace
    """

    def setUp(self):
        """
        setUp
        """
        self.place = Place()

    def tearDown(self):
        """
        tearDown
        """
        del self.place

    def test_inheritance(self):
        """
        test_inheritance
        """
        self.assertIsInstance(self.place, BaseModel)

    def test_attributes(self):
        """
        test_attributes
        """
        self.assertTrue(hasattr(self.place, 'id'))
        self.assertTrue(hasattr(self.place, 'created_at'))
        self.assertTrue(hasattr(self.place, 'updated_at'))
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertTrue(hasattr(self.place, 'longitude'))
        self.assertTrue(hasattr(self.place, 'amenity_ids'))

    def test_default_values(self):
        """
        test_default_values
        """
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_str_representation(self):
        """
        test_str_representation
        """
        expected_output = f"[Place] ({self.place.id}) {self.place.__dict__}"
        self.assertEqual(str(self.place), expected_output)

    def test_edge_case_empty_attributes(self):
        """
        test_edge_case_empty_attributes
        """
        self.place.city_id = ""
        self.place.user_id = ""
        self.place.name = ""
        self.place.description = ""
        self.place.number_rooms = 0
        self.place.number_bathrooms = 0
        self.place.max_guest = 0
        self.place.price_by_night = 0
        self.place.latitude = 0.0
        self.place.longitude = 0.0
        self.place.amenity_ids = []
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_edge_case_non_empty_attributes(self):
        """
        test_edge_case_non_empty_attributes
        """
        self.place.city_id = "city1"
        self.place.user_id = "user1"
        self.place.name = "house"
        self.place.description = "Two Bedroom Suite"
        self.place.number_rooms = 2
        self.place.number_bathrooms = 2
        self.place.max_guest = 4
        self.place.price_by_night = 1000
        self.place.latitude = 12.78
        self.place.longitude = 31.32
        self.place.amenity_ids = [12, 34]
        self.assertEqual(self.place.city_id, "city1")
        self.assertEqual(self.place.user_id, "user1")
        self.assertEqual(self.place.name, "house")
        self.assertEqual(self.place.description, "Two Bedroom Suite")
        self.assertEqual(self.place.number_rooms, 2)
        self.assertEqual(self.place.number_bathrooms, 2)
        self.assertEqual(self.place.max_guest, 4)
        self.assertEqual(self.place.price_by_night, 1000)
        self.assertEqual(self.place.latitude, 12.78)
        self.assertEqual(self.place.longitude, 31.32)
        self.assertEqual(self.place.amenity_ids, [12, 34])

    def test_edge_case_attributes_type(self):
        """
        test_edge_case_attributes_type
        """
        self.place.city_id = 123
        self.place.user_id = 123
        self.place.name = 123
        self.place.description = 123
        self.place.number_rooms = "2"
        self.place.number_bathrooms = "2"
        self.place.max_guest = "4"
        self.place.price_by_night = "1000"
        self.place.latitude = "0.0"
        self.place.longitude = "0.0"
        self.place.amenity_ids = {"1": 1, "2": 2}
        self.assertEqual(self.place.city_id, 123)
        self.assertEqual(self.place.user_id, 123)
        self.assertEqual(self.place.name, 123)
        self.assertEqual(self.place.description, 123)
        self.assertEqual(self.place.number_rooms, "2")
        self.assertEqual(self.place.number_bathrooms, "2")
        self.assertEqual(self.place.max_guest, "4")
        self.assertEqual(self.place.price_by_night, "1000")
        self.assertEqual(self.place.latitude, "0.0")
        self.assertEqual(self.place.longitude, "0.0")
        self.assertEqual(self.place.amenity_ids, {"1": 1, "2": 2})


if __name__ == '__main__':
    unittest.main()
