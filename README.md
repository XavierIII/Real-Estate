# RealEstateAI - AI-Powered Real Estate Analysis and Investment Tool

RealEstateAI is a comprehensive real estate analysis tool powered by **AI**, designed to help real estate investors make informed decisions. The app integrates **FastAPI** for backend operations and **Streamlit** for the frontend to create a smooth, interactive user experience.

### Features
- **Property Analysis**: Get detailed property analysis based on the property ID.
- **Sentiment Analysis**: Analyze sentiment for a given city’s real estate market.
- **Market Forecast**: Get insights on current and future market trends.
- **Investment Recommendations**: Receive personalized real estate investment advice.
- **Negotiation Strategy**: Get strategies for negotiating property deals.

---

## Project Structure
      ```bash
      realestateai/
      │
      ├── backend/
      │   ├── main.py        # FastAPI backend for handling API requests
      │   ├── agent.py       # LangGraph AI agents for analyzing properties and recommending strategies
      │   ├── db.py          # Database connection for Neo4j and storing data
      │
      ├── frontend/
      │   ├── streamlit_app.py   # Streamlit frontend for user interaction
      └── README.md          # This README file

---
## Requirements

Before you get started, ensure that you have the following installed:

### Backend (FastAPI)
- **Python 3.8+**: Make sure you have a compatible version of Python.
- **FastAPI**: A modern, fast web framework for building APIs.
- **Uvicorn**: An ASGI server for running FastAPI.
- **Neo4j** (Optional): For storing and querying property-related data.

### Frontend (Streamlit)
- **Streamlit**: Python package for creating interactive web applications.
- **Requests**: For making HTTP requests to the FastAPI backend.

---

## Installation

### 1. **Backend Setup (FastAPI)**

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/RealEstateAI.git
   cd RealEstateAI/backend
2. Set up a virtual environment and activate it (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. If you’re using Neo4j, ensure it’s installed and running. You can also modify the database connection in db.py to use a different database if needed.
5. Run the FastAPI backend:
   ```bash
   uvicorn main:app --reload
  This will start the FastAPI backend at http://localhost:8000.

### 2. **Frontend Setup (Streamlit)**

  1. Navigate to the frontend/ directory:
     ```bash
     cd ../frontend
  2. Set up a virtual environment and activate it (optional but recommended):
     ```bash
     python3 -m venv venv
     source venv/bin/activate  # On Windows, use venv\Scripts\activate
  3. Install Streamlit and Requests:
     ```bash
     pip install streamlit requests
  4. Run the Streamlit app:
     ```bash
     streamlit run streamlit_app.py
     
  ---

## Usage

Once the app is running, you can:

### **1. Property Analysis**
  - Input a property ID to get a detailed analysis of the property.
### **2. Sentiment Analysis**
  - Enter a city name (e.g., "Atlanta") to analyze the sentiment of the city’s real estate market.
### **3. Market Forecast**
  - View a forecast of current and future market trends.
### **4. Investment Recommendations**
  - Provide a user ID to receive personalized real estate investment recommendations based on your profile.
### **5. Negotiation Strategy**
  - Input a property ID to get strategies for negotiating a better deal for that specific property.

---

## API Endpoints

### **1. /agent/analyze_property/{property_id}**
  - Method: GET
  - Description: Fetch property analysis by ID.
  - Parameters: property_id (str) - The ID of the property.
  - Response: JSON object containing the analysis.
### **2. /properties/sentiment_analysis/{city}**
  - Method: GET
  - Description: Fetch sentiment analysis for a specific city.
  - Parameters: city (str) - The name of the city.
  - Response: JSON object containing sentiment analysis data.
### **3. /market_forecast/**
  - Method: GET
  - Description: Fetch the market forecast.
  - Response: JSON object containing market forecast data.
###  **4. /investments/recommend/{user_id}**
  - Method: GET
  - Description: Get personalized investment recommendations for a specific user.
  - Parameters: user_id (str) - The ID of the user.
  - Response: JSON object containing investment recommendations.
### **5. /negotiation/strategy/{property_id}**
  - Method: GET
  - Description: Get negotiation strategy for a given property.
  - Parameters: property_id (str) - The ID of the property.
  - Response: JSON object containing negotiation strategies.

---

## Deployment

### **1. Backend Deployment:**

  - The FastAPI backend can be deployed to any cloud service like AWS, Heroku, or Azure.
  - If using Heroku, create a Procfile with the following:
    ```less
    web: uvicorn main:app --host=0.0.0.0 --port=${PORT}
  - Push the backend to your Heroku repository and deploy it.

### **2. Frontend Deployment:**

  -  The Streamlit app can be deployed using Streamlit Cloud or Heroku.
  -  To deploy on Streamlit Cloud, follow the instructions on Streamlit Cloud Deployment.

---

## Credits
  - **FastAPI:** For the backend framework.
  - **Streamlit:** For the interactive frontend.
  - **LangGraph:** For AI-powered property analysis and recommendations.
  - **Neo4j:** Used (optionally) for property and market data storage.





