import React, {useEffect, useRef, useState} from 'react';
import useChatBot from './useChatBot';
import './chatInterface.css';
import {animateScroll} from 'react-scroll';


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
        const observer = new IntersectionObserver((entries) => {
            entries.forEach((entry) => {
                // 根据消息在视口中的可见比例设置透明度
                setVisibility((prev) => ({
                    ...prev,
                    [entry.target.dataset.index]: entry.intersectionRatio,
                }));
            });
        }, {
            root: null, // 设置 root 为 null，表示在视口内观察
            rootMargin: '0px',
            threshold: Array.from({length: 11}, (_, i) => i / 10), // 设置多个阈值以捕获渐变透明度
        });

        // 观察所有消息
        messageRefs.current.forEach((message) => {
            if (message) {
                observer.observe(message);
            }
        });

        // 清除 observer
        return () => {
            messageRefs.current.forEach((message) => {
                if (message) {
                    observer.unobserve(message);
                }
            });
        };
    }, [messages, expanded]); // 监听 expanded，确保展开的消息也能被观察

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
                        }}>
                        <div className="message-body">
                            {msg.message}
                        </div>

                        {/* 如果消息是AI的，展示 agentName 在底部 */}
                        {from === 'bot' && (
                            <div className="message-agent-name">
                                Provided by {msg.agentName}
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
    const {messages, handleSendMessage} = useChatBot();

    // Scroll to bottom whenever messages update
    useEffect(() => {
        animateScroll.scrollToBottom({
            containerId: 'chatbot-messages',
            duration: 100, // smooth scroll duration in ms
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