from app.services.task_handler import PICTURE_GENERATION

general=["gpt-4o","qwen-plus","llama-70b-chat","llama-13b-chat","glm-4"]
image_generation=["dreamshaper-8-lcm","stable-diffusion-xl-base-1.0"]

def get_model_list(task_type):
    if task_type == PICTURE_GENERATION:
        return image_generation
    else:
        return general

# todo 获取到有哪些模型之后在这里更新模型清单
def set_models(task_type, models):
    if task_type == PICTURE_GENERATION:
        image_generation.extend(models)
    else:
        general.extend(models)
