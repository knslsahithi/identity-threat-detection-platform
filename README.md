# Identity Threat Detection and Response (ITDR) Platform

## Project Overview

The Identity Threat Detection and Response (ITDR) Platform is a cybersecurity solution designed to simulate and monitor identity-based activities in an enterprise environment. The platform generates identity events, validates and normalizes them, stores them for auditing, and streams them using Apache Kafka for downstream security analytics.

This project is being developed as part of my Cyber Security Internship at **Zaalima Development Pvt Ltd**.

---

## Week 1 Progress

✅ Project Setup

✅ Identity Event Simulator

✅ Identity Event Model

✅ Event Validation

✅ Event Normalization

✅ Event Logging

✅ Apache Kafka Integration

✅ Kafka Producer

✅ Kafka Consumer

---

## Features

- Simulates enterprise identity events
- Validates incoming identity events
- Normalizes events into a standard schema
- Stores normalized events for auditing
- Streams events using Apache Kafka
- Docker-based deployment

---

## Technology Stack

### Backend

- Python 3.14
- FastAPI

### Event Streaming

- Apache Kafka
- ZooKeeper

### Containerization

- Docker
- Docker Compose

### Future Technologies

- Neo4j Graph Database
- Elasticsearch
- Kubernetes

---

## Project Architecture

```text
Identity Event Simulator
        │
        ▼
Identity Event Model
        │
        ▼
Event Validator
        │
        ▼
Event Normalizer
        │
        ▼
Event Logger
        │
        ▼
Kafka Producer
        │
        ▼
Apache Kafka
        │
        ▼
Kafka Consumer
```

---

## Folder Structure

```text
identity-threat-detection-platform
│
├── database
├── docs
├── ingestion
├── k8s
├── logs
├── models
├── services
├── tests
├── Dockerfile
├── docker-compose.yml
├── README.md
├── requirements.txt
└── main.py
```

---

## Current Status

✅ Week 1 Completed

### Upcoming

- Identity Graph using Neo4j
- Blast Radius Analysis
- Threat Detection Engine
- Automated Response APIs
- SOC Dashboard

---

## Author

**Sahithi**

Cyber Security Intern

Zaalima Development Pvt Ltd