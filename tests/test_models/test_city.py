#!/usr/bin/python3
""" Unittest for City """
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """
    TestCity
    """
    def setUp(self):
        """
        setUp
        """
        self.city = City()

    def tearDown(self):
        """
        tearDown
        """
        del self.city

    def test_inheritance(self):
        """
        test_inheritance
        """
        self.assertIsInstance(self.city, BaseModel)

    def test_attributes(self):
        """
        test_attributes
        """
        self.assertTrue(hasattr(self.city, 'id'))
        self.assertTrue(hasattr(self.city, 'created_at'))
        self.assertTrue(hasattr(self.city, 'updated_at'))
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))

    def test_default_values(self):
        """
        test_default_values
        """
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_str_representation(self):
        """
        test_str_representation
        """
        expected_output = f"[City] ({self.city.id}) {self.city.__dict__}"
        self.assertEqual(str(self.city), expected_output)

    def test_to_dict_method(self):
        """
        test_to_dict_method
        """
        expected_dict = {
            'id': self.city.id,
            'created_at': self.city.created_at.isoformat(),
            'updated_at': self.city.updated_at.isoformat(),
            '__class__': 'City'
        }
        self.assertEqual(self.city.to_dict(), expected_dict)

    def test_edge_case_empty_state_id(self):
        """
        test_edge_case_empty_state_id
        """
        self.city.state_id = ""
        self.assertEqual(self.city.state_id, "")

    def test_edge_case_empty_name(self):
        """
        test_edge_case_empty_name
        """
        self.city.name = ""
        self.assertEqual(self.city.name, "")

    def test_edge_case_non_empty_state_id_and_name(self):
        """
        test_edge_case_non_empty_state_id_and_name
        """
        self.city.state_id = "CA"
        self.city.name = "San Francisco"
        self.assertEqual(self.city.state_id, "CA")
        self.assertEqual(self.city.name, "San Francisco")

    def test_edge_case_state_id_type(self):
        """
        test_edge_case_state_id_type
        """
        self.city.state_id = 123
        self.assertEqual(self.city.state_id, 123)

    def test_edge_case_name_type(self):
        """
        test_edge_case_name_type
        """
        self.city.name = 123
        self.assertEqual(self.city.name, 123)


if __name__ == '__main__':
    unittest.main()
