document.getElementById('submitBtn').addEventListener('click', async () => {
  const input = document.getElementById('secretInput').value.trim();
  const msgBox = document.getElementById('authMessage');
  msgBox.textContent = '';

  if (!input) {
    msgBox.textContent = 'Please enter a phrase.';
    return;
  }

  try {
    const normalized = input.trim().toLowerCase();
    const hashed = await sha256(normalized);
    const response = await fetch('https://bingepal.onrender.com/api/dev-logs', {
      headers: {
        'Authorization': hashed
      }
    });

    if (response.status === 401) {
      msgBox.textContent = '❌ Incorrect phrase. Try again!';
    } else if (!response.ok) {
      msgBox.textContent = '⚠️ Server error. Please try later.';
    } else {
      const logs = await response.text();
      window.localStorage.setItem('devLogs', logs);
      window.location.href = 'admin-console.html';  // next screen
    }
  } catch (err) {
    msgBox.textContent = 'Unexpected error.';
    console.error(err);
  }
});

async function sha256(message) {
  const encoder = new TextEncoder();
  const data = encoder.encode(message);
  const hashBuffer = await crypto.subtle.digest('SHA-256', data);
  return Array.from(new Uint8Array(hashBuffer))
    .map(b => b.toString(16).padStart(2, '0')).join('');
}
