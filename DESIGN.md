# Design Decisions

## Objective

The goal of this system is to transform raw CCTV footage into business-level insights that can help retail teams understand customer activity inside a store.

Instead of focusing only on object detection accuracy, the system focuses on converting visual observations into actionable business events.

---

## High-Level Architecture

Video Input

↓

Person Detection

↓

Multi Object Tracking

↓

Business Event Generation

↓

Event Storage

↓

Analytics APIs

↓

Dashboard

---

## Detection Layer

YOLOv8 is used for person detection.

The model identifies customers visible in CCTV footage and provides bounding box coordinates with confidence scores.

Output:

* Bounding Box
* Confidence
* Class

---

## Tracking Layer

ByteTrack is used for assigning stable identities to detected customers.

Tracking enables the system to determine:

* Entry
* Exit
* Zone transitions
* Dwell duration

Without tracking, customer journeys cannot be reconstructed.

---

## Zone Intelligence

The store layout was simplified into logical business zones:

* Entrance
* FOH
* Makeup
* Shelf Area
* Billing

This design choice reduces implementation complexity while still supporting useful analytics.

---

## Event Layer

The event layer converts visual observations into business events.

Examples:

ENTRY

A customer enters the store.

EXIT

A customer leaves the store.

ZONE_ENTER

A customer enters a specific zone.

ZONE_DWELL

A customer spends meaningful time inside a zone.

---

## API Layer

FastAPI was selected for its:

* Performance
* Simplicity
* Automatic Swagger documentation
* Strong Python ecosystem support

The API layer provides a clean separation between analytics and computer vision.

---

## Dashboard Layer

The dashboard was implemented using Streamlit.

Reasons:

* Fast development
* Easy visualization
* Minimal configuration
* Suitable for prototype demonstrations

---

## Scalability Considerations

In a production environment the following upgrades would be recommended:

* PostgreSQL
* Kafka
* Redis
* Docker
* Kubernetes
* Cloud deployment

These additions would allow the system to scale across multiple stores and cameras.

---

## Design Philosophy

The primary design principle was to build a working end-to-end system that demonstrates how business insights can be derived from CCTV footage while keeping the implementation understandable and maintainable.
