# Use the official Python image with version 3.11.4 as the base image
FROM python:3.11.4

# Set the working directory inside the container
WORKDIR /app

# Copy the source code and requirements.txt file into the container
COPY . /app/

# Install the required libraries from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Clean up the package cache to reduce image size
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Expose the port that Streamlit runs on (default: 8501)
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "GreetingPage.py"]
