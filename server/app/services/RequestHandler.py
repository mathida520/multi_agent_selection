import requests
from typing import Dict, Union

class RequestHandler:
    @staticmethod
    def post(url: str, headers: Dict, data: Union[Dict, str] = None, json: Dict = None, timeout: int = 10) -> Dict:
        return RequestHandler._handle_request("POST", url, headers, data, json, timeout)
    
    @staticmethod
    def get(url: str, headers: Dict = None, params: Dict = None, timeout: int = 10) -> Dict:
        return RequestHandler._handle_request("GET", url, headers, params, None, timeout)
    
    @staticmethod
    def put(url: str, headers: Dict, data: Union[Dict, str] = None, json: Dict = None, timeout: int = 10) -> Dict:
        return RequestHandler._handle_request("PUT", url, headers, data, json, timeout)
    
    @staticmethod
    def delete(url: str, headers: Dict, timeout: int = 10) -> Dict:
        return RequestHandler._handle_request("DELETE", url, headers, None, None, timeout)

    @staticmethod
    def _handle_request(method: str, url: str, headers: Dict = None, data: Union[Dict, str] = None, json: Dict = None, timeout: int = 10) -> Dict:
        try:
            if method == "POST":
                response = requests.post(url, headers=headers, data=data, json=json, timeout=timeout)
            elif method == "GET":
                response = requests.get(url, headers=headers, params=data, timeout=timeout)
            elif method == "PUT":
                response = requests.put(url, headers=headers, data=data, json=json, timeout=timeout)
            elif method == "DELETE":
                response = requests.delete(url, headers=headers, timeout=timeout)
            else:
                return {"error": "Unsupported HTTP method"}

            response.raise_for_status()
            return response

        except requests.exceptions.Timeout:
            return {"error": "Request timed out"}
        except requests.exceptions.ConnectionError:
            return {"error": "Connection error"}
        except requests.exceptions.HTTPError as http_err:
            return {"error": f"HTTP error occurred: {http_err}"}
        except Exception as err:
            return {"error": f"An error occurred: {err}"}
        
if __name__ == "__main__":
    headers = {
        "Authorization": "api Key"
    }
    payload = {
        "prompt": "cyberpunk cat"
    }
    completion = RequestHandler.post("https://api.cloudflare.com/client/v4/accounts/5eccfadce82e2e37f4dba158506a75a9/ai/run/@cf/stabilityai/stable-diffusion-xl-base-1.0", 
                                     headers=headers, 
                                     json=payload, 
                                     timeout=600)
    
    print(completion)

    # import http.client
    # import json

    # # Correct host without 'https://'
    # conn = http.client.HTTPSConnection("api.cloudflare.com")

    # # Your payload
    # payload = json.dumps({
    #     "prompt": "cyberpunk cat"
    # })

    # # Headers
    # headers = {
    #     'Authorization': 'Bearer OhkOjKABesrD2A3f24bBDNkyj9qr5LDW3PLdTtY-',  # Add your correct bearer token
    #     'Content-Type': 'application/json'
    # }

    # # Making the POST request
    # conn.request("POST", "/client/v4/accounts/5eccfadce82e2e37f4dba158506a75a9/ai/run/@cf/lykon/dreamshaper-8-lcm", payload, headers)

    # # Getting the response
    # res = conn.getresponse()
    # data = res.read()
    # with open('output_image.png', 'wb') as f:
    #     f.write(data)
    # # Print the result

    