from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from langgraph.agent import Agent
from langgraph.core import KnowledgeGraph
from typing import List
import os

# Initialize FastAPI
app = FastAPI()

# Define database connection (Neo4j)
from db import get_db_connection

# Initialize LangGraph agents
agent = Agent("Property_Analyzer", knowledge_graph=KnowledgeGraph())

# Property Analysis Model
class Property(BaseModel):
    id: str
    location: str
    price: float
    size_sqft: int
    bedrooms: int
    bathrooms: int

# Route to fetch property analysis
@app.get("/agent/analyze_property/{property_id}")
async def analyze_property(property_id: str):
    result = agent.analyze_property_data(property_id)
    return {"property_analysis": result}

# Route to get properties based on sentiment
@app.get("/properties/sentiment_analysis/{city}")
async def sentiment_analysis(city: str):
    result = agent.analyze_sentiment(city)
    return {"sentiment_analysis": result}

# Route to forecast market trends
@app.get("/market_forecast/")
async def forecast_market():
    result = agent.forecast_market_trends()
    return {"market_forecast": result}

# Route for personalized investment recommendations
@app.get("/investments/recommend/{user_id}")
async def personalized_investment(user_id: str):
    result = agent.recommend_investment(user_id)
    return {"investment_recommendations": result}

# Route to start negotiation assistant
@app.get("/negotiation/strategy/{property_id}")
async def negotiation_strategy(property_id: str):
    result = agent.negotiate_property(property_id)
    return {"negotiation_strategy": result}

# Run server with `uvicorn backend.main:app --reload`
