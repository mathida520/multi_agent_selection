# my-chatbot-app 项目结构

- **README.md**
- **package-lock.json**
- **package.json**
- **public/**
    - `favicon.ico`
    - `index.html`
    - `logo192.png`
    - `logo512.png`
    - `manifest.json`
    - `robots.txt`
- **src/**
    - `App.css` - 全局样式文件
    - `App.js` - 主应用组件
    - `App.test.js`
    - **assets/**
        - **styles/**
            - `ChatBot.css` - ChatBot 组件的样式
            - `Message.css` - Message 组件的样式
            - `MessageInput.css` - MessageInput 组件的样式
    - **components/** - 用于存放可重用组件
        - `ChatBot.js` - ChatBot 组件
        - `Message.js` - 用于渲染单条消息的组件
        - `MessageInput.js` 用于渲染输入消息的组件
    - **hooks/** - 自定义钩子文件夹
        - `useChatBot.js` - 用于处理聊天逻辑的自定义 Hook（可选）
    - `index.css` - 全局样式文件
    - `index.js` - 入口 JavaScript 文件
    - `logo.svg`
    - `reportWebVitals.js`
    - `setupTests.js`
    - **utils/** - 工具函数文件夹
        - `api.js` - API 调用相关的工具函数

# message 参数格式

## 响应

```json
[
  {
    "agentName": "Agent 1",
    "message": "This is the first message from Agent 1."
  },
  {
    "agentName": "Agent 2",
    "message": "This is a message from Agent 2."
  },
  {
    "agentName": "Agent 3",
    "message": "This is a message from Agent 3."
  }
]
```