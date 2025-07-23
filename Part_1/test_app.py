import unittest
from student_age import app
from flask import json

class StudentAgeTests(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()
        self.headers = {
            'Authorization': 'Basic dG90bzpweXRob24='  # toto:python en base64
        }

    def test_get_student_ages(self):
        response = self.client.get('/pozos/api/v1.0/get_student_ages', headers=self.headers)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn("bob", data['student_ages'])
        self.assertIn("alice", data['student_ages'])
