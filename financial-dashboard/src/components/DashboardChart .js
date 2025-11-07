import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Plot from 'react-plotly.js';

const DashboardChart = () => {
  const API_URL = process.env.REACT_APP_API_URL;
  const [token, setToken] = useState(localStorage.getItem('token') || '');
  const [dashboardData, setDashboardData] = useState(null);
  const [error, setError] = useState(null);
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);

  // Handle login
  const handleLogin = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const response = await axios.post(`${API_URL}/api/login`, {
        username,
        password,
      });
      const { token } = response.data;
      setToken(token);
      localStorage.setItem('token', token);
      setError(null);
      await fetchDashboard(token);
    } catch (err) {
      console.error('Login error:', err);
      setError(err.response?.data?.error || 'Login failed');
    } finally {
      setLoading(false);
    }
  };

  // Fetch dashboard data
  const fetchDashboard = async (currentToken = token) => {
    setLoading(true);
    try {
      const response = await axios.get(`${API_URL}/api/dashboard`, {
        headers: {
          Authorization: `Bearer ${currentToken}`,
        },
      });
      setDashboardData(response.data);
      setError(null);
    } catch (err) {
      console.error('Fetch error:', err);
      setError(err.response?.data?.error || 'Failed to fetch dashboard');
    } finally {
      setLoading(false);
    }
  };

  // Fetch dashboard on mount if token exists
  useEffect(() => {
    if (token) {
      fetchDashboard();
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [token]);

  return (
    <div>
      {!token ? (
        <form onSubmit={handleLogin}>
          <input
            type="text"
            placeholder="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          <button type="submit" disabled={loading}>
            {loading ? 'Logging in...' : 'Login'}
          </button>
          {error && <p style={{ color: 'red' }}>{error}</p>}
        </form>
      ) : (
        <div>
          {loading && <p>Loading dashboard...</p>}
          {error && <p style={{ color: 'red' }}>{error}</p>}
          {dashboardData && (
            <Plot
              data={dashboardData.data}
              layout={{
                ...dashboardData.layout,
                width: 1200,
                height: 600,
              }}
            />
          )}
          <button
            onClick={() => {
              setToken('');
              localStorage.removeItem('token');
              setDashboardData(null);
            }}
          >
            Logout
          </button>
        </div>
      )}
    </div>
  );
};

export default DashboardChart;
