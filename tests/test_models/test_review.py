#!/usr/bin/python3
""" Unittest for Review """
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):

    def setUp(self):
        self.review = Review()

    def tearDown(self):
        del self.review

    def test_inheritance(self):
        self.assertIsInstance(self.review, BaseModel)

    def test_attributes(self):
        self.assertTrue(hasattr(self.review, 'id'))
        self.assertTrue(hasattr(self.review, 'created_at'))
        self.assertTrue(hasattr(self.review, 'updated_at'))
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))

    def test_default_values(self):
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_str_representation(self):
        expected_output = f"[Review] ({self.review.id}) {self.review.__dict__}"
        self.assertEqual(str(self.review), expected_output)

    def test_to_dict_method(self):
        expected_dict = {
            'id': self.review.id,
            'created_at': self.review.created_at.isoformat(),
            'updated_at': self.review.updated_at.isoformat(),
            '__class__': 'Review'
        }
        self.assertEqual(self.review.to_dict(), expected_dict)

    def test_edge_case_empty_attributes(self):
        self.review.place_id = ""
        self.review.user_id = ""
        self.review.text = ""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_edge_case_non_empty_attributes(self):
        self.review.place_id = "CA"
        self.review.user_id = "user1"
        self.review.text = "Great Experience"
        self.assertEqual(self.review.place_id, "CA")
        self.assertEqual(self.review.user_id, "user1")
        self.assertEqual(self.review.text, "Great Experience")

    def test_edge_case_place_id_type(self):
        self.review.place_id = 123
        self.assertEqual(self.review.place_id, 123)

    def test_edge_case_user_id_type(self):
        self.review.user_id = 123
        self.assertEqual(self.review.user_id, 123)
    
    def test_edge_case_text_type(self):
        self.review.text = 123
        self.assertEqual(self.review.text, 123)


if __name__ == '__main__':
    unittest.main()
