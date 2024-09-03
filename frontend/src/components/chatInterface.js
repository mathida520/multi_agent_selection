import React, {useState} from 'react';
import useChatBot from './useChatBot';
import './chatInterface.css'

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
            <img src="/images/Vector.png" alt="imglogo" style={{width:"13px",marginLeft:"5px"}}/>
            </button>
        </div>
    );
}

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