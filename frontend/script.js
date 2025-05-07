const userInput = document.getElementById('user-input');
  const sendBtn = document.getElementById('send-btn');
  const chatMessages = document.getElementById('chat-messages');

  // Substitua abaixo pela URL do seu backend hospedado
  const BACKEND_URL = "http://127.0.0.1:5000/chat";

  function addMessage(message, type) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `flex mb-4 ${type === 'user' ? 'justify-end' : ''}`;
    messageDiv.innerHTML = `
      <div class="${type}-message message-bubble">${message}</div>
    `;
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  async function sendMessage() {
    const message = userInput.value.trim();
    if (!message) return;

    // Mostra mensagem do usuário
    addMessage(message, 'user');
    userInput.value = '';

    try {
      const response = await fetch(BACKEND_URL, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: message })
      });

      const data = await response.json();

      if (data.reply) {
        addMessage(data.reply, 'bot');
      } else {
        addMessage("Erro ao obter resposta. Tente novamente mais tarde.", 'bot');
      }

    } catch (error) {
      console.error(error);
      addMessage("Erro de conexão com o servidor.", 'bot');
    }
  }

  sendBtn.addEventListener('click', sendMessage);
  userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') sendMessage();
  });