FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the entrypoint script into the current working directory
COPY entrypoint.sh .

# Ensure the entrypoint script is executable
# This step is critical and must be done after the COPY
RUN chmod +x entrypoint.sh

# Install system dependencies
RUN apt-get update && apt-get install -y cron procps

# Copy Python requirements and install
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of your application code
COPY . .

# Expose the port
EXPOSE 8000

# Set the entrypoint to the now-executable script
# ENTRYPOINT ["./entrypoint.sh"]
ENTRYPOINT ["sh", "./entrypoint.sh"]