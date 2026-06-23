# 🛒 Hyperlocal Price Intelligence System

## 📌 Overview

Hyperlocal Price Intelligence System is an end-to-end data analytics project that tracks product prices from e-commerce platforms, stores historical pricing data, analyzes market trends, generates buying recommendations, and forecasts future prices using Machine Learning.

The goal of this project is to help consumers make data-driven purchasing decisions by identifying the best time to buy a product based on historical price behavior.

---

## 🚀 Features

### 🔍 Automated Price Tracking

* Scrapes product prices from Amazon using BeautifulSoup.
* Collects product information and timestamps.
* Stores historical price records for trend analysis.

### 🗄️ Historical Data Storage

* Uses SQLite database for efficient storage.
* Maintains complete product price history.
* Supports long-term tracking and analysis.

### 📊 Interactive Analytics Dashboard

Built using Streamlit.

Dashboard provides:

* Total Products Tracked
* Average Price
* Lowest Price
* Highest Price
* Product-wise Price History
* Interactive Trend Visualization

### 💡 Smart Market Insights

* Best Deal Detection
* Most Volatile Product Analysis
* Product Ranking Based on Savings Potential

### 🔮 Price Forecasting

Uses Facebook Prophet to:

* Predict future prices
* Estimate expected price movement
* Generate Buy / Wait recommendations

### 🟢 Intelligent Buy Recommendation Engine

Based on historical price behavior:

* BUY NOW
* WAIT
* FAIR PRICE

---

## 🏗️ Project Architecture

```text
Hyperlocal_Price_Intelligence/
│
├── analytics/
│   ├── analysis.py
│   └── forecast.py
│
├── scraper/
│   └── scraper.py
│
├── data/
│   └── price_history.db
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Data Collection

* Requests
* BeautifulSoup

### Data Storage

* SQLite

### Data Analysis

* Pandas

### Machine Learning

* Prophet

### Visualization & Dashboard

* Streamlit
* Matplotlib

---

## 📊 Workflow

### Step 1: Data Collection

The scraper fetches product pages and extracts:

* Product Name
* Product Price
* Timestamp

### Step 2: Data Storage

Scraped information is stored inside SQLite database.

### Step 3: Analytics Layer

Historical data is processed to calculate:

* Current Price
* Average Price
* Lowest Price
* Highest Price
* Volatility

### Step 4: Recommendation Engine

Business rules determine whether users should:

* Buy Now
* Wait
* Monitor Prices

### Step 5: Forecasting

Prophet model predicts future price movement using historical trends.

### Step 6: Dashboard

Interactive Streamlit dashboard presents:

* KPIs
* Trend Analysis
* Product Insights
* Forecast Results

---

## 📈 Key Insights Generated

* Which product currently offers the best deal.
* Which product shows the highest price volatility.
* Historical pricing trends.
* Predicted future prices.
* Expected percentage change in price.

---

## ▶️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/Hyperlocal_Price_Intelligence.git
cd Hyperlocal_Price_Intelligence
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Dashboard

```bash
streamlit run app.py
```

---

## 📷 Dashboard Modules

### Dashboard

* Overall KPI Summary
* Product Performance Metrics
* Buy Recommendations

### Analytics

* Historical Trend Analysis
* Product-wise Price History

### Insights

* Best Deal Identification
* Product Ranking
* Volatility Analysis

### Forecast

* Future Price Prediction
* Expected Change Analysis
* Purchase Decision Support

---

## 🎯 Business Value

This project demonstrates how data analytics and machine learning can be used to:

* Monitor market prices.
* Identify purchasing opportunities.
* Reduce consumer spending.
* Improve decision making through predictive analytics.

Potential users include:

* Online shoppers
* Price comparison platforms
* Retail analysts
* E-commerce businesses

---

## 🧠 Skills Demonstrated

* Web Scraping
* Data Engineering
* SQL & SQLite
* Exploratory Data Analysis
* Business Analytics
* Machine Learning Forecasting
* Dashboard Development
* Data Visualization
* Streamlit Deployment

---

## 🔮 Future Enhancements

* Multi-platform price tracking (Amazon, Flipkart, Croma)
---

## 👨‍💻 Author

**Himanshu Vijay**

Aspiring Data Analyst | Data Science Enthusiast

This project was built to demonstrate practical skills in data collection, analytics, visualization, and predictive modeling through a real-world e-commerce price intelligence use case.
