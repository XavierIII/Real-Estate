import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [propertyId, setPropertyId] = useState("");
  const [userId, setUserId] = useState("");
  const [analysis, setAnalysis] = useState(null);
  const [sentiment, setSentiment] = useState(null);
  const [marketForecast, setMarketForecast] = useState(null);
  const [investmentAdvice, setInvestmentAdvice] = useState(null);
  const [negotiationStrategy, setNegotiationStrategy] = useState(null);

  const fetchAnalysis = async () => {
    const result = await axios.get(`http://localhost:8000/agent/analyze_property/${propertyId}`);
    setAnalysis(result.data.property_analysis);
  };

  const fetchSentiment = async () => {
    const result = await axios.get(`http://localhost:8000/properties/sentiment_analysis/Atlanta`);
    setSentiment(result.data.sentiment_analysis);
  };

  const fetchMarketForecast = async () => {
    const result = await axios.get(`http://localhost:8000/market_forecast/`);
    setMarketForecast(result.data.market_forecast);
  };

  const fetchInvestmentAdvice = async () => {
    const result = await axios.get(`http://localhost:8000/investments/recommend/${userId}`);
    setInvestmentAdvice(result.data.investment_recommendations);
  };

  const fetchNegotiationStrategy = async () => {
    const result = await axios.get(`http://localhost:8000/negotiation/strategy/${propertyId}`);
    setNegotiationStrategy(result.data.negotiation_strategy);
  };

  return (
    <div className="App">
      <h1>Real Estate AI Dashboard</h1>

      <input
        type="text"
        placeholder="Enter Property ID"
        onChange={(e) => setPropertyId(e.target.value)}
      />
      <button onClick={fetchAnalysis}>Analyze Property</button>
      <div>{analysis && JSON.stringify(analysis)}</div>

      <button onClick={fetchSentiment}>Sentiment Analysis</button>
      <div>{sentiment && JSON.stringify(sentiment)}</div>

      <button onClick={fetchMarketForecast}>Market Forecast</button>
      <div>{marketForecast && JSON.stringify(marketForecast)}</div>

      <input
        type="text"
        placeholder="Enter User ID"
        onChange={(e) => setUserId(e.target.value)}
      />
      <button onClick={fetchInvestmentAdvice}>Investment Advice</button>
      <div>{investmentAdvice && JSON.stringify(investmentAdvice)}</div>

      <button onClick={fetchNegotiationStrategy}>Negotiation Strategy</button>
      <div>{negotiationStrategy && JSON.stringify(negotiationStrategy)}</div>
    </div>
  );
}

export default App;
