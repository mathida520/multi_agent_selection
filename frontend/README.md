# 项目前端结构
- **public/**：存放公共资源
    - `images`：图像文件夹
    - `favicon.ico`
    - `index.html`：主页面文件
    - `logo192.png`
    - `manifest.json`
- **src/**
    - **api/**：
        - `backend.js`：后端API调用函数
    - **components/**：组件文件夹
        - `chatInterface.css`：chatInterface 组件的样式文件
        - `chatInterface.js`：chatInterface 组件
        - `useChatBot.js`
    - **pages/**：
        - `ChatPage.js`：聊天页面
        - `HomePage.js`：首页
    - `App.css`
    - `App.js`
    - `index.css`
    - `index.js`
    - `logo.svg`
- **package.json**
- **README.md**

# message 参数格式

## 响应
没有color时默认为灰色
```json
[
  {
    "model": "Agent 1",
    "message": "This is the first message from Agent 1.",
    "color": "#f1c40f"
  },
  {
    "model": "Agent 2",
    "message": "This is a message from Agent 2.",
    "color": "#2ecc71"
  },
  {
    "model": "Agent 3",
    "message": "This is a message from Agent 3.",
    "color": "#e74c3c"
  }
]
```

## 请求

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Hello, how are you"
    }
  ]
}
```