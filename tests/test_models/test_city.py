#!/usr/bin/python3
""" Unittest for City """
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):

    def setUp(self):
        self.city = City()

    def tearDown(self):
        del self.city

    def test_inheritance(self):
        self.assertIsInstance(self.city, BaseModel)

    def test_attributes(self):
        self.assertTrue(hasattr(self.city, 'id'))
        self.assertTrue(hasattr(self.city, 'created_at'))
        self.assertTrue(hasattr(self.city, 'updated_at'))
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))

    def test_default_values(self):
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_str_representation(self):
        expected_output = f"[City] ({self.city.id}) {self.city.__dict__}"
        self.assertEqual(str(self.city), expected_output)

    def test_to_dict_method(self):
        expected_dict = {
            'id': self.city.id,
            'created_at': self.city.created_at.isoformat(),
            'updated_at': self.city.updated_at.isoformat(),
            '__class__': 'City'
        }
        self.assertEqual(self.city.to_dict(), expected_dict)

    def test_edge_case_empty_state_id(self):
        self.city.state_id = ""
        self.assertEqual(self.city.state_id, "")

    def test_edge_case_empty_name(self):
        self.city.name = ""
        self.assertEqual(self.city.name, "")

    def test_edge_case_non_empty_state_id_and_name(self):
        self.city.state_id = "CA"
        self.city.name = "San Francisco"
        self.assertEqual(self.city.state_id, "CA")
        self.assertEqual(self.city.name, "San Francisco")

    def test_edge_case_state_id_type(self):
        self.city.state_id = 123
        self.assertEqual(self.city.state_id, 123)

    def test_edge_case_name_type(self):
        self.city.name = 123
        self.assertEqual(self.city.name, 123)


if __name__ == '__main__':
    unittest.main()
