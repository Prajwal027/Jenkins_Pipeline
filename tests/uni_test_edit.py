import unittest, sys
sys.path.append('/var/lib/jenkins/workspace/Jenkins_miniproject@2')
from flask_sql1 import app, db, student

class TestEdit(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        # Consider adding a fixture to set up a test database

    def test_edit_student_get(self):
        # Test GET request to access edit form
        rv = self.app.get('/2/edit')  # Assuming you want to edit student with ID 1
        self.assertEqual(rv.status_code, 200, "This Student_id is not created")  # Use status_code for clarity

    def test_edit_student_post(self):
        # Test POST request with updated student data
        updated_student = {
            "firstname": "Sid",
            "lastname": "rt",
            "email": "sid.rt2001@gmail.com",
            "age": 23,
            "bio": "This is an updated biography",
        }
        # Send POST request with data
        rv = self.app.post('/1/edit', data=updated_student)  # Assuming you want to edit student with ID 1
        # Assert successful update (redirect or database check)
        self.assertEqual(rv.status_code, 302)  # Assuming redirect on success
        # ... (Optional: Check if student is updated in the database)
if __name__ == '__main__':
    unittest.main()
