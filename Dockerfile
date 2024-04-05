# Use a lightweight base image for Python applications
FROM python:3.10-slim

# Create a working directory for the application
WORKDIR /app

# Copy requirements.txt file
COPY requirements.txt .

# Install dependencies listed in requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn

# Copy the application code
COPY . .

# Expose the port where the Flask app will run (usually 5000)
EXPOSE 8008

# Set the command to execute the Flask application
CMD ["gunicorn", "--bind", "0.0.0.0:8008", "flask_sql1:app"]
