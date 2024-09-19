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
            return response.json()

        except requests.exceptions.Timeout:
            return {"error": "Request timed out"}
        except requests.exceptions.ConnectionError:
            return {"error": "Connection error"}
        except requests.exceptions.HTTPError as http_err:
            return {"error": f"HTTP error occurred: {http_err}"}
        except Exception as err:
            return {"error": f"An error occurred: {err}"}