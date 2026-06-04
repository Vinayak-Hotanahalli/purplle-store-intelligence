# DESIGN.md

# Purplle Store Intelligence System

## Objective

The objective of this project is to transform raw CCTV footage into meaningful business intelligence that can help retail teams understand customer behavior inside a store.

Traditional CCTV systems are primarily used for security and monitoring purposes. However, the same video streams contain valuable information about customer movement, engagement, and store activity.

This project focuses on converting visual observations into structured business events that can be consumed by analytics systems and dashboards.

The solution was designed to demonstrate an end-to-end workflow that starts with video processing and ends with actionable business insights.

---

# System Architecture

The system follows a modular pipeline architecture.

Video Input

↓

Person Detection

↓

Multi-Object Tracking

↓

Zone Intelligence

↓

Business Event Generation

↓

Event Storage

↓

Analytics APIs

↓

Dashboard Visualization

Each stage performs a well-defined responsibility and communicates with downstream components using structured outputs.

This separation improves maintainability and allows individual components to evolve independently.

---

# Detection Layer

## Purpose

The detection layer is responsible for identifying customers present in CCTV footage.

## Technology Selected

YOLOv8

## Reasoning

YOLOv8 was selected because it provides:

* Strong real-time performance
* High detection accuracy
* Easy integration with Python
* Support for CPU and GPU inference
* Reliable performance for person detection tasks

The model processes each video frame and produces:

* Bounding box coordinates
* Confidence scores
* Detected object classes

These outputs form the foundation for all downstream analytics.

## Output

Each detection contains:

* X and Y coordinates
* Width and height
* Detection confidence
* Object class

---

# Tracking Layer

## Purpose

Detection alone is insufficient because customers appear across multiple video frames.

The tracking layer assigns persistent identities to customers and maintains those identities as customers move throughout the store.

## Technology Selected

ByteTrack

## Reasoning

ByteTrack was selected because it:

* Performs well in crowded environments
* Maintains identity consistency
* Integrates easily with YOLO detections
* Has strong real-time performance

Tracking enables the system to determine:

* Customer entry
* Customer exit
* Zone transitions
* Dwell duration
* Customer journeys

Without tracking, the same customer could be counted multiple times.

---

# Zone Intelligence Layer

## Purpose

The purpose of this layer is to understand where customers spend their time inside the store.

Instead of treating the store as a single area, the environment is divided into business-relevant zones.

## Zone Definitions

The store was simplified into the following zones:

### Entrance

Represents customer arrival and departure activity.

### Front of House (FOH)

Represents the primary customer browsing area.

### Makeup

Represents a product-focused engagement area.

### Shelf Area

Represents product browsing sections.

### Billing

Represents checkout and purchase activity.

## Design Decision

A simplified zone layout was intentionally chosen to:

* Reduce implementation complexity
* Improve interpretability
* Demonstrate business analytics concepts
* Support rapid prototyping

Future implementations could replace static zones with dynamically configurable store layouts.

---

# Event Generation Layer

## Purpose

The event layer converts low-level computer vision outputs into business-friendly events.

Instead of exposing raw detections and tracking data, the system generates meaningful events that represent customer behavior.

## Supported Events

### ENTRY

Generated when a visitor enters the store.

### EXIT

Generated when a visitor leaves the store.

### ZONE_ENTER

Generated when a visitor enters a new business zone.

### ZONE_DWELL

Generated when a visitor remains inside a zone beyond a predefined threshold.

## Benefits

This event-driven design:

* Decouples analytics from computer vision
* Simplifies reporting
* Enables future integrations
* Improves maintainability

---

# Event Storage

## Technology

JSONL (JSON Lines)

## Reasoning

JSONL was selected because:

* It is simple and human-readable
* Supports event streaming patterns
* Allows incremental appending
* Is easy to process with analytics tools

Each line represents a single business event.

Example:

{
"event_id":"...",
"event_type":"ENTRY",
"visitor_id":"VIS_0001"
}

This design mimics event-stream architectures commonly used in production systems.

---

# Analytics API Layer

## Purpose

The analytics layer provides structured access to generated business insights.

## Technology Selected

FastAPI

## Reasoning

FastAPI was selected because it provides:

* High performance
* Automatic Swagger documentation
* Strong typing support
* Simple development workflow
* Excellent Python ecosystem integration

## Implemented APIs

### Health Endpoint

Verifies service availability.

### Event Ingestion Endpoint

Accepts event payloads.

### Metrics Endpoint

Provides visitor and event statistics.

### Funnel Endpoint

Calculates customer funnel metrics.

### Anomaly Endpoint

Identifies unusual operational patterns.

---

# Dashboard Layer

## Purpose

The dashboard translates technical analytics into business-friendly visualizations.

## Technology Selected

Streamlit

## Reasoning

Streamlit was selected because:

* It enables rapid dashboard development
* Requires minimal frontend knowledge
* Integrates naturally with Python
* Supports fast prototyping

## Dashboard Features

* Visitor count
* Entry statistics
* Exit statistics
* Dwell event monitoring
* Event history display

The dashboard serves as a lightweight operational interface for store managers.

---

# Scalability Considerations

The current implementation focuses on demonstrating a complete working solution.

For production deployment, several architectural improvements would be recommended.

## Data Layer

* PostgreSQL
* Data warehouse integration

## Streaming Layer

* Kafka
* Event queues

## Caching

* Redis

## Infrastructure

* Docker
* Kubernetes
* Cloud deployment

## Analytics

* Heatmaps
* Customer journey reconstruction
* Multi-camera identity association

These enhancements would support large-scale deployments across multiple stores.

---

# Edge Cases and Limitations

The current implementation handles the primary workflow but does not fully address all production scenarios.

Examples include:

* Staff exclusion
* Re-entry behavior
* Occlusion handling
* Multi-camera tracking
* Identity re-association

These areas were identified as future enhancements.

---

# AI-Assisted Decisions

AI-assisted tools were used during development to accelerate research, documentation refinement, debugging support, and exploration of alternative implementation approaches.

AI assistance was primarily used for:

* Reviewing architectural alternatives
* Exploring implementation approaches
* Generating documentation drafts
* Debugging development issues
* Improving project structure
* Evaluating API design choices

All final engineering decisions, implementation details, testing activities, and validation steps were performed manually by the project author.

The final architecture, technology selection, event schema design, analytics implementation, and deployment decisions were independently reviewed and validated before submission.

AI tools were used as development assistants rather than autonomous decision makers.

Responsibility for all design choices, implementation quality, and system behavior remained entirely with the project author.

---

# Design Philosophy

The primary design principle was to build a complete end-to-end system that demonstrates how business insights can be derived from CCTV footage.

The solution prioritizes:

* Simplicity
* Modularity
* Maintainability
* Explainability
* Extensibility

Rather than optimizing for a single metric, the project focuses on demonstrating how computer vision, event-driven design, APIs, and dashboards can work together to create meaningful retail intelligence.

---

# Conclusion

The Purplle Store Intelligence System demonstrates how modern computer vision techniques can be integrated with analytics services and dashboards to transform CCTV footage into actionable business insights.

The architecture provides a strong foundation for future retail analytics applications and can be extended toward real-world production deployments through additional infrastructure, streaming, and data management capabilities.
