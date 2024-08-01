# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install the Python dependencies in the virtual environment
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port on which the Flask app will run
EXPOSE 5000

ENV GOOGLE_APPLICATION_CREDENTIALS="AIzaSyDuD9ybCKXRWceVgCOWOtAO3ctsxY_kGEk"

# Define the command to run the Flask application
CMD ["python", "app.py"]