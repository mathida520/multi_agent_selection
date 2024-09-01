// src/components/ChatBot.js
import React from 'react';
import useChatBot from '../hooks/useChatBot';
import Message from "./Message";
import MessageInput from './MessageInput';
import '../assets/styles/ChatBot.css';

function ChatBot() {
    const {messages, handleSendMessage} = useChatBot();

  return (
    <div className="chatbot-container">
      <div className="chatbot-messages">
        {messages.map((msg, index) => (
          <Message key={index} messages={msg.messages} from={msg.from} />
        ))}
      </div>
      <MessageInput onSendMessage={handleSendMessage} />
    </div>
  );
}

export default ChatBot;