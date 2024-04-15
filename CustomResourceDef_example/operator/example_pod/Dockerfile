# Use the official Python image from Docker Hub
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt .

# Install any dependencies specified in requirements.txt
RUN pip install kubernetes
#RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python script into the container at /app
COPY example_pod.py .

# Run the Python script when the container starts
CMD ["python", "example_pod.py"]
#CMD ["bash", "-c", "while true; do sleep 3600; done"]