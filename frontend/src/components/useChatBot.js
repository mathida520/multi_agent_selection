import {useState} from 'react';
import {sendMessageToAPI} from '../api/backend';

function useChatBot() {
    const [messages, setMessages] = useState([]);

    const handleSendMessage = async (input) => {
        if (input.trim()) {
            const userMessage = {
                from: 'user',
                messages: [
                    {agentName: "User", message: input}
                ]
            };
            setMessages((prevMessages) => [...prevMessages, userMessage]);

            try {
                // 发送请求到Flask后端，并获取响应数据
                const data = await sendMessageToAPI(input);

                const botMessage = {
                    from: 'bot',
                    messages: data  // 假设API返回的是数组对象格式
                };

                setMessages((prevMessages) => [...prevMessages, botMessage]);
            } catch (error) {
                console.error('Error fetching AI response:', error);
            }
        }
    };

    return {messages, handleSendMessage};
}

export default useChatBot;