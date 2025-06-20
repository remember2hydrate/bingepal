fetch("https://bingepal.onrender.com/api/admin-logs", {
  headers: {
    Authorization: "Bearer my_secret_token"
  }
})
.then(res => res.json())
.then(data => {
  const originalLogs = data.logs;

  const formattedLogs = originalLogs.replace(
    /\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z?/g,
    match => {
      const utcDate = new Date(match);
      if (isNaN(utcDate)) return match;

      // Convert to local time explicitly
      return utcDate.toLocaleString(undefined, {
        year: "numeric", month: "short", day: "numeric",
        hour: "2-digit", minute: "2-digit", second: "2-digit",
        hour12: false,
        timeZone: Intl.DateTimeFormat().resolvedOptions().timeZone
      });
    }
  );

  document.getElementById("logOutput").value = formattedLogs;
})
.catch(err => {
  document.getElementById("logOutput").value = "Error loading logs.";
});
