let chart;

function loadTrends() {
  const type = document.getElementById("typeSelect").value;
  const days = document.getElementById("rangeSelect").value;

  fetch(`https://bingepal.onrender.com/api/trending?type=${type}&days=${days}`)
    .then(res => res.json())
    .then(data => {
      const labels = data.trending.map(item => item.title);
      const values = data.trending.map(item => item.count);

      if (chart) chart.destroy();

      chart = new Chart(document.getElementById("trendChart"), {
        type: "bar",
        data: {
          labels: labels,
          datasets: [{
            label: `${type.toUpperCase()} (${days}d)`,
            data: values,
            backgroundColor: "#6f42c1"
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: {
              labels: {
                font: {
                  size: window.innerWidth < 576 ? 10 : 14
                }
              }
            }
          },
          scales: {
            x: {
              ticks: {
                font: {
                  size: window.innerWidth < 576 ? 8 : 12
                }
              }
            },
            y: {
              ticks: {
                font: {
                  size: window.innerWidth < 576 ? 8 : 12
                }
              }
            }
          }
        }
      });
    });
}

// Auto-load first view
document.addEventListener("DOMContentLoaded", loadTrends);
