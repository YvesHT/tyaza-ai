async function submitText() {
  const inputField = document.getElementById("user-input");
  const message = inputField.value.trim();
  if (!message) return;

  addMessage(message, "user");
  inputField.value = "";

  addTypingIndicator();

  try {
    const response = await fetch("https://your-backend-url.onrender.com/ask", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ question: message })
    });

    if (!response.ok) {
      throw new Error("Network response was not ok");
    }

    const data = await response.json();
    removeTypingIndicator();
    addMessage(data.answer, "ai");
  } catch (error) {
    removeTypingIndicator();
    addMessage("Error: Ntitwashoboye kuvugana na Tyaza.", "ai");
    console.error("Tyaza backend error:", error);
  }
}

function addMessage(text, sender) {
  const history = document.getElementById("history");
  const msg = document.createElement("div");
  msg.className = `message ${sender}-message`;
  msg.innerText = text;
  history.appendChild(msg);
  history.scrollTop = history.scrollHeight;
}

function addTypingIndicator() {
  const history = document.getElementById("history");
  const typing = document.createElement("div");
  typing.className = "typing-indicator ai-message";
  typing.id = "typing";
  typing.innerHTML = `
    <div class="typing-text">Tyaza aratekereza...</div>
    <div class="typing-dots">
      <div class="typing-dot"></div>
      <div class="typing-dot"></div>
      <div class="typing-dot"></div>
    </div>
  `;
  history.appendChild(typing);
  history.scrollTop = history.scrollHeight;
}

function removeTypingIndicator() {
  const typing = document.getElementById("typing");
  if (typing) typing.remove();
}
