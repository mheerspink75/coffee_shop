import React from 'react';
import './App.css';

export default function App() {
  return (
    <div className="container">
      <div className="header">
        <h1>☕ COFFEE SHOP</h1>
        <p>Order your favorite coffee online (Powered by PyScript & React)!</p>
      </div>

      <div id="output"></div>
      <div className="button-group" id="button-container"></div>

      <script type="py" src="/coffee_shop.py" config='{"interpreter": "pyodide"}'></script>
    </div>
  );
}
