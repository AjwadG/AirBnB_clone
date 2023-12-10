#!/usr/bin/python3
""" Unittest for BaseModel """
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    TestBaseModel
    """

    def test_attributes(self):
        """
        test_attributes
        """
        base_model = BaseModel()
        self.assertTrue(hasattr(base_model, 'id'))
        self.assertTrue(hasattr(base_model, 'created_at'))
        self.assertTrue(hasattr(base_model, 'updated_at'))

    def test_id_generation(self):
        """
        test_id_generation
        """
        base_model_1 = BaseModel()
        base_model_2 = BaseModel()
        self.assertNotEqual(base_model_1.id, base_model_2.id)

    def test_string_representation(self):
        """
        test_string_representation
        """
        base_model = BaseModel()
        expected = f"[BaseModel] ({base_model.id}) {base_model.__dict__}"
        self.assertEqual(str(base_model), expected)

    def test_save_method(self):
        """
        test_save_method
        """
        base_model = BaseModel()
        original_updated_at = base_model.updated_at
        base_model.save()
        self.assertNotEqual(original_updated_at, base_model.updated_at)

    def test_to_dict_method(self):
        """
        test_to_dict_method
        """
        base_model = BaseModel()
        expected_dict = {
            'id': base_model.id,
            'created_at': base_model.created_at.isoformat(),
            'updated_at': base_model.updated_at.isoformat(),
            '__class__': 'BaseModel'
        }
        self.assertEqual(base_model.to_dict(), expected_dict)

    def test_initialization_with_arguments(self):
        """
        test_initialization_with_arguments
        """
        data = {
            'id': 'some_id',
            'created_at': '2022-01-01T12:00:00.000000',
            'updated_at': '2022-01-01T13:00:00.000000'
        }
        base_model = BaseModel(**data)
        self.assertEqual(base_model.id, data['id'])
        self.assertEqual(base_model.created_at, datetime.strptime(
            data['created_at'], "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(base_model.updated_at, datetime.strptime(
            data['updated_at'], "%Y-%m-%dT%H:%M:%S.%f"))

    def test_edge_case_empty_arguments(self):
        """
        test_edge_case_empty_arguments
        """
        base_model = BaseModel()
        self.assertIsNotNone(base_model.id)
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_edge_case_invalid_datetime_format(self):
        """
        test_edge_case_invalid_datetime_format
        """
        data = {
            'id': 'some_id',
            'created_at': '2022-01-01 12:00:00',
            'updated_at': '2022-01-01 13:00:00'
        }
        with self.assertRaises(ValueError):
            BaseModel(**data)


if __name__ == '__main__':
    unittest.main()
