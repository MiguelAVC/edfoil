# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any Python dependencies from requirements.txt if present
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the main.py file when the container starts
CMD ["python", "main.py"]
