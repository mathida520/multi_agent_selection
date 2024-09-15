// useConversation.js
import { useState, useCallback } from 'react';
import { generatePrimary, generateAuxiliary } from '../api/generateContent.js';

function useConversation() {
    const [messages, setMessages] = useState([]);
    const [remainingModels, setRemainingModels] = useState([]);
    const [isSending, setIsSending] = useState(false);
    const [messageCount, setMessageCount] = useState({ primaryCount: 0, auxiliaryCount: 0 });
    const [inputString, setInputString] = useState('');

    const createMessage = useCallback((from, messageContent) => ({
        from,
        messages: Array.isArray(messageContent)
            ? messageContent
            : [{ model: from === 'bot' ? 'Bot' : 'User', message: messageContent }],
    }), []);

    const handlePrimary = useCallback(async (input) => {
        if (!input.trim()) return;

        setInputString(input);
        setIsSending(true);

        const userMessage = createMessage('user', input);
        setMessages((prev) => [...prev, userMessage]);

        try {
            const data = await generatePrimary(input);
            setRemainingModels(data.remainingModels);
            const botMessages = createMessage('bot', data.modelsResponse);
            setMessages((prev) => [...prev, botMessages]);
            setMessageCount({primaryCount: data.modelsResponse.length, auxiliaryCount: data.remainingModels.length});

        } catch (error) {
            console.error('Error fetching AI response:', error);
        } finally {
            setIsSending(false);
        }
    }, [createMessage]);

    const handleAuxiliary = useCallback(async () => {
        if (remainingModels.length === 0) return;
        setIsSending(true);

        try {
            const lastModel = remainingModels[remainingModels.length - 1];
            const data = await generateAuxiliary(inputString, lastModel);

            setMessages((prev) => [...prev, createMessage('bot', data)]);
            setRemainingModels((prev) => prev.slice(0, -1));
        } catch (error) {
            console.error('Error fetching auxiliary response:', error);
        } finally {
            setIsSending(false);
        }
    }, [remainingModels, inputString, createMessage]);

    return { messages, handlePrimary, handleAuxiliary, isSending, messageCount };
}

export default useConversation;
