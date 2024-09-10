const baseUrl = process.env.REACT_APP_BACK_URL_1;
const endpoint = "/chat";
const apiUrl = `${baseUrl}${endpoint}`;

const headers = {'Content-Type': 'application/json'};

export const sendMessageToAPI = async (input) => {
    const body = JSON.stringify({messages: [{role: 'user', content: input}]});
    try {
        const response = await fetch(apiUrl, {
            method: 'POST',
            headers,
            body,
        });

    return await response.json();
    } catch (error) {
        console.error('Error in sendMessageToAPI:', error.message || error);
        throw error;
    }
};
