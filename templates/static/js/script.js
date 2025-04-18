function sendMessage() {
    const input = document.getElementById("userInput");
    const chatWindow = document.getElementById("chatWindow");
    const message = input.value.trim();
  
    if (message === "") return;
  
    // Show user's message
    chatWindow.innerHTML += `<div class="user">${message}</div>`;
    input.value = "";
    chatWindow.scrollTop = chatWindow.scrollHeight;
  
    // Show loading dots (simulate typing)
    const loader = document.createElement("div");
    loader.classList.add("bot");
    loader.innerText = "Abhishek Bot is typing...";
    chatWindow.appendChild(loader);
  
    // Send message to Flask backend
    fetch("/get", {
      method: "POST",
      body: JSON.stringify({ message }),
      headers: { "Content-Type": "application/json" }
    })
    .then(res => res.json())
    .then(data => {
      loader.remove();
      chatWindow.innerHTML += `<div class="bot">${data.reply}</div>`;
      chatWindow.scrollTop = chatWindow.scrollHeight;
    });
  }
  