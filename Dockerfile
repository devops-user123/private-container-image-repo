FROM python:3.8

# Install Flask and the Flask CORS extension
RUN pip install flask flask_cors

# Copy the app.py file to the container
COPY app.py /app/app.py

# Set the working directory to the app directory
WORKDIR /app

# Run the app when the container is started
CMD ["python", "app.py"]