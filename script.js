document.addEventListener("DOMContentLoaded", () => {
  const chatHistory = document.querySelector(".chat-history");
  const inputField = document.getElementById("user-input");
  const sendBtn = document.querySelector(".send-btn");
  const moodSelector = document.querySelector(".mood-selector");

  // Handle sending messages
  function sendMessage() {
    const message = inputField.value.trim();
    if (message === "") return;

    appendMessage("user", message);
    inputField.value = "";
    inputField.style.height = "auto";

    // Simulated AI response (Replace this with your real AI call)
    setTimeout(() => {
      appendMessage("ai", "Ndumva neza ibyo uvuga! 😊");
    }, 800);
  }

  // Create and append a message to chat
  function appendMessage(sender, text) {
    const messageDiv = document.createElement("div");
    messageDiv.classList.add("message");
    messageDiv.classList.add(sender === "user" ? "user-message" : "ai-message");
    messageDiv.textContent = text;

    chatHistory.appendChild(messageDiv);
    chatHistory.scrollTop = chatHistory.scrollHeight;
  }

  // Auto resize textarea
  inputField.addEventListener("input", () => {
    inputField.style.height = "auto";
    inputField.style.height = inputField.scrollHeight + "px";
  });

  // Send on button click
  sendBtn.addEventListener("click", sendMessage);

  // Send on Enter key
  inputField.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  });

  // Toggle mood selector
  document.querySelector(".mood-btn")?.addEventListener("click", () => {
    moodSelector.classList.toggle("active");
  });

  // Star twinkle generator (optional eye-candy)
  const bg = document.querySelector(".cosmic-bg");
  for (let i = 0; i < 100; i++) {
    const star = document.createElement("div");
    star.classList.add("star");
    star.style.width = star.style.height = `${Math.random() * 2 + 1}px`;
    star.style.top = `${Math.random() * 100}%`;
    star.style.left = `${Math.random() * 100}%`;
    star.style.animationDuration = `${Math.random() * 5 + 5}s`;
    bg.appendChild(star);
  }
});
