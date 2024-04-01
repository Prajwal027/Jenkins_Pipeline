"""This is a test unit for create() in flask application"""
import sys
import unittest
sys.path.append('/home/runner/work/Jenkins_Pipeline/Jenkins_Pipeline/')
from flask_sql1 import app # pylint: disable=wrong-import-position

class TestCreate(unittest.TestCase):
    """
    This class is created to check on GET and POST request to access create form
    """
    def setUp(self):
        """This is just an setup function for create() test units"""
        app.testing = True
        self.app = app.test_client()
        # Consider adding a fixture to set up a test database

    def test_create_student_get(self):
        """Test GET request to access create form"""
        rv = self.app.get('/create')
        self.assertEqual(rv.status_code, 200)
        self.assertIn(b"Create", rv.data)

    def test_create_student_post(self):
        """Test POST request with student data"""
        new_student = {
            "firstname": "John1",
            "lastname": "Doe",
            "email": "john.doe10@example.com",
            "age": 30,
            "bio": "This is a test biography",
        }

        new_student1 = {
            "firstname": "Sid",
            "lastname": "rt",
            "email": "Sid.rt0@example.com",
            "age": 23,
            "bio": "This is Sid",
        }
        # Send POST request with data
        rv = self.app.post('/create', data=new_student)
        rv1 = self.app.post('/create', data=new_student1)
        # Assert successful creation (redirect or database check)
        if b"Email already exists. Please use a different email." not in rv.data:
            self.assertEqual(rv.status_code, 302)  # Assuming redirect on success
        if b"Email already exists. Please use a different email." not in rv1.data:
            self.assertEqual(rv1.status_code, 302)

if __name__=='__main__':
    unittest.main()
