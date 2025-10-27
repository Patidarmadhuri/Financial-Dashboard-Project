import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Plot from 'react-plotly.js';

const DashboardChart = () => {
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
      const response = await axios.post('http://localhost:5000/api/login', {
        username,
        password,
      });
      const { token } = response.data;
      setToken(token);
      localStorage.setItem('token', token);
      setError(null);
      await fetchDashboard();
    } catch (err) {
      setError(err.response?.data?.error || 'Login failed');
    } finally {
      setLoading(false);
    }
  };

  // Fetch dashboard data
  const fetchDashboard = async () => {
    setLoading(true);
    try {
      const response = await axios.get('http://localhost:5000/api/dashboard', {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      setDashboardData(response.data);
      setError(null);
    } catch (err) {
      setError(err.response?.data?.msg || 'Failed to fetch dashboard');
    } finally {
      setLoading(false);
    }
  };

  // Fetch dashboard on mount if token exists
  useEffect(() => {
    if (token) {
      fetchDashboard();
    }
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