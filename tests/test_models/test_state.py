#!/usr/bin/python3
""" Unittest for State """
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """
    TestState
    """

    def setUp(self):
        """
        setUp
        """
        self.state = State()

    def tearDown(self):
        """
        tearDown
        """
        del self.state

    def test_inheritance(self):
        """
        test_inheritance
        """
        self.assertIsInstance(self.state, BaseModel)

    def test_attributes(self):
        """
        test_attributes
        """
        self.assertTrue(hasattr(self.state, 'id'))
        self.assertTrue(hasattr(self.state, 'created_at'))
        self.assertTrue(hasattr(self.state, 'updated_at'))
        self.assertTrue(hasattr(self.state, 'name'))

    def test_default_values(self):
        """
        test_default_values
        """
        self.assertEqual(self.state.name, "")

    def test_str_representation(self):
        """
        test_str_representation
        """
        expected_output = f"[State] ({self.state.id}) {self.state.__dict__}"
        self.assertEqual(str(self.state), expected_output)

    def test_to_dict_method(self):
        """
        test_to_dict_method
        """
        expected_dict = {
            'id': self.state.id,
            'created_at': self.state.created_at.isoformat(),
            'updated_at': self.state.updated_at.isoformat(),
            '__class__': 'State'
        }
        self.assertEqual(self.state.to_dict(), expected_dict)

    def test_edge_case_empty_name(self):
        """
        test_edge_case_empty_name
        """
        self.state.name = ""
        self.assertEqual(self.state.name, "")

    def test_edge_case_non_empty_name(self):
        """
        test_edge_case_non_empty_name
        """
        self.state.name = "San Francisco"
        self.assertEqual(self.state.name, "San Francisco")

    def test_edge_case_name_type(self):
        """
        test_edge_case_name_type
        """
        self.state.name = 123
        self.assertEqual(self.state.name, 123)


if __name__ == '__main__':
    unittest.main()
