fetch('/api/coins')
  .then(res => res.json())
  .then(data => {
    const container = document.getElementById('coin-data');
    container.innerHTML = '<pre>' + JSON.stringify(data, null, 2) + '</pre>';
  });
