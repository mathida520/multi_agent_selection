import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from './pages/HomePage.js';
import ChatPage from './pages/ChatPage.js';

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<HomePage />} />
                <Route path="/c" element={<ChatPage />} />
            </Routes>
        </Router>
    );
}

export default App;

