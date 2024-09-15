const baseUrl = process.env.REACT_APP_BACK_URL_1;
const headers = {'Content-Type': 'application/json'};

const generatePrimary = async (input) => {
    const body = JSON.stringify({messages: [{role: 'user', content: input}]});
    try {
        const response = await fetch(
            `${baseUrl}/api/gen/prim`,
            {
                method: 'POST',
                headers,
                body,
            }
        );
        return await response.json();
    } catch (error) {
        console.error('Error:', error.message || error);
        throw error;
    }
};

const generateAuxiliary = async (input, modelName) => {
    const body = JSON.stringify(
        {
            messages: [{role: 'user', content: input}],
            modelName: modelName,
        }
    );
    try {
        const response = await fetch(
            `${baseUrl}/api/gen/auxi`,
            {
                method: 'POST',
                headers,
                body,
            }
        );
        return await response.json();
    } catch (error) {
        console.error('Error:', error.message || error);
        throw error;
    }
};

export { generatePrimary, generateAuxiliary}