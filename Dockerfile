# Use an official Python runtime as the base image
FROM python:3.10-slim

COPY ./requirements.txt /app/requirements.txt

# Set the working directory in the container
WORKDIR /app

RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install flask

RUN pip install python-jenkins

# Make port 5000 available to the world outside this container
EXPOSE 7000

ENTRYPOINT [ "python" ]

# Define the command to run the application
CMD ["python", "app.py"]
