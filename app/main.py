from fastapi import FastAPI

from app.models import Event
from app.ingestion import save_event
from app.metrics import get_metrics
from app.funnel import get_funnel
from app.anomalies import get_anomalies

app = FastAPI(
    title="Purplle Store Intelligence API",
    version="1.0.0"
)

# ----------------------------------
# Home
# ----------------------------------

@app.get("/")
def home():

    return {
        "project": "Purplle Store Intelligence",
        "status": "running"
    }

# ----------------------------------
# Health
# ----------------------------------

@app.get("/health")
def health():

    return {
        "status": "healthy"
    }

# ----------------------------------
# Event Ingestion
# ----------------------------------

@app.post("/events/ingest")
def ingest(event: Event):

    save_event(event)

    return {
        "message": "event saved"
    }

# ----------------------------------
# Metrics
# ----------------------------------

@app.get("/stores/ST1008/metrics")
def metrics():

    return get_metrics()

# ----------------------------------
# Funnel Analytics
# ----------------------------------

@app.get("/stores/ST1008/funnel")
def funnel():

    return get_funnel()

# ----------------------------------
# Anomaly Detection
# ----------------------------------

@app.get("/stores/ST1008/anomalies")
def anomalies():

    return get_anomalies()