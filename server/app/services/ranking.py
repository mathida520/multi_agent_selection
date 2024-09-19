from typing import List, Dict

import random


def rerank_models(models: List[str]) -> List[str]:
    random.shuffle(models)

    return models


def rerank_responses(responses: List[Dict]) -> List[Dict]:
    random.shuffle(responses)

    return responses
