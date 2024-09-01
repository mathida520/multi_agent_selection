// src/components/Message.js
import React, {useState} from 'react';
import '../assets/styles/Message.css';

function Message({messages, from}) {
    const [expanded, setExpanded] = useState(false);

    const handleToggle = () => {
        setExpanded(!expanded);
    };

    const visibleMessages = expanded ? messages : [messages[0]];

    return (
        <div className={`message ${from}`}>
            <div className="message-content-wrapper">
                {visibleMessages.map((msg, index) => (
                    <div key={index} className={`message-content ${from}`}>
                        <strong>{msg.agentName}:</strong> {msg.message}
                    </div>
                ))}
                {messages.length > 1 && (
                    <button className="toggle-button" onClick={handleToggle}>
                        {expanded ? 'Show Less' : 'Show More'}
                    </button>
                )}
            </div>
        </div>
    );
}

export default Message;