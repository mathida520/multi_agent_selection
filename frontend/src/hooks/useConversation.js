import {useState} from 'react';
import {sendMessageToAPI} from '../api/backend';

function useConversation() {
    const [messages, setMessages] = useState([]);

    const handleSendMessage = async (input) => {
        if (input.trim()) {
            const userMessage = {
                from: 'user',
                messages: [{model: "User", message: input}]
            };
            setMessages((prevMessages) => [...prevMessages, userMessage]);

            try {
                const botMessage = {
                    from: 'bot',
                    messages: await sendMessageToAPI(input)
                };
                setMessages((prevMessages) => [...prevMessages, botMessage]);

            } catch (error) {
                console.error('Error fetching AI response:', error);
            }
        }
    };

    return {messages, handleSendMessage};
}

export default useConversation;
