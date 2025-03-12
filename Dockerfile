# Use official Python image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy project 
COPY . .

# Install dependencies
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

# Collect static files
RUN python manage.py collectstatic --noinput

# port 
EXPOSE 8000

# Start Django app with Gunicorn
CMD ["gunicorn", "converter.wsgi:application", "--bind", "0.0.0.0:8000"]
