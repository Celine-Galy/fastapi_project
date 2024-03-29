# Use an official Python runtime as a parent image
FROM python:3.11

# Copy main.py to the container
COPY main.py /app/main.py

# Set the working directory in docker
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Specify the command to run on container start
CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"]
