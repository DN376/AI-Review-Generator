# Use the official Python image with version 3.11.4 as the base image
FROM python:3.11.4

# Set the working directory inside the container
WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy the source code and requirements.txt file into the container
RUN git clone https://github.com/DN376/AI-Review-Generator.git .

COPY requirements.txt .

# Install the required libraries from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Clean up the package cache to reduce image size
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Expose the port that Streamlit runs on (default: 8501)
EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Run the Streamlit app
ENTRYPOINT ["streamlit", "run", "GreetingPage.py", "--server.port=8501", "--server.address=0.0.0.0"]
