# Purplle Store Intelligence System

## Overview

This project was developed as part of the Purplle Tech Challenge 2026 Round 2.

The objective is to build an end-to-end store intelligence platform capable of processing CCTV footage, detecting customer movement inside the store, generating business events, exposing analytics through APIs, and visualizing insights on a dashboard.

The system converts raw video footage into structured business intelligence that can be used by store managers and operations teams to understand customer behavior and improve store performance.

---

## Features

### Computer Vision Pipeline

* Person detection using YOLOv8
* Multi-object tracking using ByteTrack
* Customer entry detection
* Customer exit detection
* Zone transition detection
* Dwell time monitoring

### Event Processing

The system generates structured events such as:

* ENTRY
* EXIT
* ZONE_ENTER
* ZONE_DWELL

All events are stored in JSONL format and can be consumed by downstream services.

### Backend APIs

The backend is implemented using FastAPI and provides:

* Health monitoring endpoint
* Event ingestion endpoint
* Store metrics endpoint
* Funnel analytics endpoint
* Anomaly detection endpoint

### Dashboard

A Streamlit dashboard provides a simple operational view of:

* Visitor count
* Entries
* Exits
* Dwell events
* Event history

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

README.md
DESIGN.md
CHOICES.md

---

## Running the Project

### Install Dependencies

pip install -r requirements.txt

### Run FastAPI

python -m uvicorn app.main:app --reload

### Open Swagger

http://127.0.0.1:8000/docs

### Run Dashboard

python -m streamlit run dashboard/app.py

---

## Event Schema

Each event follows a standard structure:

{
"event_id": "...",
"store_id": "ST1008",
"camera_id": "CAM5",
"visitor_id": "VIS_0001",
"event_type": "ENTRY",
"timestamp": "...",
"zone_id": null,
"dwell_ms": 0,
"is_staff": false,
"confidence": 1.0
}

---

## Future Improvements

* Database persistence
* Kafka based event streaming
* Real-time processing
* Multi-camera identity association
* Heatmap generation
* Queue analytics
* Customer journey reconstruction

---

## Conclusion

This project demonstrates how computer vision, event-driven design, APIs, and dashboards can be combined to transform CCTV footage into meaningful store intelligence. The architecture was intentionally designed to remain simple, modular, and easy to extend.
