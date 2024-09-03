// src/components/MessageInput.js
import React, {useState} from 'react';
import '../assets/styles/MessageInput.css'
import imglogo from "../img/Vector.png"

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
                placeholder="Anything I can help you do?"
            />
            <button onClick={handleSendMessage} className="message-send-button">
            <img src={imglogo} alt="imglogo" style={{width:"13px",marginLeft:"5px"}}/> 
            </button>
        </div>
    );
}

export default MessageInput;