# Jenkins_Pipeline
This is used for Jenkins CI/CD pipeline project
# Branch Management:

1. Principal Branch: This refers to the main branch of your code, often called master.

2. Branch (develop): This is a separate branch created from the master branch for testing commits. Once the changes are tested and approved, they can be merged back into the master branch.
# Setting Up Your Environment:

1. Create a virtual environment using the following command:
python3 -m venv venv

2. Activate the virtual environment:
source venv/bin/activate

3. Install the required Python packages using pip:
pip install -r requirements.txt

4. Run the Flask application with the --debug flag for debugging purposes:
python -m flask --debug run
# Creating Database Tables:

If you encounter an error indicating that a table is not found, you can create the necessary tables using the following steps:

1. Start a Flask shell:
flask shell
2. Import the db object from your application:
from app import db
3. Create all the tables defined in your application:
db.create_all()
