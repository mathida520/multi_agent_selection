import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './HomePage.css';

function HomePage() {
    const navigate = useNavigate();
    const [input, setInput] = useState('');

    const handleInputChange = (e) => {
        setInput(e.target.value);
    };

    const handleSearch = () => {
        if (input.trim()) {
            navigate('/c', { state: { query: input } });
        }
    };

    const handleKeyDown = (e) => {
        if (e.key === 'Enter') {
            handleSearch();
        }
    };

    return (
        <div className="home-container">
            <h1 className="title">Multi-agent comparison and collaboration system</h1>
            <h2 className="subtitle">Select and orchestrate 100+ AI agents and applications to better finish your tasks and meet your demands</h2>
            <div className="icons">
                <img src='/images/image 16.png' alt="icon1"/>
                <img src='/images/image 17.png' alt="icon2"/>
                <img src='/images/image 18.png' alt="icon3"/>
                <img src='/images/image 19.png' alt="icon4"/>
                <img src='/images/image 20.png' alt="icon5"/>
                <img src='/images/image 21.png' alt="icon6"/>
            </div>
            <div className="search-container">
                <input
                    type="text"
                    placeholder="Anything I can help you do?"
                    value={input}
                    onChange={handleInputChange}
                    onKeyDown={handleKeyDown}
                />
                <button onClick={handleSearch} className="search-button">
                    <img src="/images/Vector.png" alt="Send" style={{ width: "13px", marginLeft: "5px" }} />
                </button>
            </div>
            <div className="example-container">
                <div className="example-title">For example:</div>
                <div className="example-queries">
                    <div className="query-wrapper left">
                        <button className="query-button">Help me settle down a trip next week to NYC</button>
                    </div>
                    <div className="query-wrapper right">
                        <button className="query-button">Help me order a restaurant for tonight's family gathering</button>
                    </div>
                    <div className="query-wrapper left">
                        <button className="query-button">Help me prepare for my interview with John tomorrow</button>
                    </div>
                    <div className="query-wrapper right">
                        <button className="query-button">Invest my existing account balance based on the performance of yesterday's trading strategy</button>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default HomePage;
