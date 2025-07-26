async function sendMessage() {
  const input = document.getElementById("user-input");
  const message = input.value;
  if (!message) return;
  document.getElementById("chat-box").innerHTML += `<div><b>You:</b> ${message}</div>`;
  input.value = "";

  const response = await fetch("http://localhost:5501/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ query: message })
  });

  const data = await response.json();
  document.getElementById("chat-box").innerHTML += `<div><b>Bot:</b> ${JSON.stringify(data)}</div>`;
}