function loadHistory() {

  fetch('https://bingepal.onrender.com/api/history?limit=50')
    .then(res => res.json())
    .then(data => {
      const logList = document.getElementById("logList");
      data.forEach(item => {
        const formattedDate = new Date(item.timestamp).toLocaleString().replace(tzinfo=timezone.utc).isoformat();
        const row = document.createElement("tr");
        row.innerHTML = `<td>${formattedDate}</td><td>${item.type}</td><td>${item.title}</td>`;
        logList.appendChild(row);
      });
    });

}

// Auto-load
document.addEventListener("DOMContentLoaded", loadHistory);
