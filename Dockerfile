# Use the FastAPI image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

# Install requirements
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copy app folder to /app in container
COPY ./app /app/app
