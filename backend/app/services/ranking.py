from typing import List, Dict
import random

# from backend.app.services.generation import get_local_response


def rerank_models(models: Dict) -> Dict:
    priority_list = ['glm-4', 'qwen-plus', "llama-13b-chat", "azure-gpt-4o"]
    return {key: models[key] for key in priority_list if key in models}


def rerank_responses(responses: List[Dict]) -> List[Dict]:
    random.shuffle(responses)
    return responses
