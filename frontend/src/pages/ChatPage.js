import React, {memo, useCallback, useEffect, useRef, useState} from 'react';
import { animateScroll } from 'react-scroll';
import { useLocation } from 'react-router-dom';
import useConversation from '../hooks/useConversation';
import './ChatPage.css';

const MessageInput = memo(({ onSendMessage }) => {
    const [input, setInput] = useState('');

    const handleInputChange = useCallback((e) => {
        setInput(e.target.value);
    }, []);

    const handleSendMessage = useCallback(() => {
        if (input.trim()) {
            onSendMessage(input);
            setInput('');
        }
    }, [input, onSendMessage]);

    return (
        <div style={{ marginTop: '10px' }}>
            <input
                type="text"
                value={input}
                onChange={handleInputChange}
                className="message-input-field"
                placeholder="Anything I can help you do?"
            />
            <button onClick={handleSendMessage} className="message-send-button">
                <img src="/images/Vector.png" alt="imglogo" style={{ width: "13px", marginLeft: "5px" }} />
            </button>
        </div>
    );
});


const Message = memo(({ messages, from }) => {
    const [expanded, setExpanded] = useState(false);
    const [visibility, setVisibility] = useState({});
    const messageRefs = useRef([]);

    useEffect(() => {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach((entry) => {
                setVisibility((prev) => ({
                    ...prev,
                    [entry.target.dataset.index]: entry.intersectionRatio,
                }));
            });
        }, {
            root: null,
            threshold: Array.from({ length: 11 }, (_, i) => i / 10),
        });

        messageRefs.current.forEach((message) => {
            if (message) observer.observe(message);
        });

        return () => {
            messageRefs.current.forEach((message) => {
                if (message) observer.unobserve(message);
            });
        };
    }, [messages, expanded]);

    const handleToggle = () => setExpanded(!expanded);

    return (
        <div className={`message ${from}`}>
            <div className="message-content-wrapper">
                {(expanded ? messages : [messages[0]]).map((msg, index) => (
                    <div
                        key={index}
                        className={`message-content ${from}`}
                        data-index={index}
                        ref={(el) => { messageRefs.current[index] = el; }}
                        style={{
                            backgroundColor: msg.color,
                            opacity: visibility[index] || 0,
                            paddingBottom: from === 'bot' ? '20px' : '10px',
                        }}>
                        <div className="message-body">{msg.message}</div>
                        {from === 'bot' && <div className="message-agent-name">Provided by {msg.model}</div>}
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
});

function ChatPage() {
    const location = useLocation();
    const inputQuery = new URLSearchParams(location.search).get('query');
    const { messages, handleSendMessage } = useConversation();
    const sentRef = useRef(false);

    useEffect(() => {
        if (inputQuery && !sentRef.current) {
            handleSendMessage(inputQuery);
            sentRef.current = true;
        }
    }, [inputQuery]);

    useEffect(() => {
        animateScroll.scrollToBottom({
            containerId: 'chatbot-messages',
            duration: 100,
        });
    }, [messages]);

    return (
        <div className="chatbot-container">
            <div id="chatbot-messages" className="chatbot-messages">
                {messages.map((msg, index) => (
                    <Message key={index} messages={msg.messages} from={msg.from} />
                ))}
            </div>
            <MessageInput onSendMessage={handleSendMessage} />
        </div>
    );
}

export default ChatPage;
