import React, { memo } from 'react';

const Message = memo(({ messages, from, startIndex = 0, isSending, handleToggle, buttonText }) => {
    return (
        <div className={`message ${from}`}>
            <div className="message-content-wrapper">
                {messages.map((msg, index) => (
                    <div key={index} className="message-row">
                        {from === 'bot' && (
                            <div className="message-number">{startIndex + index + 1}</div>
                        )}
                        <div
                            className={`message-content ${from}`}
                            style={{ backgroundColor: msg.color }}
                        >
                            <div className="message-body">{msg.message}</div>
                            {from === 'bot' && <div className="message-agent-name">Provided by {msg.model}</div>}
                        </div>
                    </div>
                ))}
            </div>
            {from === 'bot' && buttonText && (
                <button className="toggle-button" onClick={handleToggle} disabled={isSending}>
                    {buttonText}
                </button>
            )}
        </div>
    );
});

export default Message;
