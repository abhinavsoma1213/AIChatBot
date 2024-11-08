document.addEventListener('DOMContentLoaded', () => {
    const sendButton = document.getElementById('send-button');
    const userInput = document.getElementById('user-input');
    const chatWindow = document.getElementById('chat-window');

    sendButton.addEventListener('click', () => {
        sendMessage();
    });

    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    function sendMessage() {
        const messageText = userInput.value.trim();
        if (messageText === '') return;

        const userMessage = document.createElement('div');
        userMessage.classList.add('message', 'user-message');
        const userContent = document.createElement('div');
        userContent.classList.add('message-content');
        userContent.textContent = messageText;
        userMessage.appendChild(userContent);
        chatWindow.appendChild(userMessage);

        // Clear input
        userInput.value = '';

        // Scroll to bottom
        chatWindow.scrollTop = chatWindow.scrollHeight;

        // Simulate bot response (for demonstration)
        setTimeout(() => {
            const botMessage = document.createElement('div');
            botMessage.classList.add('message', 'bot-message');
            const botContent = document.createElement('div');
            botContent.classList.add('message-content');
            botContent.textContent = "Thank you for your message. We're looking into it!";
            botMessage.appendChild(botContent);
            chatWindow.appendChild(botMessage);
            chatWindow.scrollTop = chatWindow.scrollHeight;
        }, 1000);
    }
});
