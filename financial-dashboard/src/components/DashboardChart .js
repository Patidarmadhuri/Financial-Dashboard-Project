import React, { useState, useEffect } from "react";
import Plot from "react-plotly.js";


   const DashboardChart  = () => {
  const [plotData, setPlotData] = useState(null);

    useEffect(() => {
    fetch("http://localhost:5000/api/dashboard")
      .then((res) => res.json())
      .then((data) => setPlotData(data))
      .catch((err) => console.error("Error fetching dashboard:", err));
  }, []);

  if (!plotData) return <p>Loading dashboard...</p>;

  return (
    <Plot
      data={plotData.data}
      layout={plotData.layout}
      config={{ responsive: true }}
      style={{ width: "100%", height: "100%" }}
    />
  );
}

export default DashboardChart ;
