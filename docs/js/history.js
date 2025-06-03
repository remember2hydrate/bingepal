function loadHistory() {
  const type = document.getElementById("historyTypeSelect").value;

  fetch(`https://bingepal.onrender.com/api/trending?type=${type}&days=3650`) // ~10 years = lifetime
    .then(res => res.json())
    .then(data => {
      const tbody = document.getElementById("historyTableBody");
      tbody.innerHTML = "";

      data.trending.forEach((item, index) => {
        const row = `
          <tr>
            <td>${index + 1}</td>
            <td>${item.title} (${item.year})</td>
            <td>${item.count}</td>
          </tr>`;
        tbody.insertAdjacentHTML("beforeend", row);
      });
    });
}

// Auto-load
document.addEventListener("DOMContentLoaded", loadHistory);
