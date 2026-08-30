import React, { useEffect, useRef } from 'react';
import './App.css';

export default function App() {
  const pyScriptStarted = useRef(false);

  const startCoffeeShop = () => {
    if (pyScriptStarted.current) return;

    pyScriptStarted.current = true;

    const script = document.createElement('script');
    script.type = 'py';
    script.src = `${import.meta.env.BASE_URL}coffee_shop.py`;
    script.setAttribute('config', '{"interpreter": "pyodide"}');

    document.getElementById('root').appendChild(script);
  };

  useEffect(() => {
    const id = requestAnimationFrame(startCoffeeShop);
    return () => cancelAnimationFrame(id);
  }, []);

  return (
    <div className="container">
      <div className="header">
        <h1>☕ COFFEE SHOP</h1>
        <p>Order your favorite coffee online (Powered by PyScript & React)!</p>
      </div>

      <p>Loading coffee menu...</p>
      <div id="output"></div>
      <div className="button-group" id="button-container"></div>
    </div>
  );
}
