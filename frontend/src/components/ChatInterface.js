import React, {useEffect, useRef, useState} from 'react';
import {animateScroll} from 'react-scroll';
import { useLocation } from 'react-router-dom';
import useChatBot from './UseChatBot';
import './ChatInterface.css';

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
                <img src="/images/Vector.png" alt="imglogo" style={{width: "13px", marginLeft: "5px"}}/>
            </button>
        </div>
    );
}

function Message({messages, from}) {
    const [expanded, setExpanded] = useState(false);

    // 透明度处理
    const [visibility, setVisibility] = useState({});

    const messageRefs = useRef([]); // 使用ref数组存储每条消息的DOM引用

    // 初始化 IntersectionObserver
    useEffect(() => {
        const currentMessageRefs = messageRefs.current; // 在 effect 内部创建一个局部变量

        const observer = new IntersectionObserver((entries) => {
            entries.forEach((entry) => {
                setVisibility((prev) => ({
                    ...prev,
                    [entry.target.dataset.index]: entry.intersectionRatio,
                }));
            });
        }, {
            root: null,
            rootMargin: '0px',
            threshold: Array.from({length: 11}, (_, i) => i / 10),
        });

        currentMessageRefs.forEach((message) => {
            if (message) {
                observer.observe(message);
            }
        });

        return () => {
            currentMessageRefs.forEach((message) => {
                if (message) {
                    observer.unobserve(message);
                }
            });
        };
    }, [messages, expanded]);


    const handleToggle = () => {
        setExpanded(!expanded);
    };

    const visibleMessages = expanded ? messages : [messages[0]];

    return (
        <div className={`message ${from}`}>
            <div className="message-content-wrapper">
                {visibleMessages.map((msg, index) => (
                    <div
                        key={index}
                        className={`message-content ${from}`}
                        data-index={index}
                        ref={(el) => (messageRefs.current[index] = el)} // 给每条消息绑定ref
                        style={{
                            backgroundColor: msg.color,
                            opacity: visibility[index] || 0, // 根据可见比例设置透明度
                            transition: 'opacity 0.5s', // 平滑过渡
                            paddingBottom: from === 'bot' ? '20px' : '10px', // 只为AI消息留出底部空间
                        }}>
                        <div className="message-body">
                            {msg.message}
                        </div>

                        {/* 如果消息是AI的，展示 model 在底部 */}
                        {from === 'bot' && (
                            <div className="message-agent-name">
                                Provided by {msg.model}
                            </div>
                        )}
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
    const location = useLocation();
    const queryParams = new URLSearchParams(location.search);
    const inputQuery = queryParams.get('query');

    const { messages, handleSendMessage } = useChatBot();
    const sentRef = useRef(false);

    useEffect(() => {
        if (inputQuery && !sentRef.current) {
            handleSendMessage(inputQuery);
            sentRef.current = true;
        }
    }, [inputQuery]);

    // 滚动到底部的效果
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
                    <Message key={index} messages={msg.messages} from={msg.from}/>
                ))}
            </div>
            <MessageInput onSendMessage={handleSendMessage}/>
        </div>
    );
}

export default ChatBot;
