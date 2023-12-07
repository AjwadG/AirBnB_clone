#!/usr/bin/python3
""" Unittest for User """
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    TestUser
    """

    def setUp(self):
        """
        setUp
        """
        self.user = User()

    def tearDown(self):
        """
        tearDown
        """
        del self.user

    def test_inheritance(self):
        """
        test_inheritance
        """
        self.assertIsInstance(self.user, BaseModel)

    def test_attributes(self):
        """
        test_attributes
        """
        self.assertTrue(hasattr(self.user, 'id'))
        self.assertTrue(hasattr(self.user, 'created_at'))
        self.assertTrue(hasattr(self.user, 'updated_at'))
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_default_values(self):
        """
        test_default_values
        """
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_str_representation(self):
        """
        test_str_representation
        """
        expected_output = f"[User] ({self.user.id}) {self.user.__dict__}"
        self.assertEqual(str(self.user), expected_output)

    def test_to_dict_method(self):
        """
        test_to_dict_method
        """
        expected_dict = {
            'id': self.user.id,
            'created_at': self.user.created_at.isoformat(),
            'updated_at': self.user.updated_at.isoformat(),
            '__class__': 'User'
        }
        self.assertEqual(self.user.to_dict(), expected_dict)

    def test_edge_case_empty_attributes(self):
        """
        test_edge_case_empty_attributes
        """
        self.user.email = ""
        self.user.password = ""
        self.user.first_name = ""
        self.user.last_name = ""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_edge_case_non_empty_attributes(self):
        """
        test_edge_case_non_empty_attributes
        """
        self.user.email = "eg@eg.com"
        self.user.password = "password123"
        self.user.first_name = "henry"
        self.user.last_name = "calvin"
        self.assertEqual(self.user.email, "eg@eg.com")
        self.assertEqual(self.user.password, "password123")
        self.assertEqual(self.user.first_name, "henry")
        self.assertEqual(self.user.last_name, "calvin")

    def test_edge_case_invalid_types(self):
        """
        test_edge_case_invalid_types
        """
        self.user.email = 123
        self.user.password = 123
        self.user.first_name = 123
        self.user.last_name = 123
        self.assertEqual(self.user.email, 123)
        self.assertEqual(self.user.password, 123)
        self.assertEqual(self.user.first_name, 123)
        self.assertEqual(self.user.last_name, 123)


if __name__ == '__main__':
    unittest.main()
