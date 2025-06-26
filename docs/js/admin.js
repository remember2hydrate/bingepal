document.addEventListener("DOMContentLoaded", () => {
  const logsDiv = document.getElementById("logs");
  const tokenInput = document.getElementById("tokenInput");
  const submitBtn = document.getElementById("submitToken");

  const modal = new bootstrap.Modal(document.getElementById("clueModal"));
  modal.show();

  submitBtn.addEventListener("click", async () => {
    const token = tokenInput.value.trim();
    if (!token) return;

    const hash = await sha256(token);

    try {
      const res = await fetch("https://bingepal.onrender.com/api/dev-logs", {
        headers: { Authorization: hash },
      });

      const data = await res.text();
      
      if (res.status === 401) {
        msgBox.textContent = '❌ Incorrect phrase. Try again!';
      } else if (!res.ok) {
        msgBox.textContent = '⚠️ Server error. Please try later.';
      } else {
        logsDiv.textContent = data;
        logsDiv.style.filter = "none";
        logsDiv.style.pointerEvents = "auto";
        modal.hide();
      }
    } catch (err) {
      logsDiv.textContent = "Failed to fetch logs.";
    }
  });
});

async function sha256(str) {
  const buffer = new TextEncoder().encode(str);
  const hashBuffer = await crypto.subtle.digest("SHA-256", buffer);
  return Array.from(new Uint8Array(hashBuffer))
    .map(b => b.toString(16).padStart(2, "0"))
    .join("");
}