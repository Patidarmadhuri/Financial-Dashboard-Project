import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Plot from 'react-plotly.js';

const DashboardChart = () => {
  const API_URL = process.env.REACT_APP_API_URL;
  const [charts, setCharts] = useState({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchCharts = async () => {
      try {
        const response = await axios.get(`${API_URL}/api/charts`);
        setCharts(response.data);
        setError(null);
      } catch (err) {
        setError('Failed to load charts. Check backend.');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };
    fetchCharts();
  }, [API_URL]);

  const chartTitles = [
    "1. CCP & LTD by Company",
    "2. Debt Coverage Ratio",
    "3. Financial Resilience Heatmap",
    "4. Debt vs Liquid Assets (all)"
  ];

  if (loading) return <div style={{ textAlign: 'center', padding: '3rem' }}>Loading...</div>;
  if (error) return <div style={{ textAlign: 'center', padding: '3rem', color: 'red' }}>{error}</div>;

  const chartKeys = Object.keys(charts);

  return (
    <div style={{ padding: '2rem', fontFamily: 'Arial, sans-serif', maxWidth: '1400px', margin: '0 auto' }}>
      <div style={{ textAlign: 'center', marginBottom: '2.5rem' }}>
        <h1 style={{ color: '#2c3e50', margin: 0, fontSize: '2.2rem' }}>
          Financial Resilience Dashboard
        </h1>
        <p style={{ color: '#7f8c8d', margin: '0.5rem 0' }}>
          Interactive Financial Visualizations | 4 Charts
        </p>
      </div>

      {chartKeys.map((id, index) => {
        const c = charts[id];
        const title = chartTitles[index] || "Chart";

        return (
          <div
            key={id}
            style={{
              margin: '3rem 0',
              padding: '2rem',
              background: '#fff',
              borderRadius: '12px',
              boxShadow: '0 4px 12px rgba(0,0,0,0.1)',
              border: '1px solid #e9ecef'
            }}
          >
            <h2 style={{ color: '#2c3e50', marginBottom: '1.5rem' }}>{title}</h2>
            <Plot
              data={c.data}
              layout={{
                ...c.layout,
                height: 620,
                margin: { t: 60, b: 100, l: 80, r: 40 }
              }}
              config={{
                responsive: true,
                displayModeBar: true,
                displaylogo: false,
                toImageButtonOptions: {
                  format: 'png',
                  filename: title.replace(/ /g, '_')
                }
              }}
              style={{ width: '100%' }}
            />
          </div>
        );
      })}
    </div>
  );
};

export default DashboardChart;