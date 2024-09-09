export const sendMessageToAPI = async (input) => {
  const baseUrl = process.env.REACT_APP_BACK_URL_1;
  const endpoint = "/chat";
  const apiUrl = `${baseUrl}${endpoint}`;
  try {
    const response = await fetch(apiUrl, {
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

    return await response.json();
  } catch (error) {
    console.error('Error in sendMessageToAPI:', error);
    return [];
  }
};