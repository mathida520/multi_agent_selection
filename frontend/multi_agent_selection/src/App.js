// src/App.js
import React from 'react';
import ChatBot from './components/ChatBot';
import './index.css';  // 确保引入全局样式文件
import img1 from './img/image 16.png'
import img2 from './img/image 17.png'
import img3 from './img/image 18.png'
import img4 from './img/image 19.png'
import img5 from './img/image 20.png'
import img6 from './img/image 21.png'
// import './assets/styles/base.css';  // 引入全局样式

function App() {
    return (
        <div className="App">
            <h1 style={{textAlign: 'center',fontSize:"30px",marginTop:"-25px"}}>Multi-agent comparison and collaboration system</h1>
            <h2 style={{textAlign: 'center',fontSize:"12px",marginTop:"-15px"}}>Select and orchestrate 100+ AI agents and applications to better finish your tasks and meet your demands</h2>
            <p><img src={img1} alt="img1" style={{width:"20px",marginLeft:"5px"}}/>
            <img src={img2} alt="img2" style={{width:"20px",marginLeft:"5px"}}/>
            <img src={img3} alt="img3" style={{width:"20px",marginLeft:"5px"}}/>
            <img src={img4} alt="img4" style={{width:"20px",marginLeft:"5px"}}/>
            <img src={img5} alt="img5" style={{width:"20px",marginLeft:"5px"}}/>
            <img src={img6} alt="img6" style={{width:"20px",marginLeft:"5px"}}/></p>
            <ChatBot/>
        </div>
    );
}

export default App;

