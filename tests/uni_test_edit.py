"""This is a test unit for edit() in flask application"""
import sys
import unittest
sys.path.append('/home/runner/work/Jenkins_Pipeline/Jenkins_Pipeline/')
from flask_sql1 import app # pylint: disable=wrong-import-position
# pylint: disable=line-too-long
class TestEdit(unittest.TestCase):
    """
    This class is used for GET request to access edit form and POST request with updated student data
    """
    def setUp(self):
        """This is just an setup function for edit test unit"""
        app.testing = True
        self.app = app.test_client()
        # Consider adding a fixture to set up a test database

    def test_edit_student_get(self):
        """Test GET request to access edit form"""
        rv = self.app.get('/1/edit')
        self.assertEqual(rv.status_code, 200, "This Student_id is not created")

    def test_edit_student_post(self):
        """Test POST request with updated student data"""
        updated_student = {
            "firstname": "Sid",
            "lastname": "rt",
            "email": "sid.rt2001@gmail.com",
            "age": 23,
            "bio": "This is an updated biography",
        }
        # Send POST request with data
        rv = self.app.post('/1/edit', data=updated_student)
        # Assert successful update (redirect or database check)
        self.assertEqual(rv.status_code, 302)
if __name__ == '__main__':
    unittest.main()
