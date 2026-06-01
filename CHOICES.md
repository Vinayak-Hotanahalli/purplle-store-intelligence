# Technology Choices and Rationale

## Why YOLOv8?

YOLOv8 provides a good balance between speed and accuracy.

Reasons:

* Fast inference
* Easy integration
* Strong community support
* Suitable for real-time applications

For this challenge, rapid prototyping and reliability were more important than pursuing maximum accuracy.

---

## Why ByteTrack?

Tracking is essential for identifying customer movement over time.

ByteTrack was selected because:

* Lightweight
* Simple integration
* Stable identity assignment
* Strong performance in crowded scenes

It enables the system to create meaningful customer journeys.

---

## Why FastAPI?

FastAPI was chosen because:

* High performance
* Automatic API documentation
* Type safety
* Easy deployment

Swagger support significantly improves developer experience during testing.

---

## Why JSONL Storage?

JSONL provides a simple event log format.

Advantages:

* Human readable
* Easy debugging
* Append-friendly
* Simple integration with analytics workflows

For a challenge environment, JSONL is sufficient and keeps the architecture lightweight.

---

## Why Streamlit?

Streamlit enables rapid dashboard creation with minimal code.

Benefits:

* Quick setup
* Interactive UI
* Easy deployment
* Strong data visualization support

It allows business metrics to be demonstrated without building a full frontend application.

---

## Why Event-Driven Design?

Rather than storing only detections, the system stores business events.

Benefits:

* Easier analytics
* Better scalability
* Clear separation of concerns
* Compatibility with streaming architectures

This approach mirrors how many production retail analytics systems are designed.

---

## Trade-Offs Made

Several simplifications were intentionally made:

* Single camera assumption
* Simplified zones
* JSONL instead of a database
* Prototype dashboard
* Local execution

These decisions reduced complexity and allowed focus on delivering a complete working system within the challenge timeline.

---

## Final Thoughts

The selected technology stack prioritizes simplicity, maintainability, and demonstration value. Every technology was chosen based on how effectively it contributes to building an end-to-end store intelligence solution rather than maximizing technical complexity.
