import React, { memo, useState } from 'react';

const MessageInput = memo(({ onSendMessage, isSending }) => {
    const [input, setInput] = useState('');

    const handleSend = () => {
        if (input.trim()) {
            onSendMessage(input);
            setInput('');
        }
    };

    const handleKeyDown = (e) => {
        if (e.key === 'Enter' && !isSending) {
            handleSend();
        }
    };

    return (
        <div className="message-input-container">
            <input
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyDown={handleKeyDown}
                className="message-input-field"
                placeholder={isSending ? "Generating a response, please wait..." : "Anything I can help you with?"}
                disabled={isSending}
            />
            <button onClick={handleSend} className="message-send-button" disabled={isSending}>
                <img src="/images/Vector.png" alt="Send" style={{ width: "13px", marginLeft: "5px" }} />
            </button>
        </div>
    );
});

export default MessageInput;
