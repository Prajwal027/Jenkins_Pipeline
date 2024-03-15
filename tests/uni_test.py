import unittest
from flask_sql1 import app
class TestHello(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
    def test_hello(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')
    def test_create(self):
        cs = self.app.get('/create')
        self.assertEqual(cs.status, '200 OK')
    def test_edit(self):
        es = self.app.get('/1/edit')
        self.assertEqual(es.status, '200 OK')
    #def test_delete(self):
     #   ds = self.app.post('/2/delete')
      #  self.assertEqual(ds.status, '302 FOUND')

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

        # Send POST request with data
        rv = self.app.post('/create', data=new_student)

        # Assert successful creation (redirect or database check)
        self.assertEqual(rv.status_code, 302)  # Assuming redirect on success
        # ... (Optional: Check if student is added to the database)
if __name__=='__main__':
    unittest.main()
