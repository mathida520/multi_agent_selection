// src/components/MessageInput.js
import React, {useState} from 'react';
import '../assets/styles/MessageInput.css'

function MessageInput({onSendMessage}) {
    const [input, setInput] = useState('');

    const handleInputChange = (e) => {
        setInput(e.target.value);
    };

    const handleSendMessage = () => {
        if (input.trim()) {
            onSendMessage(input);
            setInput(''); // 清空输入框
        }
    };

    return (
        <div style={{marginTop: '10px'}}>
            <input
                type="text"
                value={input}
                onChange={handleInputChange}
                className="message-input-field"
                placeholder="Type your message here..."
            />
            <button onClick={handleSendMessage} className="message-send-button">
                Send
            </button>
        </div>
    );
}

export default MessageInput;