FROM python:3.11.5-slim

WORKDIR /app

COPY . .

# Install requirements
RUN pip install -r requirements.txt

CMD ["streamlit", "run", "streamlit_app.py"]