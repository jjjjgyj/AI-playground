# Use the official Python 3 base image
FROM python:3

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python script to the working directory
COPY test.py .

# Run the Python script when the container starts
CMD ["python", "test.py"]
