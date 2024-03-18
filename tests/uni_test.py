import unittest, sys
sys.path.append('/var/lib/jenkins/workspace/Jenkins_miniproject@2')
from flask_sql1 import app
class TestCreate(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        # Consider adding a fixture to set up a test database

    def test_create_student_get(self):
        # Test GET request to access create form
        rv = self.app.get('/create')
        self.assertEqual(rv.status_code, 200)  # Use status_code for clarity
        self.assertIn(b"Create", rv.data)  # Check for presence of form

    def test_create_student_post(self):
        # Test POST request with student data
        new_student = {
            "firstname": "John1",
            "lastname": "Doe",
            "email": f"john.doe1@example.com",
            "age": 30,
            "bio": "This is a test biography",
        }

        new_student1 = {
            "firstname": "Sid",
            "lastname": "rt",
            "email": f"Sid.rt@example.com",
            "age": 23,
            "bio": "This is Sid",
        }
        # Send POST request with data
        rv = self.app.post('/create', data=new_student)
        rv1 = self.app.post('/create', data=new_student1)
        # Assert successful creation (redirect or database check)
        self.assertEqual(rv.status_code, 302)  # Assuming redirect on success
        # ... (Optional: Check if student is added to the database)
if __name__=='__main__':
    unittest.main()
