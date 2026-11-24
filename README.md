# Marketplace Data Engineering & Analytics Platform

## 1. Project Overview

This project focuses on building a batch-based data engineering and analytics platform using a public e-commerce dataset from Retailrocket.

The platform is designed to ingest, validate, transform, store and deliver marketplace interaction data for analytical purposes.

The dataset contains approximately 2.75 million timestamped user events, including product views, add-to-cart activities and transactions.

This is an independent academic project and does not use any company's internal or proprietary data.

## 2. Project Objectives

- Build a reproducible batch data processing pipeline.
- Process large-scale e-commerce interaction data.
- Perform data cleaning, validation and transformation.
- Integrate product metadata and category information.
- Store analytical datasets efficiently.
- Deliver insights through an interactive dashboard.
- Apply containerization, version control and data governance practices.

## 3. Technology Stack

| Component | Technology |
|---|---|
| Programming | Python |
| Data Processing | PySpark |
| Data Manipulation | Pandas |
| Data Storage | Parquet |
| Analytical Database | PostgreSQL |
| Dashboard | Streamlit |
| Containerization | Docker |
| Version Control | Git and GitHub |

## 4. Dataset

Source: Retailrocket E-commerce Dataset  
https://www.kaggle.com/datasets/retailrocket/ecommerce-dataset

The dataset includes:

- `events.csv` – User interaction events.
- `item_properties_part1.csv` – Product properties.
- `item_properties_part2.csv` – Additional product properties.
- `category_tree.csv` – Product category relationships.

Initial exploration identified:
- 2,756,101 event records.
- 460 exact duplicate event records.
- 235,061 unique products in the event data.
- 185,246 event products matched with available metadata.

Unmatched product records will be preserved during processing.

## 5. Proposed Architecture

The platform follows a modular batch-processing architecture:

1. Data Ingestion: Load and validate source datasets.
2. Data Processing: Clean events, remove duplicates, integrate metadata and generate aggregates using PySpark.
3. Data Storage: Preserve raw source files and store transformed data in Parquet.
4. Database Layer: Load analytical datasets into PostgreSQL.
5. Analytics Delivery: Present marketplace insights through Streamlit.
6. Orchestration: Schedule repeatable batch processing.
7. Deployment: Use Docker Compose to coordinate application services.

## 6. Project Structure

```text
marketplace-data-platform/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── synthetic/
│
├── ingestion/
├── processing/
├── database/
├── streaming/
├── dashboard/
│   └── pages/
├── tests/
├── docs/
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .gitignore
└── README.md
```

## 7. Data Quality and Governance

The project incorporates the following practices:

- Preserve original source datasets.
- Remove exact duplicate event records.
- Validate data types and required fields.
- Track unmatched product metadata.
- Keep credentials outside version control.
- Document data sources and processing lineage.
- Use Git for version control.

## 8. Current Implementation Status

- [x] Dataset acquisition and exploration
- [x] Initial data quality assessment
- [x] Event cleaning using Pandas
- [x] Git repository initialisation
- [x] Initial GitHub commit and upload
- [ ] PySpark processing pipeline
- [ ] Product metadata integration
- [ ] PostgreSQL analytical storage
- [ ] Streamlit dashboard
- [ ] Docker-based deployment
- [ ] Automated batch scheduling
- [ ] Testing and documentation

## 9. Future Improvements

A separate real-time streaming pipeline could be introduced using technologies such as Apache Kafka and Spark Structured Streaming to complement the batch architecture.

## 10. Academic Context

Developed as part of the Data Engineering coursework at IU International University of Applied Sciences.