# 🚦 SafeRoads: ML-Driven Women Safety Recommendation System

SafeRoads is a full-stack application designed to enhance women’s safety in urban areas by providing intelligent travel recommendations based on real-time data. The system uses machine learning, geospatial data, and community feedback to assess and visualize the safety of different city areas, and to recommend safer routes accordingly.

---

## 📌 Project Overview

This project was developed as part of my final year engineering thesis. It combines multiple technologies—including data engineering, machine learning, web development, and mobile app development—to deliver a unified safety solution tailored for women in cities like **Chennai**.

---

## 🔧 Architecture Overview

Data Sources → ETL & Preprocessing → ML Model → Geo Grid Safety Scoring → Web Dashboard + Mobile App


---

## ✅ Features

- Real-time safety scoring for urban areas
- Smart and safe route recommendations
- Crowd-sourced user feedback system
- Admin dashboard for analytics and visualization
- Lightweight mobile app for quick and easy access

---

## 📊 Step 1: Data Collection & Cleaning

We collected, cleaned, and normalized **5 key datasets**:

1. **Crime Data**  
   Official city-level crime statistics filtered for incidents like harassment and assault.

2. **CCTV Coverage**  
   Locations of CCTV cameras across the city from municipal data, geotagged and mapped.

3. **Public Transport Access**  
   Data on bus stops, metro stations, and common taxi points to assess connectivity.

4. **Street Layout and Roads**  
   Extracted road network data from OpenStreetMap for spatial route calculations.

5. **Public Sentiment**  
   Analyzed tweets and community reports (e.g., Reddit, RedDot Foundation) using NLP.

### 🧼 Cleaning & Normalization

- Missing geolocations were filled via reverse geocoding  
- Irrelevant or off-city data was filtered  
- Normalized all feature values (0–1)  
- Mapped features into city-wide grid cells for model input

---

## 🧠 Step 2: Machine Learning Model

We trained ML models to assign **safety scores** to each grid cell in the city.

### ⚙️ Techniques Used:

- Logistic Regression and Random Forest classification  
- Feature engineering using the 5 collected datasets  
- DBSCAN for unsupervised hotspot detection  
- Sentiment classification using Bag-of-Words + XGBoost

### 🔎 Output:

Each grid cell gets a score (0–100) representing its safety based on current and historical data.

---

## 🖥️ Step 3: Web Dashboard (Frontend & Backend)

### 🔗 Backend (Python + Flask)

- Exposes REST APIs to serve safety scores, map overlays, and routes  
- Handles feedback submissions  
- Lightweight, file-based (uses CSV/GeoJSON instead of a DB)

### 🌐 Frontend (React + Leaflet.js)

- Interactive map with toggleable overlays (crime, CCTV, sentiment, etc.)  
- Route recommendation from source to destination  
- Admin panel to review analytics and user reports

---

## 📱 Step 4: Mobile App (Flutter)

A cross-platform mobile application for end users, built with Flutter.

### Features:

- View nearby areas with live safety scores  
- Get safe route suggestions based on safety score and shortest path  
- Submit feedback or report unsafe spots  
- Modern UI using custom themes and responsive layouts

---

## 🧰 Tech Stack

| Area              | Tools / Languages                   |
|-------------------|--------------------------------------|
| Data Collection   | Python, Pandas, OpenStreetMap APIs   |
| ML Modeling       | Scikit-learn, XGBoost, GeoPandas     |
| Web Backend       | Python Flask, REST APIs              |
| Web Frontend      | React.js, Leaflet.js, Vite           |
| Mobile App        | Flutter, Dart                        |
| Visualization     | GeoJSON, Leaflet heatmaps            |

---


## 🚀 Future Plans

- Automate live data fetching from open city APIs  
- Scale to other metro cities with automated grid generation  
- Add Firebase for authentication and real-time feedback  
- Push notifications for alerts or unsafe zones

---

## 🙋‍♂️ About Me

Hi, I'm **M Vignesh Muruga**, a passionate software developer from Trichy, building full-stack and AI-powered apps to solve real-world problems.

📌 [GitHub](https://github.com/Vickytech16)  
📌 [LinkedIn](https://linkedin.com/in/vigneshmuruga)

---

## 💬 Feedback & Collaboration

I'm open to feedback and collaboration.  
If you're interested in working on civic-tech, women safety, or mobility solutions—reach out!



