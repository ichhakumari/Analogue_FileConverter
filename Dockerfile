# Use official Python image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy project files into the container
COPY . .

# Install dependencies
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

# Collect static files (optional)
RUN python manage.py collectstatic --noinput || true

# Expose the port (for documentation, not necessary for binding)
EXPOSE 8000

# Correctly use the PORT environment variable in CMD
CMD sh -c "gunicorn file_converstion.wsgi:application --bind 0.0.0.0:$PORT"
