
#  Python image
FROM python:3.10

# Set working directory 
WORKDIR /app

# Install system dependencies including Open Babel
RUN apt-get update && apt-get install -y \
    openbabel \
    && rm -rf /var/lib/apt/lists/*

# Verify Open Babel installation
RUN obabel -V

# Copy project files into the container
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

# Collect static files (optional)
RUN python manage.py collectstatic --noinput || true

# Expose the port (used for deployment)
EXPOSE 8000

# Correctly use the PORT environment variable in CMD
CMD sh -c "gunicorn file_converstion.wsgi:application --bind 0.0.0.0:$PORT"
