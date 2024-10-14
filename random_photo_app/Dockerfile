# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /Users/laura.ye/Documents/GitHub/camunda-task/random_photo_app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Check Flask version
RUN python -c "import flask; print(flask.__version__)"

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 5001

# Command to run the application
CMD ["python", "app.py"]