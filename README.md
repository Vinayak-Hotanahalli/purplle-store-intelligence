# Purplle Store Intelligence System

## Overview

The Purplle Store Intelligence System is an end-to-end retail analytics platform developed for the Purplle Tech Challenge 2026 Round 2.

The objective of the project is to transform raw CCTV footage into actionable business intelligence using computer vision, event-driven architecture, analytics APIs, and interactive dashboards.

The system automatically detects customers, tracks their movement across the store, identifies entry and exit behavior, monitors zone-level engagement, calculates dwell time, and exposes business metrics through APIs and dashboards.

This solution demonstrates how existing CCTV infrastructure can be leveraged to generate operational insights without requiring additional hardware investments.

---

## Problem Statement

Retail stores generate large volumes of CCTV footage every day, but most of this data remains unused for business decision-making.

Store managers need answers to questions such as:

* How many customers entered the store?
* Which areas received the highest engagement?
* How long do customers spend in specific sections?
* What is the conversion funnel from entry to billing?
* Are there unusual behavioral patterns inside the store?

This project addresses these challenges by converting video streams into structured business events and analytics.

---

## Solution Architecture

CCTV Video

↓

YOLOv8 Person Detection

↓

ByteTrack Multi-Object Tracking

↓

Business Event Generation

↓

Event Storage (JSONL)

↓

FastAPI Analytics Layer

↓

Streamlit Dashboard

---

## Key Features

### Computer Vision Pipeline

* Real-time person detection using YOLOv8
* Multi-object tracking using ByteTrack
* Unique visitor identification
* Entry event detection
* Exit event detection
* Zone transition tracking
* Dwell time monitoring

### Event Generation

The system converts low-level vision outputs into business-friendly events.

Supported events:

* ENTRY
* EXIT
* ZONE_ENTER
* ZONE_DWELL

Each event contains metadata required for analytics and reporting.

### Analytics APIs

The backend is implemented using FastAPI.

Available APIs:

* Health Monitoring API
* Event Ingestion API
* Store Metrics API
* Funnel Analytics API
* Anomaly Detection API

Swagger documentation is automatically generated and available through FastAPI.

### Dashboard

A Streamlit dashboard provides:

* Visitor analytics
* Entry and exit statistics
* Dwell event monitoring
* Event history visualization
* Store performance insights

---

## Technology Stack

### Computer Vision

* YOLOv8
* OpenCV
* ByteTrack
* Supervision

### Backend

* FastAPI
* Pydantic
* Uvicorn

### Analytics

* Pandas
* JSONL Event Storage

### Dashboard

* Streamlit

### Development

* Python 3.11
* Git
* GitHub

---

## Project Structure

PurplleChallenge/

app/

* main.py
* models.py
* metrics.py
* funnel.py
* anomalies.py
* load_events.py

pipeline/

* detect.py
* track.py
* entry_exit.py
* zone_detector.py
* dwell_detector.py

dashboard/

* app.py

outputs/

* events.jsonl

docs/

README.md
DESIGN.md
CHOICES.md

requirements.txt

---

## Event Schema

Example Event

```json
{
  "event_id": "33d149c3-0a50-4b77-8e94-eeaac3878fa8",
  "store_id": "ST1008",
  "camera_id": "CAM5",
  "visitor_id": "VIS_0001",
  "event_type": "ENTRY",
  "timestamp": "2026-06-01T18:00:15.638957",
  "zone_id": null,
  "dwell_ms": 0,
  "is_staff": false,
  "confidence": 1.0,
  "metadata": {}
}
```

---

## Running the Project

### Step 1: Clone Repository

```bash
git clone https://github.com/Vinayak-Hotanahalli/purplle-store-intelligence.git

cd purplle-store-intelligence
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run Computer Vision Pipeline

```bash
python pipeline/zone_detector.py
```

This generates business events from CCTV footage.

### Step 4: Start FastAPI Backend

```bash
python -m uvicorn app.main:app --reload
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

### Step 5: Launch Dashboard

```bash
python -m streamlit run dashboard/app.py
```

Dashboard URL:

```text
http://localhost:8501
```

---

## API Endpoints

### Health Check

```http
GET /health
```

### Event Ingestion

```http
POST /events/ingest
```

### Store Metrics

```http
GET /stores/ST1008/metrics
```

### Funnel Analytics

```http
GET /stores/ST1008/funnel
```

### Anomaly Detection

```http
GET /stores/ST1008/anomalies
```

---

## Engineering Decisions

### Why YOLOv8?

YOLOv8 provides a strong balance between detection accuracy and real-time performance, making it suitable for retail environments.

### Why ByteTrack?

ByteTrack maintains identity consistency across frames and performs well in crowded scenes.

### Why FastAPI?

FastAPI offers high performance, automatic API documentation, and rapid backend development.

### Why Streamlit?

Streamlit enables quick creation of interactive dashboards without requiring complex frontend development.

---

## Production Considerations

The architecture was intentionally designed to remain modular.

Future production enhancements may include:

* Kafka-based event streaming
* PostgreSQL event storage
* Redis caching
* Real-time processing pipelines
* Multi-camera identity association
* Heatmap generation
* Queue analytics
* Customer journey reconstruction
* Cloud deployment

---

## Docker Support

Docker configuration files are included within the repository.

Due to the size of computer vision dependencies such as YOLOv8 and PyTorch, initial Docker image builds may require additional download time depending on system resources and network conditions.

The complete solution has been validated locally using Python 3.11.

---

## Future Improvements

* Staff versus customer classification
* Product interaction detection
* Shelf engagement analytics
* Billing queue monitoring
* Advanced anomaly detection
* Real-time alerting
* Multi-store analytics platform

---

## Conclusion

The Purplle Store Intelligence System demonstrates how computer vision, event-driven processing, analytics APIs, and dashboards can be combined to transform CCTV footage into actionable business intelligence.

The solution provides a strong foundation for scalable retail analytics and can be extended into a production-grade platform through additional streaming, storage, and deployment capabilities.
