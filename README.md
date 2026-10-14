<div align="center">

![Open-Meteo Free Weather API](banner.png)

# 🌦️ weather-etl

**ETL mini project: collects weather data from the Open-Meteo API and loads it into a PostgreSQL database.**

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1?logo=postgresql&logoColor=white)
![Requests](https://img.shields.io/badge/requests-HTTP-informational)

</div>

---

## About the project

This project implements the basic flow of a data pipeline:

1. **Extract**: consumes the free [Open-Meteo](https://open-meteo.com/) API (no API key required) using `requests`.
2. **Transform**: cleans and organizes the returned JSON (data types, column names, dates).
3. **Load**: writes the data into **PostgreSQL** tables, avoiding duplicates.

It was created to practice consuming APIs, error handling (retry/backoff), and persisting data in a relational database, as a first step toward data engineering.

> ⚠️ This project is still under development!

---
