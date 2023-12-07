#!/usr/bin/python3
""" Unittest for Amenity """
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):

    def setUp(self):
        self.amenity = Amenity()

    def tearDown(self):
        del self.amenity

    def test_inheritance(self):
        self.assertIsInstance(self.amenity, BaseModel)

    def test_attributes(self):
        self.assertTrue(hasattr(self.amenity, 'id'))
        self.assertTrue(hasattr(self.amenity, 'created_at'))
        self.assertTrue(hasattr(self.amenity, 'updated_at'))
        self.assertTrue(hasattr(self.amenity, 'name'))

    def test_default_values(self):
        self.assertEqual(self.amenity.name, "")

    def test_str_representation(self):
        expected_output = f"[Amenity] ({self.amenity.id}) {self.amenity.__dict__}"
        self.assertEqual(str(self.amenity), expected_output)

    def test_to_dict_method(self):
        expected_dict = {
            'id': self.amenity.id,
            'created_at': self.amenity.created_at.isoformat(),
            'updated_at': self.amenity.updated_at.isoformat(),
            '__class__': 'Amenity'
        }
        self.assertEqual(self.amenity.to_dict(), expected_dict)

    def test_edge_case_empty_name(self):
        self.amenity.name = ""
        self.assertEqual(self.amenity.name, "")

    def test_edge_case_non_empty_name(self):
        self.amenity.name = "Swimming Pool"
        self.assertEqual(self.amenity.name, "Swimming Pool")

    def test_edge_case_name_type(self):
        self.amenity.name = 123
        self.assertEqual(self.amenity.name, 123)

if __name__ == '__main__':
    unittest.main()
