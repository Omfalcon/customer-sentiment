class SentimentDashboard {
    constructor() {
        this.loadMessages();
        this.loadAnalytics();
        setInterval(() => {
            this.loadMessages();
            this.loadAnalytics();
        }, 5000); // Update every 5 seconds
    }

    async loadMessages() {
        try {
            const response = await fetch('/api/messages');
            const messages = await response.json();
            this.displayMessages(messages);
            this.updateSpeedometer(messages);
        } catch (error) {
            console.error('Error loading messages:', error);
        }
    }

    async loadAnalytics() {
        try {
            const response = await fetch('/api/analytics');
            const analytics = await response.json();
            this.displayAnalytics(analytics);
        } catch (error) {
            console.error('Error loading analytics:', error);
        }
    }

    displayMessages(messages) {
        const container = document.getElementById('messagesContainer');
        container.innerHTML = '';

        messages.forEach(msg => {
            const messageEl = document.createElement('div');
            messageEl.className = `message-card ${msg.sentiment}`;

            messageEl.innerHTML = `
                <div class="customer-name">${msg.customer_name || 'Unknown Customer'}</div>
                <div class="message-text">${msg.content}</div>
                <div class="sentiment-info">
                    <span class="sentiment-badge badge-${msg.sentiment}">${msg.sentiment}</span>
                    <span>Score: ${msg.score !== undefined ? msg.score.toFixed(2) : 'N/A'}</span>
                </div>
            `;

            container.appendChild(messageEl);
        });
    }

    updateSpeedometer(messages) {
        if (messages.length === 0) return;

        // Calculate average score
        const totalScore = messages.reduce((sum, msg) => sum + (msg.score || 0), 0);
        const avgScore = totalScore / messages.length;

        // Update needle position (-90deg to +90deg based on score -1 to +1)
        const needle = document.getElementById('needle');
        const angle = avgScore * 90; // Convert score to degrees
        needle.style.transform = `translateX(-50%) rotate(${angle}deg)`;

        // Update score display
        document.getElementById('sentimentScore').textContent = avgScore.toFixed(2);
    }

    displayAnalytics(analytics) {
        // Update Gmail stats
        document.getElementById('gmailPositive').textContent = analytics.gmail.positive;
        document.getElementById('gmailNegative').textContent = analytics.gmail.negative;
        document.getElementById('gmailNeutral').textContent = analytics.gmail.neutral;

        // Update Chat stats
        document.getElementById('chatPositive').textContent = analytics.chat.positive;
        document.getElementById('chatNegative').textContent = analytics.chat.negative;
        document.getElementById('chatNeutral').textContent = analytics.chat.neutral;
    }
}

// Initialize dashboard when page loads
document.addEventListener('DOMContentLoaded', () => {
    new SentimentDashboard();
});