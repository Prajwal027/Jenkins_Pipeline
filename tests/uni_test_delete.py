import unittest
from flask_sql1 import app, db, student

class TestDelete(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
    def tearDown(self):
        # Clean up the database after each test
        with app.app_context():
            db.session.rollback()
            db.session.query(student).delete()
            db.session.commit()
    def test_delete_student(self):
        student_id = 1             #new_student.id
        existing_student = student.query.get(student_id)
        self.assertIsNotNone(existing_student, "Student does not exist")
        # Send a POST request to delete the student
        rv = self.app.post(f'/{student_id}/delete')
        # Check if the student has been deleted successfully
        self.assertEqual(rv.status_code, 302)  # Assuming redirect on success
        # Verify that the student has been deleted from the database
        with app.app_context():
            deleted_student = student.query.get(student_id)
            self.assertIsNone(deleted_student, "Student was not deleted from the database")

if __name__ == '__main__':
    unittest.main()
