fetch("https://bingepal.onrender.com/api/admin-logs", {
  headers: {
    Authorization: "Bearer my_secret_token"
  }
})
.then(res => res.json())
.then(data => {
  const originalLogs = data.logs;

  // Replace all ISO datetime strings with localized versions
  const formattedLogs = originalLogs.replace(
    /\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z?/g,
    match => {
      const date = new Date(match);
      return isNaN(date) ? match : date.toLocaleString();
    }
  );

  document.getElementById("logOutput").value = formattedLogs;
})
.catch(err => {
  document.getElementById("logOutput").value = "Error loading logs.";
});
