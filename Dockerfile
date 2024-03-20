# Use a lightweight base image for Python applications
FROM python:3.10-slim

# Create a working directory for the application
WORKDIR /app

# Copy requirements.txt file
COPY requirements.txt .

# Install dependencies listed in requirements.txt
RUN pip install -r requirements.txt

# Copy the application code
COPY . .

# Expose the port where the Flask app will run (usually 5000)
EXPOSE 5000

# Set the command to execute the Flask application
CMD ["python3", "flask_sql1.py"]
