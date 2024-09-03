import React from 'react';
import ChatBot from './components/chatInterface';
import './index.css';

function App() {
    return (
        <div className="App">
            <h1 style={{textAlign: 'center',fontSize:"30px",marginTop:"-25px"}}>Multi-agent comparison and collaboration system</h1>
            <h2 style={{textAlign: 'center',fontSize:"12px",marginTop:"-15px"}}>Select and orchestrate 100+ AI agents and applications to better finish your tasks and meet your demands</h2>
            <p><img src='/images/image 16.png' alt="img1" style={{width:"20px",marginLeft:"5px"}}/>
            <img src='/images/image 17.png' alt="img2" style={{width:"20px",marginLeft:"5px"}}/>
            <img src='/images/image 18.png' alt="img3" style={{width:"20px",marginLeft:"5px"}}/>
            <img src='/images/image 19.png' alt="img4" style={{width:"20px",marginLeft:"5px"}}/>
            <img src='/images/image 20.png' alt="img5" style={{width:"20px",marginLeft:"5px"}}/>
            <img src='/images/image 21.png' alt="img6" style={{width:"20px",marginLeft:"5px"}}/></p>
            <ChatBot/>
        </div>
    );
}

export default App;

