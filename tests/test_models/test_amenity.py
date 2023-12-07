#!/usr/bin/python3
""" Unittest for Amenity """
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """
    TestAmenity
    """

    def setUp(self):
        """
        setUp
        """
        self.amenity = Amenity()

    def tearDown(self):
        """
        tearDown
        """
        del self.amenity

    def test_inheritance(self):
        """
        test_inheritance
        """
        self.assertIsInstance(self.amenity, BaseModel)

    def test_attributes(self):
        """
        test_attributes
        """
        self.assertTrue(hasattr(self.amenity, 'id'))
        self.assertTrue(hasattr(self.amenity, 'created_at'))
        self.assertTrue(hasattr(self.amenity, 'updated_at'))
        self.assertTrue(hasattr(self.amenity, 'name'))

    def test_default_values(self):
        """
        test_default_values
        """
        self.assertEqual(self.amenity.name, "")

    def test_str_representation(self):
        """
        test_str_representation
        """
        expected = f"[Amenity] ({self.amenity.id}) {self.amenity.__dict__}"
        self.assertEqual(str(self.amenity), expected)

    def test_to_dict_method(self):
        """
        test_to_dict_method
        """
        expected_dict = {
            'id': self.amenity.id,
            'created_at': self.amenity.created_at.isoformat(),
            'updated_at': self.amenity.updated_at.isoformat(),
            '__class__': 'Amenity'
        }
        self.assertEqual(self.amenity.to_dict(), expected_dict)

    def test_edge_case_empty_name(self):
        """
        test_edge_case_empty_name
        """
        self.amenity.name = ""
        self.assertEqual(self.amenity.name, "")

    def test_edge_case_non_empty_name(self):
        """
        test_edge_case_non_empty_name
        """
        self.amenity.name = "Swimming Pool"
        self.assertEqual(self.amenity.name, "Swimming Pool")

    def test_edge_case_name_type(self):
        """
        test_edge_case_name_type
        """
        self.amenity.name = 123
        self.assertEqual(self.amenity.name, 123)


if __name__ == '__main__':
    unittest.main()
