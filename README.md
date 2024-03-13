# Jenkins_Pipeline
This is used for Jenkins CI/CD pipeline project
# Branch Management:

Principal Branch: This refers to the main branch of your code, often called master.
Branch (develop): This is a separate branch created from the master branch for testing commits. Once the changes are tested and approved, they can be merged back into the master branch.
# Setting Up Your Environment:

Create a virtual environment using the following command:
python3 -m venv venv
Activate the virtual environment:
source venv/bin/activate
Install the required Python packages using pip:
pip install -r requirements.txt
Run the Flask application with the --debug flag for debugging purposes:
python -m flask --debug run
# Creating Database Tables:

If you encounter an error indicating that a table is not found, you can create the necessary tables using the following steps:

Start a Flask shell:
flask shell
Import the db object from your application:
from app import db
Create all the tables defined in your application:
db.create_all()
