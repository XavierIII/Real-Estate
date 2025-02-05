import streamlit as st
import requests

# Define the FastAPI backend URL
BASE_URL = "http://localhost:8000"  # Update with your FastAPI backend URL

# Streamlit App - Real Estate AI Dashboard

# Title of the app
st.title('Real Estate AI Dashboard')

# Sidebar for user inputs
st.sidebar.header("Enter Property Details")
property_id = st.sidebar.text_input("Enter Property ID", "")
user_id = st.sidebar.text_input("Enter User ID", "")

# Buttons to trigger different API calls
if st.sidebar.button('Analyze Property'):
    if property_id:
        response = requests.get(f"{BASE_URL}/agent/analyze_property/{property_id}")
        if response.status_code == 200:
            property_analysis = response.json()
            st.subheader(f"Property Analysis for ID: {property_id}")
            st.write(property_analysis["property_analysis"])
        else:
            st.error("Failed to fetch property analysis.")

if st.sidebar.button('Sentiment Analysis'):
    city = st.sidebar.text_input("Enter City for Sentiment Analysis", "Atlanta")
    if city:
        response = requests.get(f"{BASE_URL}/properties/sentiment_analysis/{city}")
        if response.status_code == 200:
            sentiment = response.json()
            st.subheader(f"Sentiment Analysis for {city}")
            st.write(f"Sentiment Score: {sentiment['sentiment_analysis']}")
        else:
            st.error("Failed to fetch sentiment analysis.")

if st.sidebar.button('Market Forecast'):
    response = requests.get(f"{BASE_URL}/market_forecast/")
    if response.status_code == 200:
        market_forecast = response.json()
        st.subheader("Market Forecast")
        st.write(market_forecast["market_forecast"])
    else:
        st.error("Failed to fetch market forecast.")

if st.sidebar.button('Investment Recommendations'):
    if user_id:
        response = requests.get(f"{BASE_URL}/investments/recommend/{user_id}")
        if response.status_code == 200:
            investment_advice = response.json()
            st.subheader(f"Personalized Investment Recommendations for User {user_id}")
            st.write(investment_advice["investment_recommendations"])
        else:
            st.error("Failed to fetch investment recommendations.")

if st.sidebar.button('Negotiation Strategy'):
    if property_id:
        response = requests.get(f"{BASE_URL}/negotiation/strategy/{property_id}")
        if response.status_code == 200:
            negotiation_strategy = response.json()
            st.subheader(f"Negotiation Strategy for Property ID: {property_id}")
            st.write(negotiation_strategy["negotiation_strategy"])
        else:
            st.error("Failed to fetch negotiation strategy.")

# Add some additional information or customization as necessary
st.sidebar.markdown("### How It Works")
st.sidebar.markdown("""
1. **Property Analysis** - Get a detailed analysis of a property based on its ID.
2. **Sentiment Analysis** - View the sentiment score for a specific city.
3. **Market Forecast** - Get a market forecast for real estate trends.
4. **Investment Recommendations** - Receive personalized recommendations for your real estate investments.
5. **Negotiation Strategy** - Get a negotiation strategy for a given property.
""")

# Footer or additional information
st.markdown("### Powered by RealEstateAI 🚀")
