from typing import List, Dict


# todo
def evaluate_prompt(
    instruction: str,
    input_text: str,
    output1: str,
    output2: str,
    criteria: List
) -> Dict[str, str]:
    # Code: https://github.com/kixlab/EvalLM/blob/main/src/api/prompts.ts#L3
    # Paper: https://arxiv.org/pdf/2309.13633   B.1 Automatic Evaluation
    criteria_section = "\n".join([f"- {criterion['name']}: {criterion['description']}" for criterion in criteria])
    user_prompt = f"""# Task Description

We would like to request your feedback on the performance of two AI assistants responding to a user's instruction. Each assistant performed the instruction on the same input. In the feedback, please rate the quality of the responses on the given set of criteria. The user's instruction, input, the two responses, and the criteria are provided below.

Please give feedback on the responses for each criteria. First, provide a comprehensive explanation comparing the two assistants in their ability to satisfy the criterion. You should justify your judgement by providing substantial detail about your reasoning. Ensure that you only write comments about one criterion at a time. Avoid giving feedback on other aspects of the responses that are not described in the criteria. Then, for each assistant, list a maximum of five words or short phrases from their response that illustrate what you described in your explanation. Avoid listing whole sentences or long phrases as evidence. If the whole response is needed as evidence, add the token "$WHOLE$" to the list. Finally, write your scores for each assistant on the criterion. The score should be on a scale of 1 to 10, where a higher score indicates that the assistant's response was better at satisfying the criterion. Avoid any potential bias and ensure that the order in which the responses were presented does not affect your judgement. Finally, ONLY return your feedback and scores as a valid JSON object by following the Output Format provided below.

## Criteria

{criteria_section}

## Instruction

{instruction}

## Input

{input_text}

## Assistant 1's Response

{output1}

## Assistant 2's Response

{output2}

## Output Format

```json
{{
    <criterion name>: {{
        "explanation": <comprehensive and detailed comparison of the assistants' ability to satisfy the criterion>,
        "assistant_1": {{
            "evidence": [<maximum of 5 words or short phrases from the assistant's response that serve as evidence for your feedback>],
            "score": <score on the criterion>
        }},
        "assistant_2": {{
            "evidence": [<maximum of 5 words or short phrases from the assistant's response that serve as evidence for your feedback>], 
            "score": <score on the criterion>
        }}
    }},
...
}}
"""  # noqa

    return {
        "system": "You are a helpful and precise assistant that can check the quality of responses by other AI assistants for a given user instruction. You can objectively evaluate the holistic quality of responses by assessing how well the responses satisfy a set of quality criteria. You should provide comprehensive feedback on the responses according to each of these criteria and provide detailed justification for your feedback. If you refer to specific fragments of the responses in your feedback, you should also return these fragments as evidence. You should return your final answer as a valid JSON object.",  # noqa
        "user": user_prompt
    }
