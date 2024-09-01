// src/App.js
import React from 'react';
import ChatBot from './components/ChatBot';
import './index.css';  // 确保引入全局样式文件
// import './assets/styles/base.css';  // 引入全局样式

function App() {
    return (
        <div className="App">
            <h1 style={{textAlign: 'center'}}>AI Chatbot</h1>
            <ChatBot/>
        </div>
    );
}

export default App;