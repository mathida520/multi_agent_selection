export const sendMessageToAPI = async (input) => {
  try {
    const response = await fetch('http://18.140.117.184:11435/chat', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        messages: [
          {
            role: 'user',
            content: input
          }
        ]
      }),
    });

    if (!response.ok) {
      throw new Error('Network response was not ok');
    }

    const data = await response.json();
    return data;  // 假设Flask后端返回的是与之前格式一致的数组对象
  } catch (error) {
    console.error('Error in sendMessageToAPI:', error);
    return [];
  }
};