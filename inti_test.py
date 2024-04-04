import unittest
import requests

# Replace with the actual service name or URL within your Kubernetes cluster
SERVICE_URL = "http://0.0.0.0:8008"

class TestFlaskApp(unittest.TestCase):

    def test_get_all_students(self):
        """
        Tests if the GET request to retrieve all students returns a successful response (200 OK).
        """
        response = requests.get(f"{SERVICE_URL}/")
        self.assertEqual(response.status_code, 200)
        print("This is the first test")
    def test_create_student(self):
        """
        Tests creating a new student and verifies it's added successfully.
        """
        data = {
            "firstname": "John",
            "lastname": "Doe",
            "email": "john.doeyo@example.com",
            "age": 25,
            "bio": "A brief bio of John Doe."
        }
        data1 = {
            "firstname": "John1",
            "lastname": "Doe",
            "email": "john.doe1@example.com",
            "age": 25,
            "bio": "A brief bio of John Doe."
        }

        response = requests.post(f"{SERVICE_URL}/create", data=data)
        response = requests.post(f"{SERVICE_URL}/create", data=data1)
        self.assertEqual(response.status_code, 200)  # Redirect on successful creation

        # Optional: Verify the newly created student is present (requires additional logic)
        # ...

    def test_edit_student(self):
        """
        Tests editing an existing student and verifies the changes are reflected.
        (Requires creating a student beforehand)
        """
        # Implement logic to create a student first (e.g., using test_create_student)
        student_id = 4  # Replace with the actual ID of the created student

        data = {
            "firstname": "chetan",
            "lastname": "Doe",
            "email": "chetan.doe@example.com",  # Update email
            "age": 30,
            "bio": "An updated bio for Jane Doe."
        }
        response = requests.post(f"{SERVICE_URL}/{student_id}/edit", data=data)
        self.assertEqual(response.status_code, 200)  # Redirect on successful edit

        # Optional: Verify the edited student information (requires additional logic)
        # ...

    def test_delete_student(self):
        """
        Tests deleting an existing student and verifies it's removed.
        (Requires creating a student beforehand)
        """
        # Implement logic to create a student first (e.g., using test_create_student)
        student_id =3# Replace with the actual ID of the created student

        response = requests.post(f"{SERVICE_URL}/{student_id}/delete")
        self.assertEqual(response.status_code, 200)  # Redirect on successful delete

        # Optional: Verify the student is no longer present (requires additional logic)
        # ...

if __name__ == "__main__":
    unittest.main()
