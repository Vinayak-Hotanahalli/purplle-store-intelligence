FROM python:3.11-slim

WORKDIR /app

COPY requirements-dashboard.txt .

RUN pip install --default-timeout=1000 --no-cache-dir -r requirements-dashboard.txt

COPY . .

EXPOSE 8501

CMD ["python", "-m", "streamlit", "run", "dashboard/app.py", "--server.address=0.0.0.0"]