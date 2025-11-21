import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Plot from 'react-plotly.js';

const DashboardChart = () => {
  const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';
  const [charts, setCharts] = useState({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [activeTab, setActiveTab] = useState(0);
  const [tab4Title, setTab4Title] = useState("4. Debt vs Liquid Assets");

  useEffect(() => {
    const fetchCharts = async () => {
      try {
        const response = await axios.get(`${API_URL}/api/charts`);
        setCharts(response.data || {});
        setError(null);
      } catch (err) {
        setError('Failed to load charts.');
      } finally {
        setLoading(false);
      }
    };
    fetchCharts();
  }, [API_URL]);

  const tabs = [
    { title: "1. CCP & LTD by Company", short: "Cash vs Debt trends over time" },
    { title: "2. Debt Coverage Ratio", short: "How many times cash covers long-term debt" },
    { title: "3. Financial Resilience Heatmap", short: "One-glance strength across companies & quarters" },
    { title: tab4Title, short: "Bubble size = coverage strength • Position = risk level" }
  ];

  const explanations = [
    "Solid line = Cash • Dashed line = Debt\nWidening gap = getting stronger\nUse dropdown to show only cash or debt",
    "Cash ÷ Debt = Coverage Ratio\n>1 = Safe • <0.5 = Risk zone\nGreen = Strong • Red = Danger",
    "Cool color (green) = financially strong\nWarm colors (yellow/red) = stress periods\nSee who improved over time",
    "Bottom-right = Bulletproof (high cash, low debt)\nTop-left = High risk\nBubble size = coverage power\nRed/blue lines = medians"
  ];

  if (loading) return <div className="text-center py-32 text-3xl text-gray-600 font-light">Loading dashboard...</div>;
  if (error) return <div className="text-center py-32 text-red-600 text-xl">{error}</div>;

  const currentChart = charts[`chart${activeTab}`];

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-100 py-10 px-4">

      {/* FINAL HERO SECTION – PERFECT 2026 STYLE */}
      <div className="text-center max-w-5xl mx-auto mb-20">
        <h1 className="text-5xl md:text-6xl font-black text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-purple-700 mb-10">
          Financial Dashboard
        </h1>

        <div className="grid md:grid-cols-3 gap-6 max-w-4xl mx-auto">
          <div className="bg-white/70 backdrop-blur-lg rounded-3xl p-7 shadow-xl border border-white/50">
            <div className="text-4xl font-bold text-amber-600 mb-3">Question</div>
            <p className="text-lg leading-relaxed text-slate-800">
              Can these companies survive the next crisis?
            </p>
          </div>

          <div className="bg-gradient-to-br from-blue-600 to-purple-700 text-white rounded-3xl p-8 shadow-2xl transform scale-105">
            <div className="text-4xl font-bold mb-3">Answer</div>
            <p className="text-lg leading-relaxed font-medium">
              Some are <span className="font-bold text-green-300">bulletproof</span>.<br/>
              Others are <span className="font-bold text-red-300">one shock away</span> from trouble.
            </p>
          </div>

          <div className="bg-white/70 backdrop-blur-lg rounded-3xl p-7 shadow-xl border border-white/50">
            <div className="text-4xl font-bold text-indigo-600 mb-3">Tech</div>
            <p className="text-lg leading-relaxed text-slate-800">
              React • Plotly • Flask • MongoDB Atlas
            </p>
          </div>
        </div>

        {/* ONE-LINE PROJECT DESCRIPTION */}
        <div className="mt-12">
          <p className="text-xl md:text-2xl font-medium text-slate-700 max-w-4xl mx-auto leading-relaxed">
            Instantly compare <span className="font-bold text-blue-600">cash reserves vs long-term debt</span> of major companies across quarters — see who’s <span className="text-green-500 font-bold">bulletproof</span> and who’s <span className="text-red-500 font-bold">at risk</span> in the next crisis.
          </p>
        </div>
      </div>

      {/* Tabs */}
      <div className="flex justify-center flex-wrap gap-4 mb-12">
        {tabs.map((tab, i) => (
          <button
            key={i}
            onClick={() => setActiveTab(i)}
            className={`px-10 py-5 rounded-2xl font-bold text-lg transition-all transform hover:scale-105 shadow-lg ${
              activeTab === i
                ? 'bg-gradient-to-r from-blue-600 to-purple-600 text-white'
                : 'bg-white text-slate-700 hover:shadow-2xl'
            }`}
          >
            {tab.title}
          </button>
        ))}
      </div>

      {/* Short tagline */}
      <p className="text-center text-2xl font-medium text-slate-700 mb-12 max-w-4xl mx-auto">
        {tabs[activeTab].short}
      </p>

      {/* Main Chart */}
      <div className="bg-white/90 backdrop-blur-sm rounded-3xl shadow-2xl p-10 max-w-7xl mx-auto border border-gray-200">
        <Plot
          data={currentChart.data}
          layout={{
            ...currentChart.layout,
            height: 720,
            margin: { t: 160, b: 100, l: 110, r: 90 },
            title: {
              text: currentChart.layout?.title?.text || '',
              font: { size: 26, color: '#1e293b' },
              x: 0.5, y: 0.89, xanchor: 'center', yanchor: 'top'
            }
          }}
          config={{ responsive: true, displayModeBar: true, displaylogo: false }}
          style={{ width: '100%' }}
          onRelayout={(ed) => {
            if (activeTab === 3 && ed?.["title.text"]) {
              const text = ed["title.text"];
              const quarter = text.includes("Q") ? text.split(": ")[1] : "Median Across Quarters";
              setTab4Title(`4. Debt vs Liquid Assets: ${quarter}`);
            }
          }}
        />

        {/* Explanation */}
        <div className="mt-12 p-10 bg-gradient-to-r from-slate-50 to-indigo-50 rounded-3xl border-l-8 border-indigo-600">
          <h3 className="text-3xl font-bold text-slate-800 mb-6">How to read this chart</h3>
          <p className="text-xl text-slate-700 leading-relaxed whitespace-pre-line">
            {explanations[activeTab]}
          </p>
        </div>
      </div>

      {/* Footer */}
      <div className="text-center mt-20 text-gray-600 text-lg">
        Built by <span className="font-bold text-blue-600">Madhuri Patidar</span> • Full-Stack Developer • 2025
      </div>
    </div>
  );
};

export default DashboardChart;