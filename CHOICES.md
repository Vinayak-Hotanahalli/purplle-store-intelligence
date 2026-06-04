# CHOICES.md

# Engineering Choices and Trade-Offs

## Introduction

This document explains the major engineering decisions made during the development of the Purplle Store Intelligence System.

The goal was not only to build a working solution but also to select technologies and architectural patterns that balance simplicity, performance, maintainability, and future scalability.

---

# Model Selection

## Why YOLOv8?

The primary requirement of the system is reliable customer detection from CCTV footage.

Several approaches were considered:

* Traditional OpenCV methods
* Haar Cascades
* SSD-based detectors
* YOLO family models

YOLOv8 was selected because it provides:

* High detection accuracy
* Fast inference speed
* Real-time processing capability
* Easy Python integration
* Strong community support

The model performs well for person detection tasks and offers a good balance between accuracy and performance.

### Trade-Off

YOLOv8 introduces larger dependency requirements compared to traditional OpenCV approaches, but the improved detection quality justified this decision.

---

# Tracking Selection

## Why ByteTrack?

Detection alone is insufficient because customers appear across multiple video frames.

A tracking solution was required to maintain customer identity across time.

Several tracking approaches were considered:

* SORT
* DeepSORT
* ByteTrack

ByteTrack was selected because:

* It is lightweight
* It performs well in crowded environments
* It maintains identity consistency effectively
* It integrates naturally with YOLO detections

### Benefits

Tracking enables:

* Entry detection
* Exit detection
* Zone analytics
* Dwell analytics
* Customer journey reconstruction

### Trade-Off

ByteTrack may occasionally lose identities during severe occlusion, but it provides an excellent balance between complexity and performance for a prototype solution.

---

# Zone Design Choices

## Why Static Zones?

The project uses predefined business zones:

* Entrance
* FOH
* Makeup
* Shelf Area
* Billing

A dynamic store-layout system was considered but not implemented.

### Reasoning

Static zones provide:

* Simpler implementation
* Faster development
* Easier debugging
* Clear business interpretation

### Trade-Off

Static zones require manual configuration when store layouts change.

Future implementations could support configurable zones stored in a database.

---

# Event Schema Design

## Why Event-Driven Architecture?

Instead of exposing raw computer vision outputs, the system generates structured business events.

Examples:

* ENTRY
* EXIT
* ZONE_ENTER
* ZONE_DWELL

### Benefits

This design:

* Decouples computer vision from analytics
* Simplifies downstream processing
* Supports future integrations
* Enables scalable analytics workflows

The event layer acts as a bridge between technical computer vision outputs and business-facing analytics.

---

# Why JSONL?

Events are stored using JSONL (JSON Lines).

Example:

```json
{"event_type":"ENTRY"}
{"event_type":"ZONE_ENTER"}
```

### Benefits

* Human-readable
* Easy to debug
* Supports append-only event streams
* Compatible with analytics tools
* Simple to process using Python

### Trade-Off

JSONL is not ideal for very large-scale production deployments.

Future systems would likely use:

* Kafka
* PostgreSQL
* Data warehouses

for long-term storage and analytics.

---

# API Architecture Decisions

## Why FastAPI?

The backend analytics layer is implemented using FastAPI.

### Reasons

* High performance
* Automatic Swagger documentation
* Strong typing support
* Easy integration with Python
* Clean developer experience

### Implemented APIs

#### Health Endpoint

Provides service health monitoring.

#### Event Ingestion Endpoint

Accepts business events.

#### Metrics Endpoint

Returns visitor and event statistics.

#### Funnel Endpoint

Provides customer journey analytics.

#### Anomaly Endpoint

Identifies unusual operational patterns.

### Trade-Off

FastAPI introduces additional API-layer complexity compared to a standalone script, but the resulting architecture is significantly more maintainable and extensible.

---

# Dashboard Technology Choice

## Why Streamlit?

The project required a lightweight dashboard for visualization.

Several options were considered:

* React
* Flask Templates
* Dash
* Streamlit

Streamlit was selected because:

* Rapid development
* Minimal frontend code
* Native Python integration
* Easy deployment

### Benefits

The dashboard enables business users to consume insights without interacting directly with APIs.

### Trade-Off

Streamlit offers less frontend customization compared to React-based applications, but significantly reduces development effort.

---

# Storage Strategy

## Why File-Based Storage?

The prototype stores events in JSONL files.

### Benefits

* Easy setup
* No external infrastructure
* Simplifies evaluation
* Supports local development

### Trade-Off

A database-backed solution would provide:

* Better scalability
* Faster querying
* Long-term persistence

This was intentionally deferred to keep the solution focused and lightweight.

---

# Production Readiness Considerations

Several production-oriented technologies were considered but not fully implemented.

Examples include:

* PostgreSQL
* Kafka
* Redis
* Docker
* Kubernetes
* Cloud deployment

These were identified as future enhancements rather than immediate requirements.

---

# AI-Assisted Engineering Decisions

AI-assisted tools were used throughout development to support:

* Research
* Documentation refinement
* Debugging
* Architectural exploration

AI assistance helped accelerate development and evaluate alternative approaches.

Final decisions regarding:

* Technology selection
* Architecture design
* Event schema
* API implementation
* Testing and validation

were performed manually by the project author.

AI tools served as engineering assistants rather than autonomous decision makers.

---

# Key Trade-Off Summary

| Area          | Selected Option | Alternative        | Reason                          |
| ------------- | --------------- | ------------------ | ------------------------------- |
| Detection     | YOLOv8          | Traditional OpenCV | Better accuracy                 |
| Tracking      | ByteTrack       | SORT / DeepSORT    | Better identity consistency     |
| API Framework | FastAPI         | Flask              | Swagger support and performance |
| Dashboard     | Streamlit       | React              | Faster development              |
| Storage       | JSONL           | Database           | Simpler prototype               |
| Zones         | Static Zones    | Dynamic Layouts    | Reduced complexity              |

---

# Conclusion

The engineering decisions made throughout this project prioritized simplicity, maintainability, explainability, and demonstration value while still preserving a clear path toward future scalability.

The resulting architecture successfully demonstrates how computer vision can be transformed into business intelligence through event-driven design, analytics APIs, and dashboard visualization.
